import { createHmac, randomBytes, timingSafeEqual } from 'node:crypto';
import { config } from '../config.js';
import { ApiError } from './errors.js';
import type { DB } from './db.js';

/**
 * Định dạng mã QR của Dy Khoa Campus
 * ----------------------------------
 *   DKC1.<base64url(payload JSON)>.<base64url(HMAC-SHA256)>
 *
 * Chữ ký do máy chủ tạo bằng QR_SECRET, nên điện thoại chỉ hiển thị và quét —
 * không thể tự chế mã hợp lệ. Payload có hạn rất ngắn (xoay vòng liên tục) và
 * mang một `n` (nonce) ngẫu nhiên để chặn phát lại ảnh chụp màn hình.
 *
 * Hai chiều điểm danh đều được hỗ trợ:
 *   t = 'S'  mã của BUỔI HỌC   — giảng viên chiếu lên màn hình, sinh viên quét
 *   t = 'U'  mã của SINH VIÊN  — sinh viên mở trên app, giảng viên quét
 */

const PREFIX = 'DKC1';
export const QR_VERSION = 1;

interface BasePayload {
  v: number;
  n: string;
  iat: number;
  exp: number;
}
export interface SessionQrPayload extends BasePayload {
  t: 'S';
  sid: string;
}
export interface StudentQrPayload extends BasePayload {
  t: 'U';
  uid: string;
}
export type QrPayload = SessionQrPayload | StudentQrPayload;

function sign(body: string): string {
  return createHmac('sha256', config.qrSecret).update(body).digest('base64url');
}

function encode(payload: QrPayload): string {
  const body = `${PREFIX}.${Buffer.from(JSON.stringify(payload), 'utf8').toString('base64url')}`;
  return `${body}.${sign(body)}`;
}

export function issueSessionQr(sessionId: string, now = Date.now()): { token: string; payload: SessionQrPayload } {
  const iat = Math.floor(now / 1000);
  const payload: SessionQrPayload = {
    v: QR_VERSION,
    t: 'S',
    sid: sessionId,
    n: randomBytes(9).toString('base64url'),
    iat,
    exp: iat + config.sessionQrTtlSec,
  };
  return { token: encode(payload), payload };
}

export function issueStudentQr(studentId: string, now = Date.now()): { token: string; payload: StudentQrPayload } {
  const iat = Math.floor(now / 1000);
  const payload: StudentQrPayload = {
    v: QR_VERSION,
    t: 'U',
    uid: studentId,
    n: randomBytes(9).toString('base64url'),
    iat,
    exp: iat + config.studentQrTtlSec,
  };
  return { token: encode(payload), payload };
}

/** Kiểm tra chữ ký, phiên bản và hạn dùng. Không đụng tới CSDL. */
export function verifyQr(token: string, now = Date.now()): QrPayload {
  const parts = token.trim().split('.');
  if (parts.length !== 3 || parts[0] !== PREFIX) {
    throw ApiError.badRequest('QR_MALFORMED', 'Mã QR không thuộc hệ thống Dy Khoa Campus');
  }
  const [, payloadB64, signature] = parts as [string, string, string];

  const expected = Buffer.from(sign(`${PREFIX}.${payloadB64}`), 'utf8');
  const actual = Buffer.from(signature, 'utf8');
  if (expected.length !== actual.length || !timingSafeEqual(expected, actual)) {
    throw ApiError.badRequest('QR_SIGNATURE_INVALID', 'Mã QR có chữ ký không hợp lệ');
  }

  let payload: QrPayload;
  try {
    payload = JSON.parse(Buffer.from(payloadB64, 'base64url').toString('utf8')) as QrPayload;
  } catch {
    throw ApiError.badRequest('QR_MALFORMED', 'Nội dung mã QR không đọc được');
  }

  if (payload.v !== QR_VERSION) {
    throw ApiError.badRequest('QR_VERSION_UNSUPPORTED', 'Phiên bản mã QR không được hỗ trợ, vui lòng cập nhật ứng dụng');
  }
  if (payload.t !== 'S' && payload.t !== 'U') {
    throw ApiError.badRequest('QR_MALFORMED', 'Loại mã QR không hợp lệ');
  }

  const nowSec = Math.floor(now / 1000);
  const skew = config.qrClockSkewSec;
  if (nowSec > payload.exp + skew) {
    throw ApiError.badRequest('QR_EXPIRED', 'Mã QR đã hết hạn, vui lòng quét lại mã mới nhất');
  }
  if (nowSec < payload.iat - skew) {
    throw ApiError.badRequest('QR_NOT_YET_VALID', 'Mã QR chưa có hiệu lực, kiểm tra lại đồng hồ thiết bị');
  }

  return payload;
}

/**
 * Ghi nhận nonce đã được `subjectId` tiêu thụ.
 * Trả về false nếu cặp (nonce, subject) đã dùng — tức là một lần phát lại.
 */
export function consumeNonce(db: DB, nonce: string, subjectId: string, expiresAtSec: number): boolean {
  const changes = db
    .prepare(`INSERT OR IGNORE INTO used_qr_nonces (nonce, subject_id, expires_at) VALUES (?, ?, ?)`)
    .run(nonce, subjectId, expiresAtSec).changes;
  return changes > 0;
}

export function purgeExpiredNonces(db: DB, now = Date.now()): void {
  db.prepare(`DELETE FROM used_qr_nonces WHERE expires_at < ?`).run(Math.floor(now / 1000) - config.qrClockSkewSec);
}
