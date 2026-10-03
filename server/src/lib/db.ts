import Database from 'better-sqlite3';
import { randomUUID } from 'node:crypto';
import { mkdirSync, readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { config } from '../config.js';

const here = dirname(fileURLToPath(import.meta.url));
const SCHEMA_PATH = join(here, 'schema.sql');

export type DB = Database.Database;

let instance: DB | null = null;

export function openDatabase(file = config.databaseFile): DB {
  if (file !== ':memory:') mkdirSync(dirname(file), { recursive: true });
  const db = new Database(file);
  db.pragma('foreign_keys = ON');
  db.exec(readFileSync(SCHEMA_PATH, 'utf8'));
  return db;
}

export function getDb(): DB {
  if (!instance) instance = openDatabase();
  return instance;
}

/** Dùng trong test để trỏ vào CSDL trong bộ nhớ. */
export function setDb(db: DB): void {
  instance = db;
}

export function newId(prefix: string): string {
  return `${prefix}_${randomUUID().replaceAll('-', '').slice(0, 20)}`;
}

export function nowIso(): string {
  return new Date().toISOString();
}

export function audit(
  db: DB,
  entry: { actorId: string | null; action: string; entity: string; entityId?: string | null; meta?: unknown },
): void {
  db.prepare(
    `INSERT INTO audit_log (id, actor_id, action, entity, entity_id, meta, created_at)
     VALUES (?, ?, ?, ?, ?, ?, ?)`,
  ).run(
    newId('aud'),
    entry.actorId,
    entry.action,
    entry.entity,
    entry.entityId ?? null,
    entry.meta === undefined ? null : JSON.stringify(entry.meta),
    nowIso(),
  );
}
