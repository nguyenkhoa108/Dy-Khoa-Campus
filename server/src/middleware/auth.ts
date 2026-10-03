import type { NextFunction, Request, Response } from 'express';
import { ApiError } from '../lib/errors.js';
import { getDb } from '../lib/db.js';
import { verifyAccessToken } from '../lib/tokens.js';
import type { Role, UserRow } from '../lib/types.js';

declare global {
  // eslint-disable-next-line @typescript-eslint/no-namespace
  namespace Express {
    interface Request {
      user?: UserRow;
    }
  }
}

export function requireAuth(req: Request, _res: Response, next: NextFunction): void {
  const header = req.header('authorization') ?? '';
  const [scheme, token] = header.split(' ');
  if (scheme?.toLowerCase() !== 'bearer' || !token) {
    next(ApiError.unauthorized('AUTH_REQUIRED', 'Thiếu Authorization: Bearer <access token>'));
    return;
  }

  try {
    const claims = verifyAccessToken(token);
    const user = getDb().prepare(`SELECT * FROM users WHERE id = ?`).get(claims.sub) as UserRow | undefined;
    if (!user || !user.is_active) {
      next(ApiError.unauthorized('ACCOUNT_DISABLED', 'Tài khoản không tồn tại hoặc đã bị khoá'));
      return;
    }
    req.user = user;
    next();
  } catch (err) {
    next(err);
  }
}

export function requireRole(...roles: Role[]) {
  return (req: Request, _res: Response, next: NextFunction): void => {
    if (!req.user) {
      next(ApiError.unauthorized('AUTH_REQUIRED', 'Chưa đăng nhập'));
      return;
    }
    if (!roles.includes(req.user.role)) {
      next(ApiError.forbidden('ROLE_FORBIDDEN', `Chức năng này chỉ dành cho: ${roles.join(', ')}`));
      return;
    }
    next();
  };
}

/** Lấy người dùng đã xác thực, ném lỗi nếu middleware chưa chạy. */
export function currentUser(req: Request): UserRow {
  if (!req.user) throw ApiError.unauthorized('AUTH_REQUIRED', 'Chưa đăng nhập');
  return req.user;
}
