import { Router } from 'express';
import { z } from 'zod';
import { config } from '../config.js';
import { audit, getDb, newId, nowIso } from '../lib/db.js';
import { ApiError } from '../lib/errors.js';
import { assertCanManageSession, getSessionOrThrow, isEnrolled, ownsClass } from '../lib/access.js';
import { closeSessionAttendance, serializeAttendance } from '../lib/attendance.js';
import { issueSessionQr } from '../lib/qr.js';
import { currentUser, requireAuth, requireRole } from '../middleware/auth.js';
import type { AttendanceStatus, SessionRow } from '../lib/types.js';

export const classesRouter = Router();
classesRouter.use(requireAuth);

export function serializeSession(s: SessionRow, extra: Record<string, unknown> = {}) {
  return {
    id: s.id,
    classId: s.class_id,
    title: s.title,
    room: s.room,
    startsAt: s.starts_at,
    endsAt: s.ends_at,
    lateAfterMin: s.late_after_min,
    checkinState: s.checkin_state,
    openedAt: s.opened_at,
    closedAt: s.closed_at,
    ...extra,
  };
}

/** Danh sách lớp của người dùng hiện tại (giảng viên: lớp phụ trách, sinh viên: lớp đã đăng ký). */
classesRouter.get('/classes', (req, res) => {
  const user = currentUser(req);
  const db = getDb();
  const rows = db
    .prepare(
      user.role === 'student'
        ? `SELECT c.*, u.full_name AS lecturer_name,
                  (SELECT COUNT(*) FROM enrollments e2 WHERE e2.class_id = c.id) AS student_count
             FROM enrollments e JOIN classes c ON c.id = e.class_id JOIN users u ON u.id = c.lecturer_id
            WHERE e.student_id = ? ORDER BY c.code`
        : user.role === 'admin'
          ? `SELECT c.*, u.full_name AS lecturer_name,
                    (SELECT COUNT(*) FROM enrollments e2 WHERE e2.class_id = c.id) AS student_count
               FROM classes c JOIN users u ON u.id = c.lecturer_id ORDER BY c.code`
          : `SELECT c.*, u.full_name AS lecturer_name,
                    (SELECT COUNT(*) FROM enrollments e2 WHERE e2.class_id = c.id) AS student_count
               FROM classes c JOIN users u ON u.id = c.lecturer_id
              WHERE c.lecturer_id = ? ORDER BY c.code`,
    )
    .all(...(user.role === 'admin' ? [] : [user.id])) as Array<Record<string, any>>;

  res.json({
    items: rows.map((c) => ({
      id: c.id,
      code: c.code,
      name: c.name,
      term: c.term,
      room: c.room,
      lecturerId: c.lecturer_id,
      lecturerName: c.lecturer_name,
      studentCount: c.student_count,
    })),
  });
});

/** Buổi học của một lớp. */
classesRouter.get('/classes/:classId/sessions', (req, res) => {
  const user = currentUser(req);
  const db = getDb();
  const classId = req.params.classId as string;

  if (!ownsClass(db, classId, user) && !isEnrolled(db, classId, user.id)) {
    throw ApiError.forbidden('CLASS_FORBIDDEN', 'Bạn không có quyền xem lớp học phần này');
  }

  const rows = db
    .prepare(`SELECT * FROM class_sessions WHERE class_id = ? ORDER BY starts_at DESC`)
    .all(classId) as SessionRow[];

  // Sinh viên thấy kèm trạng thái điểm danh của chính mình.
  const myStatus = new Map<string, AttendanceStatus>();
  if (user.role === 'student') {
    const mine = db
      .prepare(
        `SELECT a.session_id, a.status FROM attendance_records a
           JOIN class_sessions s ON s.id = a.session_id
          WHERE s.class_id = ? AND a.student_id = ?`,
      )
      .all(classId, user.id) as Array<{ session_id: string; status: AttendanceStatus }>;
    for (const r of mine) myStatus.set(r.session_id, r.status);
  }

  res.json({
    items: rows.map((s) =>
      serializeSession(s, user.role === 'student' ? { myStatus: myStatus.get(s.id) ?? null } : {}),
    ),
  });
});

/** Các buổi học đang mở điểm danh mà người dùng có liên quan — màn hình chính của app. */
classesRouter.get('/sessions/open', (req, res) => {
  const user = currentUser(req);
  const db = getDb();
  const rows = db
    .prepare(
      user.role === 'student'
        ? `SELECT s.*, c.code AS class_code, c.name AS class_name
             FROM class_sessions s JOIN classes c ON c.id = s.class_id
             JOIN enrollments e ON e.class_id = c.id AND e.student_id = ?
            WHERE s.checkin_state = 'open' ORDER BY s.starts_at`
        : user.role === 'admin'
          ? `SELECT s.*, c.code AS class_code, c.name AS class_name
               FROM class_sessions s JOIN classes c ON c.id = s.class_id
              WHERE s.checkin_state = 'open' ORDER BY s.starts_at`
          : `SELECT s.*, c.code AS class_code, c.name AS class_name
               FROM class_sessions s JOIN classes c ON c.id = s.class_id
              WHERE s.checkin_state = 'open' AND c.lecturer_id = ? ORDER BY s.starts_at`,
    )
    .all(...(user.role === 'admin' ? [] : [user.id])) as Array<SessionRow & { class_code: string; class_name: string }>;

  res.json({
    items: rows.map((s) => serializeSession(s, { classCode: s.class_code, className: s.class_name })),
  });
});

const createSessionBody = z.object({
  classId: z.string().min(1),
  title: z.string().trim().min(1).max(200),
  room: z.string().trim().max(60).optional(),
  startsAt: z.iso.datetime({ offset: true }),
  endsAt: z.iso.datetime({ offset: true }),
  lateAfterMin: z.number().int().min(0).max(240).default(15),
});

classesRouter.post('/sessions', requireRole('lecturer', 'admin'), (req, res) => {
  const user = currentUser(req);
  const db = getDb();
  const body = createSessionBody.parse(req.body);

  if (!ownsClass(db, body.classId, user)) {
    throw ApiError.forbidden('NOT_CLASS_OWNER', 'Bạn không phụ trách lớp học phần này');
  }
  if (new Date(body.endsAt) <= new Date(body.startsAt)) {
    throw ApiError.badRequest('TIME_RANGE_INVALID', 'Giờ kết thúc phải sau giờ bắt đầu');
  }

  const id = newId('ses');
  db.prepare(
    `INSERT INTO class_sessions (id, class_id, title, room, starts_at, ends_at, late_after_min, created_at)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
  ).run(id, body.classId, body.title, body.room ?? null, body.startsAt, body.endsAt, body.lateAfterMin, nowIso());

  audit(db, { actorId: user.id, action: 'session.create', entity: 'session', entityId: id });
  res.status(201).json({ session: serializeSession(getSessionOrThrow(db, id)) });
});

classesRouter.post('/sessions/:sessionId/open', requireRole('lecturer', 'admin'), (req, res) => {
  const user = currentUser(req);
  const db = getDb();
  const session = getSessionOrThrow(db, req.params.sessionId as string);
  assertCanManageSession(db, session, user);

  db.prepare(`UPDATE class_sessions SET checkin_state = 'open', opened_at = ?, closed_at = NULL WHERE id = ?`).run(
    nowIso(),
    session.id,
  );
  audit(db, { actorId: user.id, action: 'session.open', entity: 'session', entityId: session.id });
  res.json({ session: serializeSession(getSessionOrThrow(db, session.id)) });
});

classesRouter.post('/sessions/:sessionId/close', requireRole('lecturer', 'admin'), (req, res) => {
  const user = currentUser(req);
  const db = getDb();
  const session = getSessionOrThrow(db, req.params.sessionId as string);
  assertCanManageSession(db, session, user);

  const markedAbsent = db.transaction(() => closeSessionAttendance(db, session, user.id))();
  res.json({ session: serializeSession(getSessionOrThrow(db, session.id)), markedAbsent });
});

/**
 * Cấp mã QR của buổi học để giảng viên chiếu lên màn hình.
 * Mã có hạn rất ngắn, app phải gọi lại trước khi hết hạn (xoay vòng).
 */
classesRouter.get('/sessions/:sessionId/qr', requireRole('lecturer', 'admin'), (req, res) => {
  const user = currentUser(req);
  const db = getDb();
  const session = getSessionOrThrow(db, req.params.sessionId as string);
  assertCanManageSession(db, session, user);

  if (session.checkin_state !== 'open') {
    throw ApiError.conflict('SESSION_CLOSED', 'Hãy mở điểm danh trước khi lấy mã QR', { sessionId: session.id });
  }

  const { token, payload } = issueSessionQr(session.id);
  res.json({
    token,
    expiresAt: new Date(payload.exp * 1000).toISOString(),
    ttlSec: config.sessionQrTtlSec,
    // Gợi ý cho app: nên xin mã mới sau bao nhiêu giây để không bao giờ hiện mã hết hạn.
    refreshAfterSec: Math.max(5, Math.floor(config.sessionQrTtlSec * 0.6)),
  });
});

/** Bảng điểm danh của một buổi học — màn hình theo dõi trực tiếp của giảng viên. */
classesRouter.get('/sessions/:sessionId/attendance', (req, res) => {
  const user = currentUser(req);
  const db = getDb();
  const session = getSessionOrThrow(db, req.params.sessionId as string);

  if (user.role === 'student') {
    if (!isEnrolled(db, session.class_id, user.id)) {
      throw ApiError.forbidden('NOT_ENROLLED', 'Bạn không thuộc lớp học phần này');
    }
    const mine = db
      .prepare(`SELECT * FROM attendance_records WHERE session_id = ? AND student_id = ?`)
      .get(session.id, user.id);
    res.json({
      session: serializeSession(session),
      items: mine ? [serializeAttendance(mine as any)] : [],
      summary: null,
    });
    return;
  }

  assertCanManageSession(db, session, user);

  const rows = db
    .prepare(
      `SELECT u.id AS student_id, u.code, u.full_name, a.id AS record_id, a.status, a.method,
              a.checked_in_at, a.note
         FROM enrollments e
         JOIN users u ON u.id = e.student_id
         LEFT JOIN attendance_records a ON a.session_id = ? AND a.student_id = u.id
        WHERE e.class_id = ?
        ORDER BY u.code`,
    )
    .all(session.id, session.class_id) as Array<Record<string, any>>;

  const summary = { total: rows.length, present: 0, late: 0, excused: 0, absent: 0, pending: 0 };
  for (const r of rows) {
    if (r.status === 'present') summary.present += 1;
    else if (r.status === 'late') summary.late += 1;
    else if (r.status === 'excused') summary.excused += 1;
    else if (r.status === 'absent') summary.absent += 1;
    else summary.pending += 1;
  }

  res.json({
    session: serializeSession(session),
    summary,
    items: rows.map((r) => ({
      studentId: r.student_id,
      studentCode: r.code,
      fullName: r.full_name,
      recordId: r.record_id,
      status: (r.status ?? null) as AttendanceStatus | null,
      method: r.method,
      checkedInAt: r.checked_in_at,
      note: r.note,
    })),
  });
});

const manualMarkBody = z.object({
  studentId: z.string().min(1),
  status: z.enum(['present', 'late', 'absent', 'excused']),
  note: z.string().trim().max(300).optional(),
});

/** Điểm danh thủ công: dự phòng khi điện thoại sinh viên hỏng hoặc camera không quét được. */
classesRouter.post('/sessions/:sessionId/attendance', requireRole('lecturer', 'admin'), (req, res) => {
  const user = currentUser(req);
  const db = getDb();
  const session = getSessionOrThrow(db, req.params.sessionId as string);
  assertCanManageSession(db, session, user);
  const body = manualMarkBody.parse(req.body);

  if (!isEnrolled(db, session.class_id, body.studentId)) {
    throw ApiError.forbidden('NOT_ENROLLED', 'Sinh viên không thuộc lớp học phần này');
  }

  const now = nowIso();
  const checkedInAt = body.status === 'present' || body.status === 'late' ? now : null;
  db.prepare(
    `INSERT INTO attendance_records
       (id, session_id, student_id, status, method, checked_in_at, recorded_by, note, created_at, updated_at)
     VALUES (?, ?, ?, ?, 'manual', ?, ?, ?, ?, ?)
     ON CONFLICT (session_id, student_id) DO UPDATE SET
       status = excluded.status, method = 'manual', checked_in_at = excluded.checked_in_at,
       recorded_by = excluded.recorded_by, note = excluded.note, updated_at = excluded.updated_at`,
  ).run(newId('att'), session.id, body.studentId, body.status, checkedInAt, user.id, body.note ?? null, now, now);

  const record = db
    .prepare(`SELECT * FROM attendance_records WHERE session_id = ? AND student_id = ?`)
    .get(session.id, body.studentId);
  audit(db, {
    actorId: user.id,
    action: 'attendance.manual',
    entity: 'attendance',
    entityId: (record as any).id,
    meta: { studentId: body.studentId, status: body.status },
  });
  res.json({ record: serializeAttendance(record as any) });
});
