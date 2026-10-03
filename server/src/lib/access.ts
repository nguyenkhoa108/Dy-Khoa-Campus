import { ApiError } from './errors.js';
import type { DB } from './db.js';
import type { SessionRow, UserRow } from './types.js';

export function getSessionOrThrow(db: DB, sessionId: string): SessionRow {
  const row = db.prepare(`SELECT * FROM class_sessions WHERE id = ?`).get(sessionId) as SessionRow | undefined;
  if (!row) throw ApiError.notFound('SESSION_NOT_FOUND', 'Không tìm thấy buổi học');
  return row;
}

export function isEnrolled(db: DB, classId: string, studentId: string): boolean {
  return (
    db.prepare(`SELECT 1 FROM enrollments WHERE class_id = ? AND student_id = ?`).get(classId, studentId) !== undefined
  );
}

export function ownsClass(db: DB, classId: string, user: UserRow): boolean {
  if (user.role === 'admin') return true;
  return db.prepare(`SELECT 1 FROM classes WHERE id = ? AND lecturer_id = ?`).get(classId, user.id) !== undefined;
}

/** Giảng viên phụ trách lớp hoặc quản trị viên mới được quản lý buổi học. */
export function assertCanManageSession(db: DB, session: SessionRow, user: UserRow): void {
  if (!ownsClass(db, session.class_id, user)) {
    throw ApiError.forbidden('NOT_CLASS_OWNER', 'Bạn không phụ trách lớp học phần này');
  }
}

/** Quyền xem dữ liệu của một sinh viên: chính sinh viên đó, giảng viên dạy họ, hoặc quản trị. */
export function assertCanViewStudent(db: DB, studentId: string, user: UserRow): void {
  if (user.role === 'admin' || user.id === studentId) return;
  if (user.role === 'lecturer') {
    const shared = db
      .prepare(
        `SELECT 1 FROM enrollments e JOIN classes c ON c.id = e.class_id
          WHERE e.student_id = ? AND c.lecturer_id = ? LIMIT 1`,
      )
      .get(studentId, user.id);
    if (shared) return;
  }
  throw ApiError.forbidden('STUDENT_FORBIDDEN', 'Bạn không có quyền xem dữ liệu của sinh viên này');
}
