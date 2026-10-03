import { beforeEach, describe, expect, it } from 'vitest';
import request from 'supertest';
import { API_PREFIX, SEED_PASSWORD, auth, bootstrap, login, type TestContext } from './helpers.js';

let ctx: TestContext;
beforeEach(() => {
  ctx = bootstrap();
});

describe('xác thực', () => {
  it('đăng nhập bằng email hoặc mã số đều được', async () => {
    for (const identifier of ['an.pham@sv.dykhoa.edu.vn', '2210001']) {
      const res = await request(ctx.app)
        .post(`${API_PREFIX}/auth/login`)
        .send({ identifier, password: SEED_PASSWORD, deviceId: 'test-device' });
      expect(res.status).toBe(200);
      expect(res.body.user.code).toBe('2210001');
      expect(res.body.user).not.toHaveProperty('password_hash');
      expect(res.body.accessToken).toBeTruthy();
      expect(res.body.refreshToken).toBeTruthy();
    }
  });

  it('từ chối sai mật khẩu bằng mã lỗi ổn định', async () => {
    const res = await request(ctx.app)
      .post(`${API_PREFIX}/auth/login`)
      .send({ identifier: '2210001', password: 'sai-mat-khau' });
    expect(res.status).toBe(401);
    expect(res.body.error.code).toBe('CREDENTIALS_INVALID');
  });

  it('chặn truy cập khi thiếu access token', async () => {
    const res = await request(ctx.app).get(`${API_PREFIX}/auth/me`);
    expect(res.status).toBe(401);
    expect(res.body.error.code).toBe('AUTH_REQUIRED');
  });

  it('xoay vòng refresh token và thu hồi toàn bộ phiên khi token cũ bị dùng lại', async () => {
    const first = await request(ctx.app)
      .post(`${API_PREFIX}/auth/login`)
      .send({ identifier: '2210001', password: SEED_PASSWORD });
    const oldRefresh = first.body.refreshToken as string;

    const rotated = await request(ctx.app).post(`${API_PREFIX}/auth/refresh`).send({ refreshToken: oldRefresh });
    expect(rotated.status).toBe(200);
    expect(rotated.body.refreshToken).not.toBe(oldRefresh);

    const replay = await request(ctx.app).post(`${API_PREFIX}/auth/refresh`).send({ refreshToken: oldRefresh });
    expect(replay.status).toBe(401);
    expect(replay.body.error.code).toBe('REFRESH_REUSED');

    // Token mới cũng bị thu hồi theo, buộc đăng nhập lại.
    const after = await request(ctx.app)
      .post(`${API_PREFIX}/auth/refresh`)
      .send({ refreshToken: rotated.body.refreshToken });
    expect(after.status).toBe(401);
  });

  it('/auth/me trả về lớp theo đúng vai trò', async () => {
    const student = await login(ctx.app, '2210001');
    const sv = await request(ctx.app).get(`${API_PREFIX}/auth/me`).set(auth(student));
    expect(sv.body.user.role).toBe('student');
    expect(sv.body.classes.map((c: any) => c.code).sort()).toEqual(['IT3100', 'IT4409', 'IT4785']);

    const lecturer = await login(ctx.app, 'GV001');
    const gv = await request(ctx.app).get(`${API_PREFIX}/auth/me`).set(auth(lecturer));
    expect(gv.body.user.role).toBe('lecturer');
    expect(gv.body.classes.map((c: any) => c.code).sort()).toEqual(['IT3100', 'IT4409']);
  });
});
