import request from 'supertest';
import type { Express } from 'express';
import { createApp, API_PREFIX } from '../src/app.js';
import { openDatabase, setDb, type DB } from '../src/lib/db.js';
import { seed, SEED_PASSWORD } from '../src/seed.js';

export { API_PREFIX, SEED_PASSWORD };

export interface TestContext {
  app: Express;
  db: DB;
}

export function bootstrap(): TestContext {
  const db = openDatabase(':memory:');
  setDb(db);
  seed(db);
  return { app: createApp(), db };
}

export async function login(app: Express, identifier: string): Promise<string> {
  const res = await request(app)
    .post(`${API_PREFIX}/auth/login`)
    .send({ identifier, password: SEED_PASSWORD });
  if (res.status !== 200) throw new Error(`login failed for ${identifier}: ${res.status} ${res.text}`);
  return res.body.accessToken as string;
}

export function auth(token: string) {
  return { Authorization: `Bearer ${token}` };
}
