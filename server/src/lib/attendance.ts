import { ApiError } from './errors.js';
import { audit, newId, nowIso, type DB } from './db.js';
import { isEnrolled } from './access.js';
import type { AttendanceMethod, AttendanceRow, AttendanceStatus, SessionRow } from './types.js';

export interface CheckInInput {
  session: SessionRow;
  studentId: string;
  method: AttendanceMethod;
  /** Ai bấm ghi nhận: sinh viên tự quét thì chính họ, giảng viên quét thì là giảng viên. */
  recordedBy: string;
  deviceId?: string | null;
  clientUuid?: string | null;
  /** Thời điểm quét thực tế trên máy, dùng cho bản ghi offline đồng bộ muộn. */
  scannedAt?: string | null;
  note?: string | null;
}

export interface CheckInResult {
  record: AttendanceRow;
  /** true nếu bản ghi đã tồn tại từ trước (đồng bộ lại cùng clientUuid, hoặc quét trùng). */
  duplicate: boolean;
}

/** Quét lúc nào thì tính đi muộn — mốc là giờ bắt đầu cộng `late_after_min`. */
export function resolveStatus(session: SessionRow, scannedAtIso: string): AttendanceStatus {
  const lateFrom = new Date(session.starts_at).getTime() + session.late_after_min * 60_000;
  return new Date(scannedAtIso).getTime() > lateFrom ? 'late' : 'present';
}

export function findByClientUuid(db: DB, clientUuid: string): AttendanceRow | undefined {
  return db.prepare(`SELECT * FROM attendance_records WHERE client_uuid = ?`).get(clientUuid) as
    | AttendanceRow
    | undefined;
}

/**
 * Ghi nhận một lượt điểm danh.
 *
 * Idempotent theo `clientUuid`: app di động sinh UUID cho mỗi lần quét và giữ
 * nguyên khi gửi lại, nên hàng đợi offline có thể đồng bộ nhiều lần an toàn.
 */
export function recordCheckIn(db: DB, input: CheckInInput): CheckInResult {
  const { session, studentId, method, recordedBy } = input;
  const scannedAt = input.scannedAt ?? nowIso();

  if (input.clientUuid) {
    const existing = findByClientUuid(db, input.clientUuid);
    if (existing) return { record: existing, duplicate: true };
  }

  if (session.checkin_state !== 'open') {
    throw ApiError.conflict('SESSION_CLOSED', 'Buổi học chưa mở hoặc đã đóng điểm danh', { sessionId: session.id });
  }
  if (!isEnrolled(db, session.class_id, studentId)) {
    throw ApiError.forbidden('NOT_ENROLLED', 'Sinh viên không thuộc lớp học phần này', { sessionId: session.id });
  }

  const prior = db
    .prepare(`SELECT * FROM attendance_records WHERE session_id = ? AND student_id = ?`)
    .get(session.id, studentId) as AttendanceRow | undefined;

  if (prior && (prior.status === 'present' || prior.status === 'late')) {
    return { record: prior, duplicate: true };
  }

  const status = resolveStatus(session, scannedAt);
  const now = nowIso();

  if (prior) {
    // Đã có bản ghi 'absent' hoặc 'excused' — ghi đè bằng lượt quét thật.
    db.prepare(
      `UPDATE attendance_records
          SET status = ?, method = ?, checked_in_at = ?, recorded_by = ?, device_id = ?,
              client_uuid = COALESCE(?, client_uuid), note = ?, updated_at = ?
        WHERE id = ?`,
    ).run(status, method, scannedAt, recordedBy, input.deviceId ?? null, input.clientUuid ?? null, input.note ?? null, now, prior.id);
  } else {
    db.prepare(
      `INSERT INTO attendance_records
         (id, session_id, student_id, status, method, checked_in_at, recorded_by, device_id, client_uuid, note, created_at, updated_at)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
    ).run(
      newId('att'),
      session.id,
      studentId,
      status,
      method,
      scannedAt,
      recordedBy,
      input.deviceId ?? null,
      input.clientUuid ?? null,
      input.note ?? null,
      now,
      now,
    );
  }

  const record = db
    .prepare(`SELECT * FROM attendance_records WHERE session_id = ? AND student_id = ?`)
    .get(session.id, studentId) as AttendanceRow;

  audit(db, {
    actorId: recordedBy,
    action: 'attendance.check_in',
    entity: 'attendance',
    entityId: record.id,
    meta: { sessionId: session.id, studentId, status, method },
  });

  return { record, duplicate: false };
}

/** Đóng điểm danh: ai chưa có bản ghi thì tính vắng. */
export function closeSessionAttendance(db: DB, session: SessionRow, actorId: string): number {
  const now = nowIso();
  const missing = db
    .prepare(
      `SELECT e.student_id FROM enrollments e
        WHERE e.class_id = ?
          AND NOT EXISTS (SELECT 1 FROM attendance_records a WHERE a.session_id = ? AND a.student_id = e.student_id)`,
    )
    .all(session.class_id, session.id) as Array<{ student_id: string }>;

  const insert = db.prepare(
    `INSERT INTO attendance_records
       (id, session_id, student_id, status, method, checked_in_at, recorded_by, created_at, updated_at)
     VALUES (?, ?, ?, 'absent', 'manual', NULL, ?, ?, ?)`,
  );
  for (const row of missing) insert.run(newId('att'), session.id, row.student_id, actorId, now, now);

  db.prepare(`UPDATE class_sessions SET checkin_state = 'closed', closed_at = ? WHERE id = ?`).run(now, session.id);
  audit(db, {
    actorId,
    action: 'session.close',
    entity: 'session',
    entityId: session.id,
    meta: { markedAbsent: missing.length },
  });
  return missing.length;
}

export function serializeAttendance(row: AttendanceRow) {
  return {
    id: row.id,
    sessionId: row.session_id,
    studentId: row.student_id,
    status: row.status,
    method: row.method,
    checkedInAt: row.checked_in_at,
    recordedBy: row.recorded_by,
    note: row.note,
    clientUuid: row.client_uuid,
    updatedAt: row.updated_at,
  };
}
