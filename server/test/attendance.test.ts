import { beforeEach, describe, expect, it } from 'vitest';
import request from 'supertest';
import { API_PREFIX, auth, bootstrap, login, type TestContext } from './helpers.js';

let ctx: TestContext;
let lecturer: string;
let student: string;

const OPEN_SESSION = 'ses_open_now'; // IT4409, đang mở điểm danh trong dữ liệu mẫu

beforeEach(async () => {
  ctx = bootstrap();
  lecturer = await login(ctx.app, 'GV001');
  student = await login(ctx.app, '2210001');
});

async function sessionQr(token = lecturer, sessionId = OPEN_SESSION): Promise<string> {
  const res = await request(ctx.app).get(`${API_PREFIX}/sessions/${sessionId}/qr`).set(auth(token));
  expect(res.status).toBe(200);
  return res.body.token as string;
}

async function studentQr(token = student): Promise<string> {
  const res = await request(ctx.app).get(`${API_PREFIX}/me/qr`).set(auth(token));
  expect(res.status).toBe(200);
  return res.body.token as string;
}

describe('cấp mã QR', () => {
  it('chỉ giảng viên phụ trách lấy được mã của buổi học', async () => {
    const other = await login(ctx.app, 'GV002');
    const res = await request(ctx.app).get(`${API_PREFIX}/sessions/${OPEN_SESSION}/qr`).set(auth(other));
    expect(res.status).toBe(403);
    expect(res.body.error.code).toBe('NOT_CLASS_OWNER');
  });

  it('không cấp mã khi buổi học chưa mở điểm danh', async () => {
    const res = await request(ctx.app).get(`${API_PREFIX}/sessions/ses_prev_1/qr`).set(auth(lecturer));
    expect(res.status).toBe(409);
    expect(res.body.error.code).toBe('SESSION_CLOSED');
  });

  it('mỗi lần gọi trả về một mã khác nhau (xoay vòng)', async () => {
    expect(await sessionQr()).not.toBe(await sessionQr());
  });

  it('giảng viên không có mã QR cá nhân', async () => {
    const res = await request(ctx.app).get(`${API_PREFIX}/me/qr`).set(auth(lecturer));
    expect(res.status).toBe(403);
    expect(res.body.error.code).toBe('STUDENT_ONLY');
  });
});

describe('điểm danh: sinh viên quét mã buổi học', () => {
  it('ghi nhận có mặt', async () => {
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(student))
      .send({ qr: await sessionQr(), clientUuid: 'scan-0000-0001' });

    expect(res.status).toBe(201);
    expect(res.body.duplicate).toBe(false);
    expect(res.body.record.status).toBe('present');
    expect(res.body.record.method).toBe('qr_session');
    expect(res.body.student.code).toBe('2210001');
  });

  it('chặn dùng lại cùng một mã (ảnh chụp màn hình)', async () => {
    const qr = await sessionQr();
    const first = await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(student))
      .send({ qr, clientUuid: 'scan-0000-0002' });
    expect(first.status).toBe(201);

    const replay = await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(student))
      .send({ qr, clientUuid: 'scan-0000-0003' });
    expect(replay.status).toBe(409);
    expect(replay.body.error.code).toBe('QR_ALREADY_USED');
  });

  it('cùng clientUuid gửi lại nhiều lần chỉ tạo một bản ghi', async () => {
    const body = { qr: await sessionQr(), clientUuid: 'scan-0000-0004' };
    const first = await request(ctx.app).post(`${API_PREFIX}/attendance/check-in`).set(auth(student)).send(body);
    const again = await request(ctx.app).post(`${API_PREFIX}/attendance/check-in`).set(auth(student)).send(body);

    expect(first.status).toBe(201);
    expect(again.status).toBe(200);
    expect(again.body.duplicate).toBe(true);
    expect(again.body.record.id).toBe(first.body.record.id);

    const count = ctx.db
      .prepare(`SELECT COUNT(*) AS n FROM attendance_records WHERE session_id = ? AND student_id = 'usr_sv01'`)
      .get(OPEN_SESSION) as { n: number };
    expect(count.n).toBe(1);
  });

  it('từ chối mã bị sửa chữ ký', async () => {
    const qr = await sessionQr();
    const tampered = `${qr.slice(0, -4)}AAAA`;
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(student))
      .send({ qr: tampered, clientUuid: 'scan-0000-0005' });
    expect(res.status).toBe(400);
    expect(['QR_SIGNATURE_INVALID', 'QR_MALFORMED']).toContain(res.body.error.code);
  });

  it('từ chối chuỗi QR lạ không thuộc hệ thống', async () => {
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(student))
      .send({ qr: 'https://example.com/khong-phai-ma-cua-truong', clientUuid: 'scan-0000-0006' });
    expect(res.status).toBe(400);
    expect(res.body.error.code).toBe('QR_MALFORMED');
  });

  it('từ chối sinh viên không đăng ký lớp', async () => {
    const outsider = await login(ctx.app, '2210003'); // không học IT4785
    const gv2 = await login(ctx.app, 'GV002');
    await request(ctx.app).post(`${API_PREFIX}/sessions/ses_today_pm/open`).set(auth(gv2)).expect(200);

    const res = await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(outsider))
      .send({ qr: await sessionQr(gv2, 'ses_today_pm'), clientUuid: 'scan-0000-0007' });
    expect(res.status).toBe(403);
    expect(res.body.error.code).toBe('NOT_ENROLLED');
  });

  it('từ chối khi buổi học đã đóng điểm danh', async () => {
    const qr = await sessionQr();
    await request(ctx.app).post(`${API_PREFIX}/sessions/${OPEN_SESSION}/close`).set(auth(lecturer)).expect(200);

    const res = await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(student))
      .send({ qr, clientUuid: 'scan-0000-0008' });
    expect(res.status).toBe(409);
    expect(res.body.error.code).toBe('SESSION_CLOSED');
  });

  it('giảng viên không quét được mã buổi học thay sinh viên', async () => {
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(lecturer))
      .send({ qr: await sessionQr(), clientUuid: 'scan-0000-0009' });
    expect(res.status).toBe(403);
    expect(res.body.error.code).toBe('SESSION_QR_STUDENT_ONLY');
  });
});

describe('điểm danh: giảng viên quét mã sinh viên', () => {
  it('ghi nhận có mặt cho đúng sinh viên', async () => {
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(lecturer))
      .send({ qr: await studentQr(), sessionId: OPEN_SESSION, clientUuid: 'scan-0001-0001' });

    expect(res.status).toBe(201);
    expect(res.body.record.method).toBe('qr_student');
    expect(res.body.student.code).toBe('2210001');
    expect(res.body.record.recordedBy).toBe('usr_gv01');
  });

  it('bắt buộc chọn buổi học trước khi quét', async () => {
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(lecturer))
      .send({ qr: await studentQr(), clientUuid: 'scan-0001-0002' });
    expect(res.status).toBe(400);
    expect(res.body.error.code).toBe('SESSION_ID_REQUIRED');
  });

  it('sinh viên không quét được mã của sinh viên khác', async () => {
    const other = await login(ctx.app, '2210002');
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(other))
      .send({ qr: await studentQr(), sessionId: OPEN_SESSION, clientUuid: 'scan-0001-0003' });
    expect(res.status).toBe(403);
    expect(res.body.error.code).toBe('STUDENT_QR_STAFF_ONLY');
  });

  it('giảng viên khác không điểm danh hộ lớp không phụ trách', async () => {
    const gv2 = await login(ctx.app, 'GV002');
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(gv2))
      .send({ qr: await studentQr(), sessionId: OPEN_SESSION, clientUuid: 'scan-0001-0004' });
    expect(res.status).toBe(403);
    expect(res.body.error.code).toBe('NOT_CLASS_OWNER');
  });
});

describe('đồng bộ hàng đợi offline', () => {
  it('xử lý từng mục độc lập và bỏ qua mục trùng', async () => {
    const qrA = await studentQr(student);
    const qrB = await studentQr(await login(ctx.app, '2210002'));

    const payload = {
      items: [
        { qr: qrA, sessionId: OPEN_SESSION, clientUuid: 'offline-0001', scannedAt: new Date().toISOString() },
        { qr: qrB, sessionId: OPEN_SESSION, clientUuid: 'offline-0002', scannedAt: new Date().toISOString() },
        { qr: 'rac-khong-doc-duoc', sessionId: OPEN_SESSION, clientUuid: 'offline-0003' },
      ],
    };

    const res = await request(ctx.app).post(`${API_PREFIX}/attendance/sync`).set(auth(lecturer)).send(payload);
    expect(res.status).toBe(200);
    expect(res.body.accepted).toBe(2);
    expect(res.body.rejected).toBe(1);

    const failure = res.body.results.find((r: any) => r.clientUuid === 'offline-0003');
    expect(failure.ok).toBe(false);
    expect(failure.retryable).toBe(false); // lỗi 4xx: app phải bỏ khỏi hàng đợi

    // Gửi lại toàn bộ lô: không sinh thêm bản ghi nào.
    const retry = await request(ctx.app).post(`${API_PREFIX}/attendance/sync`).set(auth(lecturer)).send(payload);
    expect(retry.body.results.filter((r: any) => r.duplicate).length).toBe(2);

    const total = ctx.db
      .prepare(`SELECT COUNT(*) AS n FROM attendance_records WHERE session_id = ?`)
      .get(OPEN_SESSION) as { n: number };
    expect(total.n).toBe(2);
  });

  it('giữ nguyên giờ quét gốc để tính đi muộn đúng', async () => {
    const session = ctx.db.prepare(`SELECT * FROM class_sessions WHERE id = ?`).get(OPEN_SESSION) as any;
    const lateAt = new Date(new Date(session.starts_at).getTime() + 45 * 60_000).toISOString();

    const res = await request(ctx.app)
      .post(`${API_PREFIX}/attendance/sync`)
      .set(auth(lecturer))
      .send({ items: [{ qr: await studentQr(), sessionId: OPEN_SESSION, clientUuid: 'offline-late-1', scannedAt: lateAt }] });

    expect(res.body.results[0].record.status).toBe('late');
    expect(res.body.results[0].record.checkedInAt).toBe(lateAt);
  });
});

describe('bảng điểm danh và lịch sử', () => {
  it('giảng viên xem được sĩ số và thống kê buổi học', async () => {
    await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(student))
      .send({ qr: await sessionQr(), clientUuid: 'scan-0002-0001' });

    const res = await request(ctx.app).get(`${API_PREFIX}/sessions/${OPEN_SESSION}/attendance`).set(auth(lecturer));
    expect(res.status).toBe(200);
    expect(res.body.summary.total).toBe(5);
    expect(res.body.summary.present).toBe(1);
    expect(res.body.summary.pending).toBe(4);
    expect(res.body.items).toHaveLength(5);
  });

  it('đóng điểm danh thì những người chưa quét bị tính vắng', async () => {
    await request(ctx.app)
      .post(`${API_PREFIX}/attendance/check-in`)
      .set(auth(student))
      .send({ qr: await sessionQr(), clientUuid: 'scan-0002-0002' });

    const res = await request(ctx.app).post(`${API_PREFIX}/sessions/${OPEN_SESSION}/close`).set(auth(lecturer));
    expect(res.status).toBe(200);
    expect(res.body.markedAbsent).toBe(4);
    expect(res.body.session.checkinState).toBe('closed');
  });

  it('sinh viên chỉ thấy bản ghi của chính mình trong bảng điểm danh', async () => {
    const res = await request(ctx.app).get(`${API_PREFIX}/sessions/${OPEN_SESSION}/attendance`).set(auth(student));
    expect(res.status).toBe(200);
    expect(res.body.summary).toBeNull();
    expect(res.body.items).toHaveLength(0);
  });

  it('lịch sử điểm danh kèm thống kê', async () => {
    const res = await request(ctx.app).get(`${API_PREFIX}/attendance/history`).set(auth(student));
    expect(res.status).toBe(200);
    expect(res.body.studentId).toBe('usr_sv01');
    expect(res.body.summary.present).toBe(2);
    expect(res.body.items[0].session.classCode).toBeTruthy();
  });

  it('sinh viên không xem được lịch sử của người khác', async () => {
    const res = await request(ctx.app)
      .get(`${API_PREFIX}/attendance/history?studentId=usr_sv02`)
      .set(auth(student));
    expect(res.status).toBe(403);
  });

  it('giảng viên xem được lịch sử sinh viên lớp mình', async () => {
    const res = await request(ctx.app)
      .get(`${API_PREFIX}/attendance/history?studentId=usr_sv01`)
      .set(auth(lecturer));
    expect(res.status).toBe(200);
  });
});
