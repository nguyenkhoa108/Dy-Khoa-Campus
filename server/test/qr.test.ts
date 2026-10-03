import { describe, expect, it } from 'vitest';
import { config } from '../src/config.js';
import { ApiError } from '../src/lib/errors.js';
import { consumeNonce, issueSessionQr, issueStudentQr, purgeExpiredNonces, verifyQr } from '../src/lib/qr.js';
import { openDatabase } from '../src/lib/db.js';

function expectApiError(fn: () => unknown, code: string) {
  try {
    fn();
  } catch (err) {
    expect(err).toBeInstanceOf(ApiError);
    expect((err as ApiError).code).toBe(code);
    return;
  }
  throw new Error(`Mong đợi lỗi ${code} nhưng không có lỗi nào được ném`);
}

describe('mã QR có chữ ký', () => {
  it('đi và về nguyên vẹn', () => {
    const { token, payload } = issueSessionQr('ses_abc');
    const decoded = verifyQr(token);
    expect(decoded.t).toBe('S');
    expect(decoded).toMatchObject({ sid: 'ses_abc', n: payload.n });
  });

  it('phân biệt mã buổi học và mã sinh viên', () => {
    expect(verifyQr(issueStudentQr('usr_sv01').token).t).toBe('U');
    expect(verifyQr(issueSessionQr('ses_abc').token).t).toBe('S');
  });

  it('từ chối mã bị sửa nội dung', () => {
    const { token } = issueSessionQr('ses_abc');
    const [prefix, payload, sig] = token.split('.') as [string, string, string];
    const forged = Buffer.from(JSON.stringify({ v: 1, t: 'S', sid: 'ses_khac', n: 'x', iat: 1, exp: 9e9 })).toString(
      'base64url',
    );
    expectApiError(() => verifyQr(`${prefix}.${forged}.${sig}`), 'QR_SIGNATURE_INVALID');
    expect(() => verifyQr(`${prefix}.${payload}.${sig}`)).not.toThrow();
  });

  it('từ chối chuỗi không đúng định dạng', () => {
    for (const bad of ['', 'xin-chao', 'DKC1.chi-co-hai-phan', 'OTHER.a.b']) {
      expectApiError(() => verifyQr(bad), 'QR_MALFORMED');
    }
  });

  it('hết hạn sau TTL cộng dung sai đồng hồ', () => {
    const now = Date.now();
    const { token } = issueSessionQr('ses_abc', now);
    const ttlMs = config.sessionQrTtlSec * 1000;
    const skewMs = config.qrClockSkewSec * 1000;

    expect(() => verifyQr(token, now + ttlMs - 1000)).not.toThrow();
    expect(() => verifyQr(token, now + ttlMs + skewMs - 1000)).not.toThrow();
    expectApiError(() => verifyQr(token, now + ttlMs + skewMs + 2000), 'QR_EXPIRED');
  });

  it('từ chối mã từ tương lai (đồng hồ máy lệch quá nhiều)', () => {
    const now = Date.now();
    const { token } = issueSessionQr('ses_abc', now);
    expectApiError(() => verifyQr(token, now - (config.qrClockSkewSec + 5) * 1000), 'QR_NOT_YET_VALID');
  });
});

describe('chống phát lại bằng nonce', () => {
  it('mỗi cặp (nonce, người dùng) chỉ tiêu thụ được một lần', () => {
    const db = openDatabase(':memory:');
    const exp = Math.floor(Date.now() / 1000) + 60;

    expect(consumeNonce(db, 'nonce-1', 'usr_sv01:ses_a', exp)).toBe(true);
    expect(consumeNonce(db, 'nonce-1', 'usr_sv01:ses_a', exp)).toBe(false);
    // Người khác vẫn quét được chính mã đó — mã buổi học là mã chung cho cả lớp.
    expect(consumeNonce(db, 'nonce-1', 'usr_sv02:ses_a', exp)).toBe(true);
    db.close();
  });

  it('dọn được các nonce đã hết hạn', () => {
    const db = openDatabase(':memory:');
    const past = Math.floor(Date.now() / 1000) - 3600;
    consumeNonce(db, 'nonce-cu', 'usr_sv01:ses_a', past);
    consumeNonce(db, 'nonce-moi', 'usr_sv01:ses_a', Math.floor(Date.now() / 1000) + 600);

    purgeExpiredNonces(db);
    const rows = db.prepare(`SELECT nonce FROM used_qr_nonces`).all() as Array<{ nonce: string }>;
    expect(rows.map((r) => r.nonce)).toEqual(['nonce-moi']);
    db.close();
  });
});
