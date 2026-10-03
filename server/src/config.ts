import 'dotenv/config';

function str(name: string, fallback?: string): string {
  const v = process.env[name] ?? fallback;
  if (v === undefined || v === '') throw new Error(`Missing required env var ${name}`);
  return v;
}

function int(name: string, fallback: number): number {
  const raw = process.env[name];
  if (raw === undefined || raw === '') return fallback;
  const n = Number.parseInt(raw, 10);
  if (!Number.isFinite(n)) throw new Error(`Env var ${name} must be an integer, got "${raw}"`);
  return n;
}

const isProd = process.env.NODE_ENV === 'production';
const DEV_JWT_SECRET = 'dev-only-change-me-dy-khoa-campus-secret-key';
const DEV_QR_SECRET = 'dev-only-change-me-dy-khoa-campus-qr-key';

export const config = {
  isProd,
  isTest: process.env.NODE_ENV === 'test',
  port: int('PORT', 4000),
  jwtSecret: str('JWT_SECRET', isProd ? undefined : DEV_JWT_SECRET),
  qrSecret: str('QR_SECRET', isProd ? undefined : DEV_QR_SECRET),
  accessTokenTtlSec: int('ACCESS_TOKEN_TTL_SEC', 15 * 60),
  refreshTokenTtlSec: int('REFRESH_TOKEN_TTL_SEC', 30 * 24 * 3600),
  sessionQrTtlSec: int('SESSION_QR_TTL_SEC', 30),
  studentQrTtlSec: int('STUDENT_QR_TTL_SEC', 60),
  qrClockSkewSec: int('QR_CLOCK_SKEW_SEC', 10),
  databaseFile: str('DATABASE_FILE', './data/campus.db'),
  corsOrigin: str('CORS_ORIGIN', '*'),
} as const;

// Fail fast rather than shipping the documented development secrets to production.
if (isProd) {
  if (config.jwtSecret === DEV_JWT_SECRET || config.qrSecret === DEV_QR_SECRET) {
    throw new Error('Refusing to start in production with the example JWT_SECRET/QR_SECRET');
  }
  for (const [name, value] of [['JWT_SECRET', config.jwtSecret], ['QR_SECRET', config.qrSecret]] as const) {
    if (value.length < 32) throw new Error(`${name} must be at least 32 characters in production`);
  }
}
