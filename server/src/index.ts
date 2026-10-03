import { config } from './config.js';
import { createApp } from './app.js';
import { getDb } from './lib/db.js';
import { purgeExpiredNonces } from './lib/qr.js';
import { purgeExpiredRefreshTokens } from './lib/tokens.js';

const db = getDb();

// Dọn nonce QR và refresh token hết hạn định kỳ để bảng không phình vô hạn.
const sweeper = setInterval(
  () => {
    try {
      purgeExpiredNonces(db);
      purgeExpiredRefreshTokens(db);
    } catch (err) {
      console.error('[sweeper]', err);
    }
  },
  5 * 60 * 1000,
);
sweeper.unref();

const server = createApp().listen(config.port, () => {
  console.log(`Dy Khoa Campus API đang chạy tại http://localhost:${config.port}`);
  console.log(`  health:   http://localhost:${config.port}/health`);
  console.log(`  base URL cho app di động: http://<IP-LAN-cua-may-nay>:${config.port}/api/v1`);
});

for (const signal of ['SIGINT', 'SIGTERM'] as const) {
  process.on(signal, () => {
    server.close(() => {
      db.close();
      process.exit(0);
    });
  });
}
