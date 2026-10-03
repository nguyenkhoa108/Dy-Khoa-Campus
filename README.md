# Dy Khoa Campus — Ứng dụng di động

Ứng dụng di động cho trường Dy Khoa với hai chức năng chính:

- **Điểm danh bằng mã QR** — hai chiều quét: sinh viên quét mã giảng viên chiếu
  trên lớp, hoặc giảng viên quét mã QR cá nhân của sinh viên.
- **Phê duyệt đơn xin phép** — sinh viên nộp đơn, giảng viên duyệt hoặc từ chối
  ngay trên điện thoại; đơn được duyệt tự đánh dấu "nghỉ có phép" cho các buổi
  học trong khoảng ngày.

Dữ liệu dùng chung với Dy Khoa Campus web app qua một REST API được đặc tả đầy
đủ trong [`docs/API_CONTRACT.md`](docs/API_CONTRACT.md).

---

## Cấu trúc kho mã

```
.
├── mobile/     Ứng dụng React Native (Expo SDK 57, TypeScript)
├── server/     API tham chiếu — Express + SQLite, hiện thực đầy đủ hợp đồng API
└── docs/
    └── API_CONTRACT.md   Đặc tả API để web app khớp theo
```

`server/` tồn tại vì hai lý do: nó chạy được ngay nên app demo được end-to-end
mà không cần chờ web app, và nó là bản mô tả **thực thi được** của hợp đồng API
— nhóm web app có thể đối chiếu từng endpoint thay vì đoán theo tài liệu.

---

## Chạy thử trong 5 phút

Cần Node.js ≥ 20 và điện thoại cài [Expo Go](https://expo.dev/go), hoặc máy ảo
Android/iOS.

### 1. Khởi động API

```bash
cd server
cp .env.example .env
npm install
npm run seed      # nạp dữ liệu mẫu: 3 lớp, 5 sinh viên, 1 buổi đang mở điểm danh
npm start         # http://localhost:4000
```

### 2. Khởi động ứng dụng

```bash
cd mobile
npm install
npm start         # quét mã QR hiện ra bằng Expo Go
```

### 3. Trỏ app về đúng máy chủ

- **Máy ảo Android:** chạy được ngay (app tự đổi `localhost` → `10.0.2.2`).
- **Máy ảo iOS / web:** chạy được ngay với `localhost`.
- **Điện thoại thật:** điện thoại không hiểu `localhost` của máy tính. Mở app →
  tab **Cài đặt** → **Địa chỉ API** → nhập IP LAN của máy chạy server, ví dụ
  `http://192.168.1.10:4000/api/v1`. Lấy IP bằng `ipconfig` (Windows) hoặc
  `ifconfig | grep inet` (macOS/Linux).

Muốn đổi mặc định vĩnh viễn thì sửa `extra.apiBaseUrl` trong `mobile/app.json`.

### Tài khoản dùng thử

Mật khẩu chung: **`campus123`**

| Mã số | Vai trò | Họ tên | Dùng để thử |
|---|---|---|---|
| `2210001` | Sinh viên | Phạm Hoàng An | Quét mã điểm danh, nộp đơn xin phép |
| `2210002` | Sinh viên | Lê Thanh Bình | Đã có sẵn một đơn chờ duyệt |
| `GV001` | Giảng viên | TS. Nguyễn Thị Lan | Chiếu mã QR, duyệt đơn (lớp IT4409, IT3100) |
| `GV002` | Giảng viên | ThS. Trần Văn Minh | Lớp IT4785 |
| `AD001` | Quản trị | Phòng Đào tạo | Duyệt đơn nghỉ toàn bộ lớp |

Đăng nhập được bằng mã số hoặc email (`an.pham@sv.dykhoa.edu.vn`…).

### Thử luồng điểm danh mà chỉ có một máy

Cần hai "màn hình" để quét. Cách nhanh nhất là mở Expo Go trên điện thoại (đăng
nhập `GV001`, vào buổi đang mở → **Chiếu mã QR**) rồi dùng một điện thoại thứ
hai đăng nhập `2210001` để quét. Nếu chỉ có một máy, đăng nhập `GV001`, mở
**Quét SV**, và chiếu mã QR cá nhân của sinh viên từ trình duyệt — hoặc chạy
`server/` rồi gọi API trực tiếp như trong `docs/API_CONTRACT.md`.

---

## Chức năng theo vai trò

### Sinh viên

| Màn hình | Nội dung |
|---|---|
| Trang chủ | Buổi đang mở điểm danh, tỷ lệ chuyên cần, đơn phép gần đây |
| Quét QR | Camera quét mã buổi học, phản hồi rung + hộp kết quả lớn |
| Mã của tôi | Mã QR cá nhân tự xoay vòng, kèm đồng hồ đếm ngược |
| Lịch sử | Toàn bộ bản ghi điểm danh, lọc theo lớp, thống kê 4 trạng thái |
| Xin phép | Nộp đơn (chọn lớp, loại nghỉ, khoảng ngày, lý do), xem và rút đơn |
| Cài đặt | Hàng đợi offline, địa chỉ máy chủ, đăng xuất |

### Giảng viên

| Màn hình | Nội dung |
|---|---|
| Lớp học | Lớp phụ trách, buổi đang mở, cảnh báo số đơn chờ duyệt |
| Buổi học | Danh sách buổi, nút **Mở buổi điểm danh ngay** tạo và mở buổi trong một chạm |
| Chiếu mã QR | Mã lớn cho cả lớp quét, đếm sĩ số đã điểm danh cập nhật mỗi 5 giây |
| Quét SV | Quét mã cá nhân từng sinh viên, nhật ký các lượt vừa quét |
| Danh sách điểm danh | Toàn bộ sĩ số, sửa tay từng người, đóng buổi (tự tính vắng) |
| Duyệt phép | Lọc theo trạng thái, duyệt hoặc từ chối kèm lý do; chấm đỏ số đơn chờ |

---

## Những điểm thiết kế đáng chú ý

### Mã QR không gian lận được bằng ảnh chụp màn hình

Mã do **máy chủ ký** bằng HMAC-SHA256 (khoá riêng, khác khoá JWT), **hết hạn sau
30–60 giây** và **tự xoay vòng** trước khi hết hạn, và mỗi mã chỉ **dùng được
một lần cho mỗi sinh viên** (nonce). Ảnh chụp màn hình gửi cho bạn gần như vô
dụng. Chi tiết và giới hạn còn lại nằm ở mục 3 của
[`docs/API_CONTRACT.md`](docs/API_CONTRACT.md).

### Mất sóng giảng đường không làm hỏng buổi điểm danh

Giảng đường hay sóng yếu. Mỗi lượt quét được ghi xuống máy trước; khi mất mạng
app xếp vào hàng đợi cục bộ và tự gửi lên khi có sóng trở lại. Mỗi lượt mang một
`clientUuid`, nên gửi lại bao nhiêu lần cũng chỉ sinh **một** bản ghi điểm danh.
Giờ quét thật được giữ nguyên, nên bản ghi đồng bộ muộn vẫn tính đúng "có mặt"
hay "đi muộn".

### Đơn phép không ghi đè dữ liệu điểm danh thật

Duyệt đơn đánh dấu `excused` cho các buổi trong khoảng ngày, nhưng buổi nào sinh
viên đã thực sự quét mã thì giữ nguyên `present` / `late`.

### Luôn có lối thoát thủ công

Điện thoại hết pin, camera hỏng, mã không đọc được — giảng viên vẫn điểm danh
tay từng sinh viên trong màn hình danh sách, bản ghi được đánh dấu
`method = "manual"` để đối soát sau.

---

## Phát triển

```bash
# API
cd server
npm run dev        # tự khởi động lại khi sửa mã
npm test           # 57 test cho QR, điểm danh, đơn phép, xác thực
npm run typecheck

# Ứng dụng
cd mobile
npm start
npm run typecheck
npx expo export --platform android   # kiểm tra đóng gói Metro
```

### Biến môi trường của server

Xem [`server/.env.example`](server/.env.example). Hai biến bắt buộc đổi khi chạy
thật:

| Biến | Mặc định | Ghi chú |
|---|---|---|
| `JWT_SECRET` | giá trị mẫu | Ký access token. Khi `NODE_ENV=production` phải ≥ 32 ký tự và khác giá trị mẫu, nếu không server từ chối khởi động |
| `QR_SECRET` | giá trị mẫu | Ký payload mã QR. **Phải khác** `JWT_SECRET` |

Các biến còn lại (`SESSION_QR_TTL_SEC`, `STUDENT_QR_TTL_SEC`,
`QR_CLOCK_SKEW_SEC`, `CORS_ORIGIN`…) đều có mặc định hợp lý.

---

## Đóng gói bản cài đặt

```bash
cd mobile
npx eas build --platform android --profile preview   # APK để phát cho sinh viên thử
npx eas build --platform ios --profile preview
```

Trước khi build, đặt `extra.apiBaseUrl` trong `app.json` về địa chỉ thật của web
app (dùng HTTPS). Android chặn HTTP không mã hoá từ Android 9 trở lên, nên bản
phát hành bắt buộc dùng HTTPS.

---

## Tích hợp với web app

App không ràng buộc vào `server/`. Để chuyển sang dùng dữ liệu của web app:

1. Web app hiện thực các endpoint trong
   [`docs/API_CONTRACT.md`](docs/API_CONTRACT.md) — chú ý danh sách kiểm tra ở
   mục 7.
2. Đổi `extra.apiBaseUrl` trong `mobile/app.json`.
3. Chạy lại `npm test` ở `server/` như bộ test đối chiếu hành vi: mọi khẳng định
   trong đó là hành vi mà app trông đợi.

Hướng ngược lại cũng được: giữ `server/` làm dịch vụ điểm danh độc lập và cho
web app đọc chung cơ sở dữ liệu, hoặc gọi sang qua chính các endpoint này.

---

## Những việc còn bỏ ngỏ

Các hạng mục sau nằm ngoài phạm vi lần triển khai này, ghi lại để khỏi quên:

- **Thông báo đẩy** khi đơn phép được duyệt hoặc khi buổi học mở điểm danh.
  Cần `expo-notifications` và một bảng lưu push token.
- **Đính kèm minh chứng** cho đơn xin phép (`attachmentUrl` đã có trong lược đồ
  và API nhưng app chưa có màn hình tải ảnh lên).
- **Chống gian lận theo vị trí** (geofence hoặc BLE beacon) — xem phần giới hạn
  ở mục 3 của hợp đồng API.
- **Xác thực SSO của trường** thay cho email/mật khẩu.
- **Kiểm thử giao diện** cho các màn hình app; hiện mới có 57 test ở tầng API và
  kiểm tra đóng gói Metro.
