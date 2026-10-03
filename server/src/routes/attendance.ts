import { Router } from 'express';
import { z } from 'zod';
import { config } from '../config.js';
import { getDb } from '../lib/db.js';
import { ApiError } from '../lib/errors.js';
import { assertCanManageSession, assertCanViewStudent, getSessionOrThrow } from '../lib/access.js';
import { findByClientUuid, recordCheckIn, serializeAttendance } from '../lib/attendance.js';
import { consumeNonce, issueStudentQr, verifyQr } from '../lib/qr.js';
import { currentUser, requireAuth } from '../middleware/auth.js';
import type { AttendanceRow, UserRow } from '../lib/types.js';

export const attendanceRouter = Router();
attendanceRouter.use(requireAuth);

/**
 * Mã QR cá nhân của sinh viên — giảng viên quét mã này để điểm danh.
 * Mã xoay vòng theo STUDENT_QR_TTL_SEC nên ảnh chụp màn hình nhanh chóng vô dụng.
 */
attendanceRouter.get('/me/qr', (req, res) => {
  const user = currentUser(req);
  if (user.role !== 'student') {
    throw ApiError.forbidden('STUDENT_ONLY', 'Chỉ sinh viên mới có mã QR cá nhân');
  }
  const { token, payload } = issueStudentQr(user.id);
  res.json({
    token,
    studentCode: user.code,
    fullName: user.full_name,
    expiresAt: new Date(payload.exp * 1000).toISOString(),
    ttlSec: config.studentQrTtlSec,
    refreshAfterSec: Math.max(5, Math.floor(config.studentQrTtlSec * 0.6)),
  });
});

const checkInBody = z.object({
  /** Chuỗi đọc được từ mã QR, nguyên văn. */
  qr: z.string().min(1, 'Thiếu nội dung mã QR'),
  /** Bắt buộc khi giảng viên quét mã sinh viên: cho biết đang điểm danh buổi nào. */
  sessionId: z.string().min(1).optional(),
  /** UUID do app sinh cho mỗi lượt quét — để gửi lại an toàn sau khi mất mạng. */
  clientUuid: z.string().trim().min(8).max(64).optional(),
  deviceId: z.string().trim().max(128).optional(),
  /** Giờ quét thực tế trên máy, dùng khi đồng bộ bản ghi offline. */
  scannedAt: z.iso.datetime({ offset: true }).optional(),
});
type CheckInBody = z.infer<typeof checkInBody>;

interface CheckInOutcome {
  record: AttendanceRow;
  duplicate: boolean;
  student: { id: string; code: string; fullName: string };
  sessionId: string;
}

/** Dựng lại phần mô tả kèm theo một bản ghi điểm danh đã có. */
function describeRecord(record: AttendanceRow): Omit<CheckInOutcome, 'duplicate'> {
  const student = getDb().prepare(`SELECT id, code, full_name FROM users WHERE id = ?`).get(record.student_id) as {
    id: string;
    code: string;
    full_name: string;
  };
  return {
    record,
    student: { id: student.id, code: student.code, fullName: student.full_name },
    sessionId: record.session_id,
  };
}

/**
 * Xử lý một lượt quét, dùng chung cho cả quét trực tiếp lẫn đồng bộ offline.
 * Tự nhận biết loại mã để chọn đúng chiều điểm danh.
 */
function processScan(body: CheckInBody, actor: UserRow, now = Date.now()): CheckInOutcome {
  const db = getDb();

  // Kiểm tra trùng theo clientUuid TRƯỚC mọi thứ khác. Một lượt quét đã ghi nhận
  // thành công nhưng mất phản hồi mạng sẽ được app gửi lại với đúng UUID cũ; khi đó
  // mã QR kèm theo đã hết hạn và nonce đã bị tiêu thụ, nên nếu xác thực QR trước thì
  // lần gửi lại sẽ bị từ chối oan.
  if (body.clientUuid) {
    const existing = findByClientUuid(db, body.clientUuid);
    if (existing) return { ...describeRecord(existing), duplicate: true };
  }

  const payload = verifyQr(body.qr, now);

  let studentId: string;
  let sessionId: string;
  let method: 'qr_session' | 'qr_student';

  if (payload.t === 'S') {
    // Sinh viên quét mã chiếu trên lớp.
    if (actor.role !== 'student') {
      throw ApiError.forbidden('SESSION_QR_STUDENT_ONLY', 'Mã buổi học chỉ dành cho sinh viên quét');
    }
    studentId = actor.id;
    sessionId = payload.sid;
    method = 'qr_session';
  } else {
    // Giảng viên quét mã cá nhân của sinh viên.
    if (actor.role === 'student') {
      throw ApiError.forbidden('STUDENT_QR_STAFF_ONLY', 'Chỉ giảng viên mới quét được mã sinh viên');
    }
    if (!body.sessionId) {
      throw ApiError.badRequest('SESSION_ID_REQUIRED', 'Cần chọn buổi học trước khi quét mã sinh viên');
    }
    studentId = payload.uid;
    sessionId = body.sessionId;
    method = 'qr_student';
  }

  const session = getSessionOrThrow(db, sessionId);
  if (method === 'qr_student') assertCanManageSession(db, session, actor);

  // Nonce gắn với cặp (mã QR, người tiêu thụ): chặn dùng lại cùng một ảnh chụp.
  if (!consumeNonce(db, payload.n, `${studentId}:${sessionId}`, payload.exp)) {
    throw ApiError.conflict('QR_ALREADY_USED', 'Mã QR này đã được dùng, vui lòng quét mã mới nhất');
  }

  const result = recordCheckIn(db, {
    session,
    studentId,
    method,
    recordedBy: actor.id,
    deviceId: body.deviceId ?? null,
    clientUuid: body.clientUuid ?? null,
    scannedAt: body.scannedAt ?? null,
  });

  return { ...describeRecord(result.record), duplicate: result.duplicate };
}

/** Điểm danh bằng một lượt quét. */
attendanceRouter.post('/attendance/check-in', (req, res) => {
  const actor = currentUser(req);
  const outcome = processScan(checkInBody.parse(req.body), actor);
  res.status(outcome.duplicate ? 200 : 201).json({
    duplicate: outcome.duplicate,
    record: serializeAttendance(outcome.record),
    student: outcome.student,
    sessionId: outcome.sessionId,
  });
});

const syncBody = z.object({
  items: z.array(checkInBody.extend({ clientUuid: z.string().trim().min(8).max(64) })).min(1).max(200),
});

/**
 * Đồng bộ hàng đợi offline.
 * Mỗi phần tử được xử lý độc lập: một lượt hỏng không làm hỏng cả lô, và
 * `clientUuid` đảm bảo gửi lại nhiều lần vẫn chỉ ghi một bản ghi.
 */
attendanceRouter.post('/attendance/sync', (req, res) => {
  const actor = currentUser(req);
  const { items } = syncBody.parse(req.body);

  const results = items.map((item) => {
    try {
      const outcome = processScan(item, actor);
      return {
        clientUuid: item.clientUuid,
        ok: true as const,
        duplicate: outcome.duplicate,
        record: serializeAttendance(outcome.record),
        student: outcome.student,
      };
    } catch (err) {
      if (err instanceof ApiError) {
        return {
          clientUuid: item.clientUuid,
          ok: false as const,
          // Lỗi 4xx là vĩnh viễn — app nên bỏ khỏi hàng đợi thay vì thử lại mãi.
          retryable: err.status >= 500,
          error: { code: err.code, message: err.message },
        };
      }
      return {
        clientUuid: item.clientUuid,
        ok: false as const,
        retryable: true,
        error: { code: 'INTERNAL_ERROR', message: 'Lỗi hệ thống khi đồng bộ' },
      };
    }
  });

  res.json({
    accepted: results.filter((r) => r.ok).length,
    rejected: results.filter((r) => !r.ok).length,
    results,
  });
});

const historyQuery = z.object({
  studentId: z.string().min(1).optional(),
  classId: z.string().min(1).optional(),
  from: z.iso.date().optional(),
  to: z.iso.date().optional(),
  limit: z.coerce.number().int().min(1).max(200).default(50),
  offset: z.coerce.number().int().min(0).default(0),
});

/** Lịch sử điểm danh của một sinh viên, kèm thống kê nhanh. */
attendanceRouter.get('/attendance/history', (req, res) => {
  const actor = currentUser(req);
  const q = historyQuery.parse(req.query);
  const db = getDb();

  const studentId = q.studentId ?? actor.id;
  if (actor.role === 'student' && studentId !== actor.id) {
    throw ApiError.forbidden('STUDENT_FORBIDDEN', 'Bạn chỉ xem được lịch sử của chính mình');
  }
  assertCanViewStudent(db, studentId, actor);

  const where: string[] = ['a.student_id = ?'];
  const params: unknown[] = [studentId];
  if (q.classId) {
    where.push('s.class_id = ?');
    params.push(q.classId);
  }
  if (q.from) {
    where.push('date(s.starts_at) >= date(?)');
    params.push(q.from);
  }
  if (q.to) {
    where.push('date(s.starts_at) <= date(?)');
    params.push(q.to);
  }
  const whereSql = where.join(' AND ');

  const rows = db
    .prepare(
      `SELECT a.*, s.title, s.starts_at, s.ends_at, s.room, c.code AS class_code, c.name AS class_name
         FROM attendance_records a
         JOIN class_sessions s ON s.id = a.session_id
         JOIN classes c ON c.id = s.class_id
        WHERE ${whereSql}
        ORDER BY s.starts_at DESC
        LIMIT ? OFFSET ?`,
    )
    .all(...params, q.limit, q.offset) as Array<Record<string, any>>;

  const stats = db
    .prepare(
      `SELECT a.status, COUNT(*) AS n
         FROM attendance_records a
         JOIN class_sessions s ON s.id = a.session_id
        WHERE ${whereSql}
        GROUP BY a.status`,
    )
    .all(...params) as Array<{ status: string; n: number }>;

  const summary = { present: 0, late: 0, absent: 0, excused: 0, total: 0 };
  for (const s of stats) {
    summary[s.status as keyof typeof summary] = s.n;
    summary.total += s.n;
  }

  res.json({
    studentId,
    summary,
    items: rows.map((r) => ({
      ...serializeAttendance(r as AttendanceRow),
      session: {
        id: r.session_id,
        title: r.title,
        startsAt: r.starts_at,
        endsAt: r.ends_at,
        room: r.room,
        classCode: r.class_code,
        className: r.class_name,
      },
    })),
    paging: { limit: q.limit, offset: q.offset, count: rows.length },
  });
});
