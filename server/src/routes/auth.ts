import { Router } from 'express';
import bcrypt from 'bcryptjs';
import { z } from 'zod';
import { config } from '../config.js';
import { getDb, audit } from '../lib/db.js';
import { ApiError } from '../lib/errors.js';
import { issueRefreshToken, revokeRefreshToken, rotateRefreshToken, signAccessToken } from '../lib/tokens.js';
import { requireAuth, currentUser } from '../middleware/auth.js';
import { publicUser, type UserRow } from '../lib/types.js';

export const authRouter = Router();

const loginBody = z.object({
  // Chấp nhận email hoặc MSSV / mã giảng viên
  identifier: z.string().trim().min(1, 'Nhập email hoặc mã số'),
  password: z.string().min(1, 'Nhập mật khẩu'),
  deviceId: z.string().trim().max(128).optional(),
});

function tokenPair(user: UserRow, deviceId: string | null) {
  const db = getDb();
  const accessToken = signAccessToken({ sub: user.id, role: user.role, code: user.code, name: user.full_name });
  const refresh = issueRefreshToken(db, user.id, deviceId);
  return {
    accessToken,
    refreshToken: refresh.token,
    tokenType: 'Bearer' as const,
    expiresIn: config.accessTokenTtlSec,
    refreshExpiresAt: new Date(refresh.expiresAt * 1000).toISOString(),
    user: publicUser(user),
  };
}

authRouter.post('/login', (req, res) => {
  const { identifier, password, deviceId } = loginBody.parse(req.body);
  const db = getDb();

  const user = db
    .prepare(`SELECT * FROM users WHERE lower(email) = lower(?) OR lower(code) = lower(?)`)
    .get(identifier, identifier) as UserRow | undefined;

  // So sánh cả khi không có người dùng để thời gian phản hồi không lộ email tồn tại hay không.
  const hash = user?.password_hash ?? '$2b$10$invalidinvalidinvalidinvalidinvalidinvalidinvalidinvalidinv';
  const ok = bcrypt.compareSync(password, hash);

  if (!user || !ok) throw ApiError.unauthorized('CREDENTIALS_INVALID', 'Sai tài khoản hoặc mật khẩu');
  if (!user.is_active) throw ApiError.forbidden('ACCOUNT_DISABLED', 'Tài khoản đã bị khoá');

  audit(db, { actorId: user.id, action: 'auth.login', entity: 'user', entityId: user.id, meta: { deviceId } });
  res.json(tokenPair(user, deviceId ?? null));
});

const refreshBody = z.object({ refreshToken: z.string().min(1) });

authRouter.post('/refresh', (req, res) => {
  const { refreshToken } = refreshBody.parse(req.body);
  const db = getDb();
  const { userId, deviceId } = rotateRefreshToken(db, refreshToken);
  const user = db.prepare(`SELECT * FROM users WHERE id = ?`).get(userId) as UserRow | undefined;
  if (!user || !user.is_active) throw ApiError.unauthorized('ACCOUNT_DISABLED', 'Tài khoản không còn hiệu lực');
  res.json(tokenPair(user, deviceId));
});

authRouter.post('/logout', (req, res) => {
  const parsed = refreshBody.safeParse(req.body);
  if (parsed.success) revokeRefreshToken(getDb(), parsed.data.refreshToken);
  res.json({ ok: true });
});

authRouter.get('/me', requireAuth, (req, res) => {
  const user = currentUser(req);
  const db = getDb();

  const classes = db
    .prepare(
      user.role === 'student'
        ? `SELECT c.id, c.code, c.name, c.term, c.room, u.full_name AS lecturer_name
             FROM enrollments e
             JOIN classes c ON c.id = e.class_id
             JOIN users u ON u.id = c.lecturer_id
            WHERE e.student_id = ?
            ORDER BY c.code`
        : `SELECT c.id, c.code, c.name, c.term, c.room, u.full_name AS lecturer_name
             FROM classes c
             JOIN users u ON u.id = c.lecturer_id
            WHERE c.lecturer_id = ?
            ORDER BY c.code`,
    )
    .all(user.id) as Array<{
    id: string;
    code: string;
    name: string;
    term: string;
    room: string | null;
    lecturer_name: string;
  }>;

  res.json({
    user: publicUser(user),
    classes: classes.map((c) => ({
      id: c.id,
      code: c.code,
      name: c.name,
      term: c.term,
      room: c.room,
      lecturerName: c.lecturer_name,
    })),
  });
});

const changePasswordBody = z.object({
  currentPassword: z.string().min(1),
  newPassword: z.string().min(8, 'Mật khẩu mới tối thiểu 8 ký tự'),
});

authRouter.post('/change-password', requireAuth, (req, res) => {
  const user = currentUser(req);
  const { currentPassword, newPassword } = changePasswordBody.parse(req.body);
  if (!bcrypt.compareSync(currentPassword, user.password_hash)) {
    throw ApiError.badRequest('PASSWORD_MISMATCH', 'Mật khẩu hiện tại không đúng');
  }
  const db = getDb();
  db.prepare(`UPDATE users SET password_hash = ? WHERE id = ?`).run(bcrypt.hashSync(newPassword, 10), user.id);
  // Đổi mật khẩu thì mọi thiết bị khác phải đăng nhập lại.
  db.prepare(`UPDATE refresh_tokens SET revoked_at = datetime('now') WHERE user_id = ? AND revoked_at IS NULL`).run(
    user.id,
  );
  audit(db, { actorId: user.id, action: 'auth.change_password', entity: 'user', entityId: user.id });
  res.json({ ok: true });
});
