import express from 'express';
import cors from 'cors';
import { config } from './config.js';
import { authRouter } from './routes/auth.js';
import { classesRouter } from './routes/classes.js';
import { attendanceRouter } from './routes/attendance.js';
import { leaveRouter } from './routes/leave.js';
import { errorHandler, notFoundHandler } from './middleware/errorHandler.js';

export const API_PREFIX = '/api/v1';

export function createApp() {
  const app = express();

  app.set('trust proxy', 1);
  app.use(
    cors({
      origin: config.corsOrigin === '*' ? true : config.corsOrigin.split(',').map((o) => o.trim()),
      credentials: false,
    }),
  );
  app.use(express.json({ limit: '1mb' }));

  app.get('/health', (_req, res) => {
    res.json({ ok: true, service: 'dy-khoa-campus-api', time: new Date().toISOString() });
  });

  app.use(`${API_PREFIX}/auth`, authRouter);
  app.use(API_PREFIX, classesRouter);
  app.use(API_PREFIX, attendanceRouter);
  app.use(API_PREFIX, leaveRouter);

  app.use(notFoundHandler);
  app.use(errorHandler);
  return app;
}
