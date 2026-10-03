import { beforeEach, describe, expect, it } from 'vitest';
import request from 'supertest';
import { API_PREFIX, auth, bootstrap, login, type TestContext } from './helpers.js';

let ctx: TestContext;
let lecturer: string; // GV001 — phụ trách IT4409, IT3100
let student: string; // 2210001 — usr_sv01
let admin: string;

const today = () => new Date().toISOString().slice(0, 10);
const plusDays = (n: number) => new Date(Date.now() + n * 86_400_000).toISOString().slice(0, 10);

beforeEach(async () => {
  ctx = bootstrap();
  lecturer = await login(ctx.app, 'GV001');
  student = await login(ctx.app, '2210001');
  admin = await login(ctx.app, 'AD001');
});

describe('nộp đơn xin phép', () => {
  it('sinh viên nộp đơn thành công, trạng thái chờ duyệt', async () => {
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/leave-requests`)
      .set(auth(student))
      .send({
        classId: 'cls_it4409',
        type: 'sick',
        startDate: plusDays(1),
        endDate: plusDays(1),
        reason: 'Em bị cúm, có đơn thuốc của bác sĩ.',
      });

    expect(res.status).toBe(201);
    expect(res.body.leaveRequest.status).toBe('pending');
    expect(res.body.leaveRequest.student.code).toBe('2210001');
    expect(res.body.leaveRequest.class.code).toBe('IT4409');
  });

  it('từ chối ngày kết thúc trước ngày bắt đầu', async () => {
    const res = await request(ctx.app).post(`${API_PREFIX}/leave-requests`).set(auth(student)).send({
      classId: 'cls_it4409',
      type: 'personal',
      startDate: plusDays(5),
      endDate: plusDays(2),
      reason: 'Lý do hợp lệ nhưng ngày sai.',
    });
    expect(res.status).toBe(400);
    expect(res.body.error.code).toBe('DATE_RANGE_INVALID');
  });

  it('từ chối lớp sinh viên không đăng ký', async () => {
    const other = await login(ctx.app, '2210002'); // không học IT4785
    const res = await request(ctx.app).post(`${API_PREFIX}/leave-requests`).set(auth(other)).send({
      classId: 'cls_it4785',
      type: 'personal',
      startDate: plusDays(1),
      endDate: plusDays(1),
      reason: 'Em xin nghỉ buổi này ạ.',
    });
    expect(res.status).toBe(403);
    expect(res.body.error.code).toBe('NOT_ENROLLED');
  });

  it('chặn nộp đơn trùng khoảng thời gian đang chờ duyệt', async () => {
    const body = {
      classId: 'cls_it4409',
      type: 'sick' as const,
      startDate: plusDays(1),
      endDate: plusDays(3),
      reason: 'Em bị sốt cao phải nghỉ mấy hôm.',
    };
    await request(ctx.app).post(`${API_PREFIX}/leave-requests`).set(auth(student)).send(body).expect(201);

    const dup = await request(ctx.app)
      .post(`${API_PREFIX}/leave-requests`)
      .set(auth(student))
      .send({ ...body, startDate: plusDays(2), endDate: plusDays(4) });
    expect(dup.status).toBe(409);
    expect(dup.body.error.code).toBe('LEAVE_OVERLAPPING');
  });

  it('giảng viên không nộp được đơn xin phép', async () => {
    const res = await request(ctx.app).post(`${API_PREFIX}/leave-requests`).set(auth(lecturer)).send({
      classId: 'cls_it4409',
      type: 'sick',
      startDate: today(),
      endDate: today(),
      reason: 'Thử nộp đơn.',
    });
    expect(res.status).toBe(403);
  });

  it('bắt buộc lý do đủ dài', async () => {
    const res = await request(ctx.app).post(`${API_PREFIX}/leave-requests`).set(auth(student)).send({
      classId: 'cls_it4409',
      type: 'other',
      startDate: plusDays(1),
      endDate: plusDays(1),
      reason: 'ốm',
    });
    expect(res.status).toBe(400);
    expect(res.body.error.code).toBe('VALIDATION_FAILED');
  });
});

describe('hộp duyệt đơn', () => {
  it('giảng viên chỉ thấy đơn của lớp mình phụ trách', async () => {
    const res = await request(ctx.app).get(`${API_PREFIX}/leave-requests?status=pending`).set(auth(lecturer));
    expect(res.status).toBe(200);
    const ids = res.body.items.map((i: any) => i.id);
    expect(ids).toContain('lv_pending_1'); // IT4409
    expect(ids).toContain('lv_pending_2'); // IT4409
    expect(ids).not.toContain('lv_pending_3'); // IT4785 của GV002
  });

  it('sinh viên chỉ thấy đơn của chính mình', async () => {
    const res = await request(ctx.app).get(`${API_PREFIX}/leave-requests`).set(auth(student));
    expect(res.status).toBe(200);
    expect(res.body.items.every((i: any) => i.studentId === 'usr_sv01')).toBe(true);
  });

  it('đơn chờ duyệt được xếp lên đầu danh sách', async () => {
    const res = await request(ctx.app).get(`${API_PREFIX}/leave-requests`).set(auth(admin));
    expect(res.body.items[0].status).toBe('pending');
  });

  it('đếm số đơn chờ duyệt cho chấm đỏ trên tab', async () => {
    const gv = await request(ctx.app).get(`${API_PREFIX}/leave-requests/pending-count`).set(auth(lecturer));
    expect(gv.body.pending).toBe(2);

    const ad = await request(ctx.app).get(`${API_PREFIX}/leave-requests/pending-count`).set(auth(admin));
    expect(ad.body.pending).toBe(3);

    const sv = await request(ctx.app).get(`${API_PREFIX}/leave-requests/pending-count`).set(auth(student));
    expect(sv.status).toBe(403);
  });

  it('giảng viên không xem được chi tiết đơn ngoài lớp mình', async () => {
    const res = await request(ctx.app).get(`${API_PREFIX}/leave-requests/lv_pending_3`).set(auth(lecturer));
    expect(res.status).toBe(403);
  });
});

describe('phê duyệt', () => {
  it('duyệt đơn và tự đánh dấu nghỉ có phép cho buổi học trong khoảng ngày', async () => {
    // Buổi học tương lai của IT4409 nằm trong khoảng xin phép.
    const sessionDate = ctx.db.prepare(`SELECT starts_at FROM class_sessions WHERE id = 'ses_next_1'`).get() as {
      starts_at: string;
    };
    const day = sessionDate.starts_at.slice(0, 10);

    const created = await request(ctx.app).post(`${API_PREFIX}/leave-requests`).set(auth(student)).send({
      classId: 'cls_it4409',
      type: 'family',
      startDate: day,
      endDate: day,
      reason: 'Em về quê lo việc gia đình, xin phép nghỉ buổi này.',
    });
    expect(created.status).toBe(201);

    const approved = await request(ctx.app)
      .post(`${API_PREFIX}/leave-requests/${created.body.leaveRequest.id}/approve`)
      .set(auth(lecturer))
      .send({ note: 'Đồng ý, em nhớ xem lại bài giảng.' });

    expect(approved.status).toBe(200);
    expect(approved.body.leaveRequest.status).toBe('approved');
    expect(approved.body.leaveRequest.reviewerId).toBe('usr_gv01');
    expect(approved.body.excusedSessions).toBe(1);

    const record = ctx.db
      .prepare(`SELECT * FROM attendance_records WHERE session_id = 'ses_next_1' AND student_id = 'usr_sv01'`)
      .get() as any;
    expect(record.status).toBe('excused');
    expect(record.method).toBe('leave');
  });

  it('không ghi đè buổi sinh viên đã thực sự có mặt', async () => {
    const session = ctx.db.prepare(`SELECT * FROM class_sessions WHERE id = 'ses_open_now'`).get() as any;
    const qr = await request(ctx.app).get(`${API_PREFIX}/sessions/ses_open_now/qr`).set(auth(lecturer));
    await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(student))
      .send({ qr: qr.body.token, clientUuid: 'leave-test-0001' })
      .expect(201);

    const day = session.starts_at.slice(0, 10);
    const created = await request(ctx.app).post(`${API_PREFIX}/leave-requests`).set(auth(student)).send({
      classId: 'cls_it4409',
      type: 'sick',
      startDate: day,
      endDate: day,
      reason: 'Em thấy mệt nên xin phép nghỉ hôm nay.',
    });

    await request(ctx.app)
      .post(`${API_PREFIX}/leave-requests/${created.body.leaveRequest.id}/approve`)
      .set(auth(lecturer))
      .send({})
      .expect(200);

    const record = ctx.db
      .prepare(`SELECT status FROM attendance_records WHERE session_id = 'ses_open_now' AND student_id = 'usr_sv01'`)
      .get() as any;
    expect(record.status).toBe('present'); // điểm danh thật thắng đơn phép
  });

  it('từ chối đơn kèm lý do bắt buộc', async () => {
    const noNote = await request(ctx.app)
      .post(`${API_PREFIX}/leave-requests/lv_pending_1/reject`)
      .set(auth(lecturer))
      .send({});
    expect(noNote.status).toBe(400);

    const res = await request(ctx.app)
      .post(`${API_PREFIX}/leave-requests/lv_pending_1/reject`)
      .set(auth(lecturer))
      .send({ note: 'Em bổ sung giấy khám bệnh rồi nộp lại nhé.' });
    expect(res.status).toBe(200);
    expect(res.body.leaveRequest.status).toBe('rejected');
    expect(res.body.leaveRequest.reviewNote).toContain('giấy khám bệnh');
  });

  it('không duyệt lại đơn đã xử lý', async () => {
    await request(ctx.app).post(`${API_PREFIX}/leave-requests/lv_pending_1/approve`).set(auth(lecturer)).send({});
    const again = await request(ctx.app)
      .post(`${API_PREFIX}/leave-requests/lv_pending_1/approve`)
      .set(auth(lecturer))
      .send({});
    expect(again.status).toBe(409);
    expect(again.body.error.code).toBe('LEAVE_NOT_PENDING');
  });

  it('giảng viên không duyệt được đơn lớp khác', async () => {
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/leave-requests/lv_pending_3/approve`)
      .set(auth(lecturer))
      .send({});
    expect(res.status).toBe(403);
    expect(res.body.error.code).toBe('NOT_CLASS_OWNER');
  });

  it('sinh viên không tự duyệt đơn của mình', async () => {
    const created = await request(ctx.app).post(`${API_PREFIX}/leave-requests`).set(auth(student)).send({
      classId: 'cls_it4409',
      type: 'other',
      startDate: plusDays(9),
      endDate: plusDays(9),
      reason: 'Em có việc riêng cần xin phép.',
    });
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/leave-requests/${created.body.leaveRequest.id}/approve`)
      .set(auth(student))
      .send({});
    expect(res.status).toBe(403);
  });

  it('đơn nghỉ toàn bộ lớp phải do quản trị viên duyệt', async () => {
    const created = await request(ctx.app).post(`${API_PREFIX}/leave-requests`).set(auth(student)).send({
      classId: null,
      type: 'sick',
      startDate: plusDays(10),
      endDate: plusDays(12),
      reason: 'Em nhập viện phẫu thuật, xin nghỉ toàn bộ các lớp.',
    });
    expect(created.status).toBe(201);
    const id = created.body.leaveRequest.id;

    const byLecturer = await request(ctx.app)
      .post(`${API_PREFIX}/leave-requests/${id}/approve`)
      .set(auth(lecturer))
      .send({});
    expect(byLecturer.status).toBe(403);
    expect(byLecturer.body.error.code).toBe('REVIEW_NEEDS_ADMIN');

    const byAdmin = await request(ctx.app)
      .post(`${API_PREFIX}/leave-requests/${id}/approve`)
      .set(auth(admin))
      .send({ note: 'Phòng Đào tạo đã nhận hồ sơ bệnh án.' });
    expect(byAdmin.status).toBe(200);
    expect(byAdmin.body.leaveRequest.status).toBe('approved');
  });
});

describe('rút đơn', () => {
  it('sinh viên rút được đơn đang chờ duyệt', async () => {
    const created = await request(ctx.app).post(`${API_PREFIX}/leave-requests`).set(auth(student)).send({
      classId: 'cls_it4409',
      type: 'personal',
      startDate: plusDays(6),
      endDate: plusDays(6),
      reason: 'Em đăng ký nhầm ngày, sẽ nộp lại đơn khác.',
    });
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/leave-requests/${created.body.leaveRequest.id}/cancel`)
      .set(auth(student));
    expect(res.status).toBe(200);
    expect(res.body.leaveRequest.status).toBe('cancelled');
  });

  it('không rút được đơn của người khác', async () => {
    const other = await login(ctx.app, '2210002');
    const created = await request(ctx.app).post(`${API_PREFIX}/leave-requests`).set(auth(student)).send({
      classId: 'cls_it4409',
      type: 'personal',
      startDate: plusDays(7),
      endDate: plusDays(7),
      reason: 'Em có lịch khám sức khoẻ định kỳ.',
    });
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/leave-requests/${created.body.leaveRequest.id}/cancel`)
      .set(auth(other));
    expect(res.status).toBe(403);
  });
});
