import { audit, newId, nowIso, type DB } from './db.js';
import type { LeaveRow } from './types.js';

/**
 * Áp dụng đơn phép đã duyệt lên bảng điểm danh.
 *
 * Mọi buổi học nằm trong khoảng ngày xin phép, thuộc lớp sinh viên có đăng ký
 * (giới hạn theo `class_id` nếu đơn chỉ xin nghỉ một lớp), sẽ được đánh dấu
 * 'excused'. Buổi nào sinh viên đã thực sự có mặt thì giữ nguyên — đơn phép
 * không được xoá dữ liệu điểm danh thật.
 */
export function applyApprovedLeave(db: DB, leave: LeaveRow, actorId: string): number {
  const now = nowIso();
  const sessions = db
    .prepare(
      `SELECT s.id FROM class_sessions s
         JOIN enrollments e ON e.class_id = s.class_id AND e.student_id = ?
        WHERE date(s.starts_at) BETWEEN date(?) AND date(?)
          AND (? IS NULL OR s.class_id = ?)`,
    )
    .all(leave.student_id, leave.start_date, leave.end_date, leave.class_id, leave.class_id) as Array<{ id: string }>;

  const stmt = db.prepare(
    `INSERT INTO attendance_records
       (id, session_id, student_id, status, method, checked_in_at, recorded_by, note, created_at, updated_at)
     VALUES (?, ?, ?, 'excused', 'leave', NULL, ?, ?, ?, ?)
     ON CONFLICT (session_id, student_id) DO UPDATE SET
       status = 'excused', method = 'leave', recorded_by = excluded.recorded_by,
       note = excluded.note, updated_at = excluded.updated_at
     WHERE attendance_records.status NOT IN ('present', 'late')`,
  );

  let applied = 0;
  for (const s of sessions) {
    applied += stmt.run(newId('att'), s.id, leave.student_id, actorId, `Nghỉ có phép #${leave.id}`, now, now).changes;
  }

  audit(db, {
    actorId,
    action: 'leave.apply_attendance',
    entity: 'leave_request',
    entityId: leave.id,
    meta: { sessionsInRange: sessions.length, excused: applied },
  });
  return applied;
}

export function serializeLeave(row: LeaveRow, extra: Record<string, unknown> = {}) {
  return {
    id: row.id,
    studentId: row.student_id,
    classId: row.class_id,
    type: row.type,
    startDate: row.start_date,
    endDate: row.end_date,
    reason: row.reason,
    attachmentUrl: row.attachment_url,
    status: row.status,
    reviewerId: row.reviewer_id,
    reviewNote: row.review_note,
    reviewedAt: row.reviewed_at,
    createdAt: row.created_at,
    updatedAt: row.updated_at,
    ...extra,
  };
}
