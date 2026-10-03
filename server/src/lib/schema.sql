PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

-- Người dùng: sinh viên, giảng viên, quản trị
CREATE TABLE IF NOT EXISTS users (
  id            TEXT PRIMARY KEY,
  code          TEXT NOT NULL UNIQUE,              -- MSSV hoặc mã giảng viên
  email         TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  full_name     TEXT NOT NULL,
  role          TEXT NOT NULL CHECK (role IN ('student', 'lecturer', 'admin')),
  faculty       TEXT,
  avatar_url    TEXT,
  is_active     INTEGER NOT NULL DEFAULT 1,
  created_at    TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Lớp học phần
CREATE TABLE IF NOT EXISTS classes (
  id          TEXT PRIMARY KEY,
  code        TEXT NOT NULL UNIQUE,
  name        TEXT NOT NULL,
  term        TEXT NOT NULL,                       -- vd. "2026.1"
  lecturer_id TEXT NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
  room        TEXT,
  created_at  TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_classes_lecturer ON classes(lecturer_id);

-- Sinh viên đăng ký lớp
CREATE TABLE IF NOT EXISTS enrollments (
  class_id   TEXT NOT NULL REFERENCES classes(id) ON DELETE CASCADE,
  student_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY (class_id, student_id)
);
CREATE INDEX IF NOT EXISTS idx_enrollments_student ON enrollments(student_id);

-- Buổi học (ca điểm danh)
CREATE TABLE IF NOT EXISTS class_sessions (
  id             TEXT PRIMARY KEY,
  class_id       TEXT NOT NULL REFERENCES classes(id) ON DELETE CASCADE,
  title          TEXT NOT NULL,
  room           TEXT,
  starts_at      TEXT NOT NULL,                    -- ISO 8601 UTC
  ends_at        TEXT NOT NULL,
  late_after_min INTEGER NOT NULL DEFAULT 15,      -- sau mốc này tính "đi muộn"
  checkin_state  TEXT NOT NULL DEFAULT 'closed' CHECK (checkin_state IN ('closed', 'open')),
  opened_at      TEXT,
  closed_at      TEXT,
  created_at     TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_sessions_class ON class_sessions(class_id);
CREATE INDEX IF NOT EXISTS idx_sessions_starts ON class_sessions(starts_at);

-- Bản ghi điểm danh: tối đa 1 bản ghi cho mỗi (buổi học, sinh viên)
CREATE TABLE IF NOT EXISTS attendance_records (
  id            TEXT PRIMARY KEY,
  session_id    TEXT NOT NULL REFERENCES class_sessions(id) ON DELETE CASCADE,
  student_id    TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  status        TEXT NOT NULL CHECK (status IN ('present', 'late', 'absent', 'excused')),
  method        TEXT NOT NULL CHECK (method IN ('qr_session', 'qr_student', 'manual', 'leave')),
  checked_in_at TEXT,
  recorded_by   TEXT REFERENCES users(id) ON DELETE SET NULL,
  device_id     TEXT,
  client_uuid   TEXT UNIQUE,                       -- chống ghi trùng khi đồng bộ offline
  note          TEXT,
  created_at    TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at    TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE (session_id, student_id)
);
CREATE INDEX IF NOT EXISTS idx_attendance_student ON attendance_records(student_id);
CREATE INDEX IF NOT EXISTS idx_attendance_session ON attendance_records(session_id);

-- Nonce của mã QR đã dùng: chặn phát lại (replay) ảnh chụp màn hình trong thời gian token còn hạn
CREATE TABLE IF NOT EXISTS used_qr_nonces (
  nonce      TEXT NOT NULL,
  subject_id TEXT NOT NULL,                        -- ai đã tiêu thụ nonce này
  expires_at INTEGER NOT NULL,                     -- epoch giây, để dọn dẹp
  PRIMARY KEY (nonce, subject_id)
);
CREATE INDEX IF NOT EXISTS idx_nonces_expiry ON used_qr_nonces(expires_at);

-- Đơn xin phép
CREATE TABLE IF NOT EXISTS leave_requests (
  id             TEXT PRIMARY KEY,
  student_id     TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  class_id       TEXT REFERENCES classes(id) ON DELETE CASCADE,  -- NULL = áp dụng mọi lớp
  type           TEXT NOT NULL CHECK (type IN ('sick', 'personal', 'family', 'other')),
  start_date     TEXT NOT NULL,                    -- YYYY-MM-DD
  end_date       TEXT NOT NULL,                    -- YYYY-MM-DD, bao gồm cả ngày này
  reason         TEXT NOT NULL,
  attachment_url TEXT,
  status         TEXT NOT NULL DEFAULT 'pending'
                 CHECK (status IN ('pending', 'approved', 'rejected', 'cancelled')),
  reviewer_id    TEXT REFERENCES users(id) ON DELETE SET NULL,
  review_note    TEXT,
  reviewed_at    TEXT,
  created_at     TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at     TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_leave_student ON leave_requests(student_id);
CREATE INDEX IF NOT EXISTS idx_leave_status ON leave_requests(status);
CREATE INDEX IF NOT EXISTS idx_leave_class ON leave_requests(class_id);

-- Refresh token (lưu dạng băm). Mỗi thiết bị một chuỗi token riêng.
CREATE TABLE IF NOT EXISTS refresh_tokens (
  id         TEXT PRIMARY KEY,
  user_id    TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  token_hash TEXT NOT NULL UNIQUE,
  device_id  TEXT,
  expires_at INTEGER NOT NULL,                     -- epoch giây
  revoked_at TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_refresh_user ON refresh_tokens(user_id);

-- Nhật ký thao tác, phục vụ đối soát với web app
CREATE TABLE IF NOT EXISTS audit_log (
  id         TEXT PRIMARY KEY,
  actor_id   TEXT REFERENCES users(id) ON DELETE SET NULL,
  action     TEXT NOT NULL,
  entity     TEXT NOT NULL,
  entity_id  TEXT,
  meta       TEXT,                                 -- JSON
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_audit_entity ON audit_log(entity, entity_id);
