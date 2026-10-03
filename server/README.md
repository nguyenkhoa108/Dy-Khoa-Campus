# Dy Khoa Campus — API tham chiếu

Hiện thực đầy đủ của [`docs/API_CONTRACT.md`](../docs/API_CONTRACT.md):
Express 5 + SQLite (better-sqlite3) + TypeScript.

Đây vừa là máy chủ chạy được để ứng dụng di động demo end-to-end, vừa là bản
đặc tả **thực thi được** của hợp đồng API cho nhóm web app đối chiếu.

## Chạy

```bash
cp .env.example .env
npm install
npm run seed     # dữ liệu mẫu, chạy lại được nhiều lần
npm start        # http://localhost:4000
npm run dev      # tự khởi động lại khi sửa mã
npm test         # 57 test
```

## Bố cục

```
src/
├── index.ts              Điểm vào: HTTP server + tác vụ dọn dẹp định kỳ
├── app.ts                Lắp ráp Express, CORS, router
├── config.ts             Đọc biến môi trường, chặn khởi động nếu production dùng khoá mẫu
├── seed.ts               Dữ liệu mẫu
├── lib/
│   ├── schema.sql        Lược đồ SQLite
│   ├── db.ts             Mở CSDL, sinh ID, ghi nhật ký thao tác
│   ├── qr.ts             Ký / kiểm tra mã QR, chống phát lại bằng nonce
│   ├── tokens.ts         JWT access + refresh, xoay vòng và phát hiện dùng lại
│   ├── attendance.ts     Quy tắc ghi nhận điểm danh (idempotent theo clientUuid)
│   ├── leave.ts          Áp dụng đơn phép đã duyệt lên bảng điểm danh
│   ├── access.ts         Kiểm tra quyền theo lớp học phần
│   ├── errors.ts         ApiError với mã lỗi ổn định
│   └── types.ts          Kiểu của các bảng
├── middleware/
│   ├── auth.ts           requireAuth, requireRole
│   └── errorHandler.ts   Chuyển mọi lỗi về đúng một hình dạng JSON
└── routes/
    ├── auth.ts           /auth/*
    ├── classes.ts        /classes, /sessions, mã QR buổi học
    ├── attendance.ts     /attendance/check-in, /attendance/sync, /me/qr, lịch sử
    └── leave.ts          /leave-requests/*
```

## Lưu ý vận hành

- **Khoá bí mật.** Khi `NODE_ENV=production`, server **từ chối khởi động** nếu
  `JWT_SECRET` hoặc `QR_SECRET` còn là giá trị mẫu hoặc ngắn hơn 32 ký tự. Hai
  khoá phải khác nhau.
- **Dọn dẹp.** Nonce QR và refresh token hết hạn được xoá mỗi 5 phút để bảng
  không phình vô hạn.
- **CSDL.** SQLite ở chế độ WAL, đủ cho quy mô một trường. Muốn đổi sang
  PostgreSQL thì `src/lib/schema.sql` và các câu truy vấn gần như giữ nguyên,
  chủ yếu đổi `datetime('now')` và cú pháp `ON CONFLICT`.
- **CORS.** Mặc định `*` cho tiện phát triển. Khi chạy thật hãy đặt
  `CORS_ORIGIN` về đúng origin của web app.

## Test

```
test/qr.test.ts           Ký, hết hạn, lệch đồng hồ, chống phát lại
test/auth.test.ts         Đăng nhập, xoay vòng refresh token, phát hiện dùng lại
test/attendance.test.ts   Cả hai chiều quét, idempotency, hàng đợi offline, phân quyền
test/leave.test.ts        Nộp, duyệt, từ chối, rút đơn và tác động lên điểm danh
```

Mỗi test chạy trên một CSDL trong bộ nhớ riêng, không đụng tới `data/campus.db`.
