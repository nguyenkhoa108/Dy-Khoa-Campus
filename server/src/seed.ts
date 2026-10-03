import bcrypt from 'bcryptjs';
import { pathToFileURL } from 'node:url';
import { getDb, newId, nowIso, type DB } from './lib/db.js';
import type { Role } from './lib/types.js';

/**
 * Dữ liệu mẫu cho môi trường phát triển.
 * Chạy: npm run seed  (an toàn khi chạy lại — xoá sạch rồi tạo mới)
 */

const PASSWORD = 'campus123';

interface SeedUser {
  id: string;
  code: string;
  email: string;
  fullName: string;
  role: Role;
  faculty: string;
}

const users: SeedUser[] = [
  { id: 'usr_admin', code: 'AD001', email: 'admin@dykhoa.edu.vn', fullName: 'Phòng Đào tạo', role: 'admin', faculty: 'Phòng Đào tạo' },
  { id: 'usr_gv01', code: 'GV001', email: 'lan.nguyen@dykhoa.edu.vn', fullName: 'TS. Nguyễn Thị Lan', role: 'lecturer', faculty: 'Công nghệ thông tin' },
  { id: 'usr_gv02', code: 'GV002', email: 'minh.tran@dykhoa.edu.vn', fullName: 'ThS. Trần Văn Minh', role: 'lecturer', faculty: 'Công nghệ thông tin' },
  { id: 'usr_sv01', code: '2210001', email: 'an.pham@sv.dykhoa.edu.vn', fullName: 'Phạm Hoàng An', role: 'student', faculty: 'Công nghệ thông tin' },
  { id: 'usr_sv02', code: '2210002', email: 'binh.le@sv.dykhoa.edu.vn', fullName: 'Lê Thanh Bình', role: 'student', faculty: 'Công nghệ thông tin' },
  { id: 'usr_sv03', code: '2210003', email: 'chi.vo@sv.dykhoa.edu.vn', fullName: 'Võ Ngọc Chi', role: 'student', faculty: 'Công nghệ thông tin' },
  { id: 'usr_sv04', code: '2210004', email: 'dung.hoang@sv.dykhoa.edu.vn', fullName: 'Hoàng Tiến Dũng', role: 'student', faculty: 'Công nghệ thông tin' },
  { id: 'usr_sv05', code: '2210005', email: 'en.dang@sv.dykhoa.edu.vn', fullName: 'Đặng Thuỳ En', role: 'student', faculty: 'Công nghệ thông tin' },
];

const classes = [
  { id: 'cls_it4409', code: 'IT4409', name: 'Công nghệ Web và Dịch vụ trực tuyến', term: '2026.1', lecturerId: 'usr_gv01', room: 'D9-301' },
  { id: 'cls_it3100', code: 'IT3100', name: 'Lập trình hướng đối tượng', term: '2026.1', lecturerId: 'usr_gv01', room: 'D5-102' },
  { id: 'cls_it4785', code: 'IT4785', name: 'Phát triển ứng dụng cho thiết bị di động', term: '2026.1', lecturerId: 'usr_gv02', room: 'TC-205' },
];

const enrollments: Array<[string, string]> = [
  ['cls_it4409', 'usr_sv01'], ['cls_it4409', 'usr_sv02'], ['cls_it4409', 'usr_sv03'],
  ['cls_it4409', 'usr_sv04'], ['cls_it4409', 'usr_sv05'],
  ['cls_it3100', 'usr_sv01'], ['cls_it3100', 'usr_sv02'], ['cls_it3100', 'usr_sv03'],
  ['cls_it4785', 'usr_sv01'], ['cls_it4785', 'usr_sv04'], ['cls_it4785', 'usr_sv05'],
];

/** Dựng mốc giờ theo ngày hôm nay để dữ liệu mẫu luôn "tươi". */
function at(dayOffset: number, hour: number, minute = 0): string {
  const d = new Date();
  d.setDate(d.getDate() + dayOffset);
  d.setHours(hour, minute, 0, 0);
  return d.toISOString();
}

/** Mốc giờ lệch so với hiện tại — dùng cho buổi học đang diễn ra. */
function fromNow(minutes: number): string {
  return new Date(Date.now() + minutes * 60_000).toISOString();
}

export function seed(db: DB = getDb()): void {
  const hash = bcrypt.hashSync(PASSWORD, 10);
  const now = nowIso();

  db.transaction(() => {
    for (const table of [
      'audit_log', 'used_qr_nonces', 'refresh_tokens', 'attendance_records',
      'leave_requests', 'class_sessions', 'enrollments', 'classes', 'users',
    ]) {
      db.prepare(`DELETE FROM ${table}`).run();
    }

    const insertUser = db.prepare(
      `INSERT INTO users (id, code, email, password_hash, full_name, role, faculty, is_active, created_at)
       VALUES (?, ?, ?, ?, ?, ?, ?, 1, ?)`,
    );
    for (const u of users) insertUser.run(u.id, u.code, u.email, hash, u.fullName, u.role, u.faculty, now);

    const insertClass = db.prepare(
      `INSERT INTO classes (id, code, name, term, lecturer_id, room, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)`,
    );
    for (const c of classes) insertClass.run(c.id, c.code, c.name, c.term, c.lecturerId, c.room, now);

    const insertEnrollment = db.prepare(
      `INSERT INTO enrollments (class_id, student_id, created_at) VALUES (?, ?, ?)`,
    );
    for (const [classId, studentId] of enrollments) insertEnrollment.run(classId, studentId, now);

    const insertSession = db.prepare(
      `INSERT INTO class_sessions (id, class_id, title, room, starts_at, ends_at, late_after_min, checkin_state, opened_at, created_at)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
    );
    // Một buổi đang mở điểm danh để mở app là quét được ngay.
    // Buổi này bám theo giờ hiện tại (vừa bắt đầu) để quét thử là ra "có mặt", không phải "đi muộn".
    insertSession.run('ses_open_now', 'cls_it4409', 'Buổi 5 — REST API và xác thực', 'D9-301', fromNow(-5), fromNow(145), 15, 'open', now, now);
    insertSession.run('ses_today_pm', 'cls_it4785', 'Buổi 5 — React Native: camera và quyền', 'TC-205', at(0, 13, 30), at(0, 16, 0), 10, 'closed', null, now);
    insertSession.run('ses_prev_1', 'cls_it4409', 'Buổi 4 — Thiết kế cơ sở dữ liệu', 'D9-301', at(-7, 7, 0), at(-7, 9, 30), 15, 'closed', null, now);
    insertSession.run('ses_prev_2', 'cls_it3100', 'Buổi 4 — Kế thừa và đa hình', 'D5-102', at(-5, 9, 45), at(-5, 12, 0), 15, 'closed', null, now);
    insertSession.run('ses_next_1', 'cls_it4409', 'Buổi 6 — Triển khai và CI/CD', 'D9-301', at(7, 7, 0), at(7, 9, 30), 15, 'closed', null, now);

    // Lịch sử điểm danh của các buổi đã đóng.
    const insertAttendance = db.prepare(
      `INSERT INTO attendance_records (id, session_id, student_id, status, method, checked_in_at, recorded_by, created_at, updated_at)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`,
    );
    const history: Array<[string, string, 'present' | 'late' | 'absent' | 'excused']> = [
      ['ses_prev_1', 'usr_sv01', 'present'], ['ses_prev_1', 'usr_sv02', 'late'],
      ['ses_prev_1', 'usr_sv03', 'present'], ['ses_prev_1', 'usr_sv04', 'absent'],
      ['ses_prev_1', 'usr_sv05', 'present'],
      ['ses_prev_2', 'usr_sv01', 'present'], ['ses_prev_2', 'usr_sv02', 'present'],
      ['ses_prev_2', 'usr_sv03', 'excused'],
    ];
    for (const [sessionId, studentId, status] of history) {
      const checkedIn = status === 'present' || status === 'late' ? at(-7, 7, status === 'late' ? 25 : 2) : null;
      insertAttendance.run(
        newId('att'), sessionId, studentId, status,
        checkedIn ? 'qr_session' : status === 'excused' ? 'leave' : 'manual',
        checkedIn, 'usr_gv01', now, now,
      );
    }

    // Vài đơn phép: một đơn chờ duyệt để mở app là thấy việc cần làm.
    const insertLeave = db.prepare(
      `INSERT INTO leave_requests (id, student_id, class_id, type, start_date, end_date, reason, status, reviewer_id, review_note, reviewed_at, created_at, updated_at)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
    );
    const day = (offset: number) => at(offset, 12).slice(0, 10);
    insertLeave.run('lv_pending_1', 'usr_sv02', 'cls_it4409', 'sick', day(1), day(1), 'Em bị sốt siêu vi, có giấy khám của trạm y tế trường.', 'pending', null, null, null, now, now);
    insertLeave.run('lv_pending_2', 'usr_sv04', 'cls_it4409', 'family', day(2), day(3), 'Gia đình em có việc tang, em xin phép nghỉ 2 buổi.', 'pending', null, null, null, now, now);
    insertLeave.run('lv_pending_3', 'usr_sv01', 'cls_it4785', 'personal', day(4), day(4), 'Em tham gia cuộc thi Olympic Tin học cấp trường.', 'pending', null, null, null, now, now);
    insertLeave.run('lv_done_1', 'usr_sv03', 'cls_it3100', 'sick', day(-5), day(-5), 'Em bị đau dạ dày phải nhập viện theo dõi.', 'approved', 'usr_gv01', 'Đã nhận giấy ra viện.', now, now, now);
    insertLeave.run('lv_done_2', 'usr_sv05', 'cls_it4409', 'other', day(-3), day(-3), 'Em bận việc riêng.', 'rejected', 'usr_gv01', 'Lý do chưa đủ cụ thể, em bổ sung minh chứng nhé.', now, now, now);
  })();
}

// Chạy trực tiếp qua `npm run seed`.
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  seed();
  console.log('Đã nạp dữ liệu mẫu.');
  console.log(`Mật khẩu chung cho mọi tài khoản: ${PASSWORD}`);
  console.table(users.map((u) => ({ 'Mã số': u.code, 'Email': u.email, 'Vai trò': u.role, 'Họ tên': u.fullName })));
}

export { users as seedUsers, PASSWORD as SEED_PASSWORD };
