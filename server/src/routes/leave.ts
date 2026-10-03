import { Router } from 'express';
import { z } from 'zod';
import { audit, getDb, newId, nowIso } from '../lib/db.js';
import { ApiError } from '../lib/errors.js';
import { isEnrolled, ownsClass } from '../lib/access.js';
import { applyApprovedLeave, serializeLeave } from '../lib/leave.js';
import { currentUser, requireAuth, requireRole } from '../middleware/auth.js';
import type { LeaveRow, UserRow } from '../lib/types.js';

export const leaveRouter = Router();
leaveRouter.use(requireAuth);

const LEAVE_JOIN = `
  FROM leave_requests l
  JOIN users u ON u.id = l.student_id
  LEFT JOIN classes c ON c.id = l.class_id
  LEFT JOIN users r ON r.id = l.reviewer_id`;

const LEAVE_COLUMNS = `
  l.*, u.code AS student_code, u.full_name AS student_name, u.avatar_url AS student_avatar,
  c.code AS class_code, c.name AS class_name, r.full_name AS reviewer_name`;

function decorate(row: Record<string, any>) {
  return serializeLeave(row as LeaveRow, {
    student: { id: row.student_id, code: row.student_code, fullName: row.student_name, avatarUrl: row.student_avatar },
    class: row.class_id ? { id: row.class_id, code: row.class_code, name: row.class_name } : null,
    reviewerName: row.reviewer_name ?? null,
  });
}

function loadLeave(id: string): Record<string, any> {
  const row = getDb().prepare(`SELECT ${LEAVE_COLUMNS} ${LEAVE_JOIN} WHERE l.id = ?`).get(id) as
    | Record<string, any>
    | undefined;
  if (!row) throw ApiError.notFound('LEAVE_NOT_FOUND', 'Không tìm thấy đơn xin phép');
  return row;
}

/**
 * Ai được duyệt đơn:
 *  - Đơn gắn với một lớp  → giảng viên phụ trách lớp đó, hoặc quản trị viên.
 *  - Đơn xin nghỉ mọi lớp → chỉ quản trị viên (không giảng viên nào bao quát hết).
 */
function assertCanReview(leave: LeaveRow, user: UserRow): void {
  if (user.role === 'admin') return;
  if (user.role !== 'lecturer') {
    throw ApiError.forbidden('REVIEW_FORBIDDEN', 'Bạn không có quyền duyệt đơn');
  }
  if (!leave.class_id) {
    throw ApiError.forbidden('REVIEW_NEEDS_ADMIN', 'Đơn xin nghỉ toàn bộ lớp phải do quản trị viên duyệt');
  }
  if (!ownsClass(getDb(), leave.class_id, user)) {
    throw ApiError.forbidden('NOT_CLASS_OWNER', 'Bạn không phụ trách lớp học phần của đơn này');
  }
}

const createBody = z.object({
  classId: z.string().min(1).nullish(),
  type: z.enum(['sick', 'personal', 'family', 'other']),
  startDate: z.iso.date(),
  endDate: z.iso.date(),
  reason: z.string().trim().min(5, 'Lý do tối thiểu 5 ký tự').max(1000),
  attachmentUrl: z.string().url().max(500).nullish(),
});

/** Sinh viên nộp đơn xin phép. */
leaveRouter.post('/leave-requests', requireRole('student'), (req, res) => {
  const user = currentUser(req);
  const db = getDb();
  const body = createBody.parse(req.body);

  if (body.endDate < body.startDate) {
    throw ApiError.badRequest('DATE_RANGE_INVALID', 'Ngày kết thúc phải sau hoặc bằng ngày bắt đầu');
  }
  if (body.classId && !isEnrolled(db, body.classId, user.id)) {
    throw ApiError.forbidden('NOT_ENROLLED', 'Bạn không đăng ký lớp học phần này');
  }

  // Chặn nộp trùng: đã có đơn chờ duyệt phủ lên cùng khoảng ngày và cùng phạm vi lớp.
  const overlapping = db
    .prepare(
      `SELECT id FROM leave_requests
        WHERE student_id = ? AND status = 'pending'
          AND (class_id IS ? OR class_id IS NULL OR ? IS NULL)
          AND date(start_date) <= date(?) AND date(end_date) >= date(?)`,
    )
    .get(user.id, body.classId ?? null, body.classId ?? null, body.endDate, body.startDate) as
    | { id: string }
    | undefined;
  if (overlapping) {
    throw ApiError.conflict('LEAVE_OVERLAPPING', 'Bạn đã có đơn chờ duyệt trùng khoảng thời gian này', {
      leaveRequestId: overlapping.id,
    });
  }

  const id = newId('lv');
  const now = nowIso();
  db.prepare(
    `INSERT INTO leave_requests
       (id, student_id, class_id, type, start_date, end_date, reason, attachment_url, status, created_at, updated_at)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?, ?)`,
  ).run(
    id,
    user.id,
    body.classId ?? null,
    body.type,
    body.startDate,
    body.endDate,
    body.reason,
    body.attachmentUrl ?? null,
    now,
    now,
  );

  audit(db, { actorId: user.id, action: 'leave.create', entity: 'leave_request', entityId: id });
  res.status(201).json({ leaveRequest: decorate(loadLeave(id)) });
});

const listQuery = z.object({
  status: z.enum(['pending', 'approved', 'rejected', 'cancelled']).optional(),
  classId: z.string().min(1).optional(),
  studentId: z.string().min(1).optional(),
  scope: z.enum(['mine', 'to-review']).optional(),
  limit: z.coerce.number().int().min(1).max(100).default(30),
  offset: z.coerce.number().int().min(0).default(0),
});

/**
 * Danh sách đơn.
 *  - Sinh viên: luôn chỉ thấy đơn của chính mình.
 *  - Giảng viên: mặc định thấy đơn thuộc các lớp mình phụ trách (hộp duyệt).
 *  - Quản trị: thấy tất cả.
 */
leaveRouter.get('/leave-requests', (req, res) => {
  const user = currentUser(req);
  const db = getDb();
  const q = listQuery.parse(req.query);

  const where: string[] = [];
  const params: unknown[] = [];

  if (user.role === 'student' || q.scope === 'mine') {
    where.push('l.student_id = ?');
    params.push(user.id);
  } else if (user.role === 'lecturer') {
    where.push('l.class_id IN (SELECT id FROM classes WHERE lecturer_id = ?)');
    params.push(user.id);
  }

  if (q.status) {
    where.push('l.status = ?');
    params.push(q.status);
  }
  if (q.classId) {
    where.push('l.class_id = ?');
    params.push(q.classId);
  }
  if (q.studentId) {
    if (user.role === 'student' && q.studentId !== user.id) {
      throw ApiError.forbidden('STUDENT_FORBIDDEN', 'Bạn chỉ xem được đơn của chính mình');
    }
    where.push('l.student_id = ?');
    params.push(q.studentId);
  }

  const whereSql = where.length ? `WHERE ${where.join(' AND ')}` : '';
  const rows = db
    .prepare(
      `SELECT ${LEAVE_COLUMNS} ${LEAVE_JOIN} ${whereSql}
        ORDER BY CASE l.status WHEN 'pending' THEN 0 ELSE 1 END, l.created_at DESC
        LIMIT ? OFFSET ?`,
    )
    .all(...params, q.limit, q.offset) as Array<Record<string, any>>;

  const total = (
    db.prepare(`SELECT COUNT(*) AS n ${LEAVE_JOIN} ${whereSql}`).get(...params) as { n: number }
  ).n;

  res.json({ items: rows.map(decorate), paging: { limit: q.limit, offset: q.offset, total } });
});

/** Số đơn đang chờ duyệt — dùng cho chấm đỏ trên tab của giảng viên. */
leaveRouter.get('/leave-requests/pending-count', requireRole('lecturer', 'admin'), (req, res) => {
  const user = currentUser(req);
  const db = getDb();
  const row =
    user.role === 'admin'
      ? (db.prepare(`SELECT COUNT(*) AS n FROM leave_requests WHERE status = 'pending'`).get() as { n: number })
      : (db
          .prepare(
            `SELECT COUNT(*) AS n FROM leave_requests
              WHERE status = 'pending' AND class_id IN (SELECT id FROM classes WHERE lecturer_id = ?)`,
          )
          .get(user.id) as { n: number });
  res.json({ pending: row.n });
});

leaveRouter.get('/leave-requests/:id', (req, res) => {
  const user = currentUser(req);
  const row = loadLeave(req.params.id as string);
  if (user.role === 'student' && row.student_id !== user.id) {
    throw ApiError.forbidden('LEAVE_FORBIDDEN', 'Bạn không có quyền xem đơn này');
  }
  if (user.role === 'lecturer' && row.student_id !== user.id) {
    // Giảng viên chỉ xem được đơn thuộc lớp mình phụ trách.
    if (!row.class_id || !ownsClass(getDb(), row.class_id, user)) {
      throw ApiError.forbidden('LEAVE_FORBIDDEN', 'Bạn không có quyền xem đơn này');
    }
  }
  res.json({ leaveRequest: decorate(row) });
});

const decisionBody = z.object({ note: z.string().trim().max(500).optional() });

function decide(id: string, user: UserRow, status: 'approved' | 'rejected', note: string | null) {
  const db = getDb();
  const leave = loadLeave(id) as LeaveRow & Record<string, any>;
  assertCanReview(leave, user);

  if (leave.status !== 'pending') {
    throw ApiError.conflict('LEAVE_NOT_PENDING', `Đơn đã ở trạng thái "${leave.status}", không thể duyệt lại`);
  }

  const now = nowIso();
  let excusedSessions = 0;

  db.transaction(() => {
    db.prepare(
      `UPDATE leave_requests SET status = ?, reviewer_id = ?, review_note = ?, reviewed_at = ?, updated_at = ?
        WHERE id = ? AND status = 'pending'`,
    ).run(status, user.id, note, now, now, id);

    if (status === 'approved') {
      excusedSessions = applyApprovedLeave(db, { ...leave, status: 'approved' }, user.id);
    }
    audit(db, {
      actorId: user.id,
      action: `leave.${status}`,
      entity: 'leave_request',
      entityId: id,
      meta: { note, excusedSessions },
    });
  })();

  return { leaveRequest: decorate(loadLeave(id)), excusedSessions };
}

/** Phê duyệt đơn: đồng thời đánh dấu "nghỉ có phép" cho các buổi học trong khoảng ngày. */
leaveRouter.post('/leave-requests/:id/approve', requireRole('lecturer', 'admin'), (req, res) => {
  const { note } = decisionBody.parse(req.body ?? {});
  res.json(decide(req.params.id as string, currentUser(req), 'approved', note ?? null));
});

const rejectBody = z.object({ note: z.string().trim().min(3, 'Nhập lý do từ chối').max(500) });

leaveRouter.post('/leave-requests/:id/reject', requireRole('lecturer', 'admin'), (req, res) => {
  const { note } = rejectBody.parse(req.body ?? {});
  res.json(decide(req.params.id as string, currentUser(req), 'rejected', note));
});

/** Sinh viên tự rút đơn khi chưa ai duyệt. */
leaveRouter.post('/leave-requests/:id/cancel', requireRole('student'), (req, res) => {
  const user = currentUser(req);
  const db = getDb();
  const leave = loadLeave(req.params.id as string);

  if (leave.student_id !== user.id) throw ApiError.forbidden('LEAVE_FORBIDDEN', 'Đây không phải đơn của bạn');
  if (leave.status !== 'pending') {
    throw ApiError.conflict('LEAVE_NOT_PENDING', 'Chỉ rút được đơn đang chờ duyệt');
  }

  db.prepare(`UPDATE leave_requests SET status = 'cancelled', updated_at = ? WHERE id = ?`).run(nowIso(), leave.id);
  audit(db, { actorId: user.id, action: 'leave.cancel', entity: 'leave_request', entityId: leave.id });
  res.json({ leaveRequest: decorate(loadLeave(leave.id)) });
});
