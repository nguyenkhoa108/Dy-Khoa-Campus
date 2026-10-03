import { createHash, randomBytes } from 'node:crypto';
import jwt from 'jsonwebtoken';
import { config } from '../config.js';
import { ApiError } from './errors.js';
import { newId, nowIso, type DB } from './db.js';
import type { Role } from './types.js';

export interface AccessClaims {
  sub: string;
  role: Role;
  code: string;
  name: string;
}

export function signAccessToken(claims: AccessClaims): string {
  return jwt.sign(claims, config.jwtSecret, {
    expiresIn: config.accessTokenTtlSec,
    issuer: 'dy-khoa-campus',
    audience: 'dy-khoa-campus-mobile',
  });
}

export function verifyAccessToken(token: string): AccessClaims {
  try {
    return jwt.verify(token, config.jwtSecret, {
      issuer: 'dy-khoa-campus',
      audience: 'dy-khoa-campus-mobile',
    }) as AccessClaims;
  } catch (err) {
    const expired = err instanceof jwt.TokenExpiredError;
    throw ApiError.unauthorized(
      expired ? 'TOKEN_EXPIRED' : 'TOKEN_INVALID',
      expired ? 'Access token đã hết hạn' : 'Access token không hợp lệ',
    );
  }
}

function hashRefreshToken(token: string): string {
  return createHash('sha256').update(token).digest('hex');
}

export function issueRefreshToken(db: DB, userId: string, deviceId: string | null): { token: string; expiresAt: number } {
  const token = randomBytes(48).toString('base64url');
  const expiresAt = Math.floor(Date.now() / 1000) + config.refreshTokenTtlSec;
  db.prepare(
    `INSERT INTO refresh_tokens (id, user_id, token_hash, device_id, expires_at, created_at)
     VALUES (?, ?, ?, ?, ?, ?)`,
  ).run(newId('rt'), userId, hashRefreshToken(token), deviceId, expiresAt, nowIso());
  return { token, expiresAt };
}

/**
 * Đổi refresh token lấy cặp token mới (xoay vòng token).
 * Nếu một token đã thu hồi bị dùng lại, thu hồi toàn bộ phiên của người dùng đó.
 */
export function rotateRefreshToken(db: DB, token: string): { userId: string; deviceId: string | null } {
  const row = db
    .prepare(`SELECT id, user_id, device_id, expires_at, revoked_at FROM refresh_tokens WHERE token_hash = ?`)
    .get(hashRefreshToken(token)) as
    | { id: string; user_id: string; device_id: string | null; expires_at: number; revoked_at: string | null }
    | undefined;

  if (!row) throw ApiError.unauthorized('REFRESH_INVALID', 'Refresh token không hợp lệ');

  if (row.revoked_at) {
    db.prepare(`UPDATE refresh_tokens SET revoked_at = ? WHERE user_id = ? AND revoked_at IS NULL`).run(
      nowIso(),
      row.user_id,
    );
    throw ApiError.unauthorized('REFRESH_REUSED', 'Refresh token đã bị dùng lại, mọi phiên đã được thu hồi');
  }

  if (row.expires_at <= Math.floor(Date.now() / 1000)) {
    throw ApiError.unauthorized('REFRESH_EXPIRED', 'Refresh token đã hết hạn');
  }

  db.prepare(`UPDATE refresh_tokens SET revoked_at = ? WHERE id = ?`).run(nowIso(), row.id);
  return { userId: row.user_id, deviceId: row.device_id };
}

export function revokeRefreshToken(db: DB, token: string): void {
  db.prepare(`UPDATE refresh_tokens SET revoked_at = ? WHERE token_hash = ? AND revoked_at IS NULL`).run(
    nowIso(),
    hashRefreshToken(token),
  );
}

export function purgeExpiredRefreshTokens(db: DB): void {
  db.prepare(`DELETE FROM refresh_tokens WHERE expires_at < ?`).run(Math.floor(Date.now() / 1000));
}
