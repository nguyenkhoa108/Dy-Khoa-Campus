# Dy Khoa Campus — Ứng dụng di động

React Native trên Expo SDK 57, TypeScript. Xem [README gốc](../README.md) để
biết cách chạy nhanh và tài khoản dùng thử.

## Bố cục

```
App.tsx                   Lắp các Provider và bộ điều hướng
src/
├── config.ts             Địa chỉ API (app.json → ghi đè được trong Cài đặt)
├── theme.ts              Màu, khoảng cách, kiểu chữ dùng chung
├── api/
│   ├── client.ts         fetch có timeout, tự làm mới access token khi gặp 401
│   ├── endpoints.ts      Toàn bộ lời gọi API, gom một chỗ
│   └── types.ts          Kiểu dữ liệu khớp với hợp đồng API
├── state/
│   ├── AuthContext.tsx      Phiên đăng nhập, token lưu trong SecureStore
│   ├── ScanQueueContext.tsx Hàng đợi quét offline, tự đồng bộ khi có mạng
│   └── useCheckIn.ts        Logic chung cho mọi màn hình quét
├── components/
│   ├── ui.tsx               Thư viện thành phần dùng chung
│   ├── QrScanner.tsx        Camera + khung ngắm + đèn pin + chống quét trùng
│   ├── RotatingQr.tsx       Mã QR tự làm mới kèm đếm ngược
│   ├── ScanResultSheet.tsx  Hộp kết quả sau mỗi lượt quét
│   └── OfflineBanner.tsx    Dải cảnh báo mất mạng / còn lượt chờ gửi
├── navigation/
│   └── RootNavigator.tsx    Điều hướng theo vai trò
├── screens/
│   ├── LoginScreen.tsx
│   ├── SettingsScreen.tsx
│   ├── student/          Trang chủ, Quét QR, Mã của tôi, Lịch sử, Xin phép
│   └── lecturer/         Lớp học, Buổi học, Chiếu QR, Quét SV, Danh sách, Duyệt phép
└── utils/
    ├── datetime.ts       Định dạng ngày giờ tiếng Việt
    ├── labels.ts         Nhãn và màu cho các trạng thái
    └── device.ts         Mã thiết bị ổn định, sinh UUID cho mỗi lượt quét
```

## Vài điểm khi đọc mã

- **Token.** Giữ trong `useRef` của `AuthContext` để `api/client.ts` đọc được
  đồng bộ, không phụ thuộc vòng render. Lưu lâu dài bằng `expo-secure-store`.
- **Làm mới token.** Nhiều màn hình có thể cùng gặp 401 một lúc; `client.ts` gom
  chúng vào **một** lượt refresh rồi thử lại từng request đúng một lần.
- **Quét trùng.** `QrScanner` bỏ qua cùng một mã trong 2 giây và khoá camera
  trong lúc đang gửi request, nên một lần giơ máy không bắn ra nhiều lượt.
- **Hàng đợi offline.** `ScanQueueContext` ghi xuống `AsyncStorage`, lắng nghe
  `NetInfo` và tự gửi khi có mạng. Lỗi 4xx bị loại khỏi hàng đợi (không thể thử
  lại thành công), lỗi 5xx và lỗi mạng thì giữ lại.
- **Xoay vòng mã QR.** `RotatingQr` xin mã mới sau `refreshAfterSec` giây — mốc
  do máy chủ trả về — nên màn hình không bao giờ hiện mã đã chết.

## Lệnh

```bash
npm start                            # Expo dev server
npm run android / ios / web
npm run typecheck
npx expo export --platform android   # kiểm tra đóng gói Metro
```

## Quyền

Chỉ dùng **camera**, và chỉ để đọc mã QR — app không chụp, không lưu, không gửi
hình ảnh đi đâu. Chuỗi giải thích quyền nằm ở `app.json`
(`NSCameraUsageDescription` và plugin `expo-camera`).
