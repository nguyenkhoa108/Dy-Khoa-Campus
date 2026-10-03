# Hợp đồng API — Dy Khoa Campus

Tài liệu này mô tả **chính xác** các endpoint mà ứng dụng di động Dy Khoa Campus
gọi tới. Thư mục [`server/`](../server) là bản hiện thực tham chiếu đầy đủ của
hợp đồng này.

> **Dành cho nhóm web app:** để app di động dùng chung dữ liệu với web app đang
> triển khai, web app chỉ cần phơi ra đúng những endpoint dưới đây (cùng đường
> dẫn, cùng hình dạng JSON, cùng mã lỗi). Khi đó đổi `extra.apiBaseUrl` trong
> `mobile/app.json` sang địa chỉ của web app là app chạy ngay, không phải sửa
> dòng mã nào. Nếu muốn đi đường ngược lại, hãy chạy `server/` làm dịch vụ
> điểm danh riêng và cho web app đọc chung cơ sở dữ liệu.

- Base URL: `{host}/api/v1`
- Mọi request/response đều là `application/json; charset=utf-8`
- Mọi mốc thời gian là chuỗi ISO 8601 có offset (`2026-10-03T07:00:00.000Z`)
- Mọi ngày (không kèm giờ) là `YYYY-MM-DD`

---

## 1. Quy ước chung

### Xác thực

Trừ `POST /auth/login`, `POST /auth/refresh` và `POST /auth/logout`, mọi endpoint
đều yêu cầu header:

```
Authorization: Bearer <accessToken>
```

### Hình dạng lỗi

Mọi lỗi trả về đúng một hình dạng. App bắt theo `code`, **không** bắt theo
`message` (thông điệp có thể đổi lời văn bất cứ lúc nào).

```json
{
  "error": {
    "code": "QR_EXPIRED",
    "message": "Mã QR đã hết hạn, vui lòng quét lại mã mới nhất",
    "details": { "sessionId": "ses_abc" }
  }
}
```

`details` là tuỳ chọn.

### Bảng mã lỗi

| Mã | HTTP | Ý nghĩa | App xử lý thế nào |
|---|---|---|---|
| `AUTH_REQUIRED` | 401 | Thiếu header `Authorization` | Đăng xuất |
| `TOKEN_EXPIRED` | 401 | Access token hết hạn | Gọi `/auth/refresh` rồi thử lại **một lần** |
| `TOKEN_INVALID` | 401 | Access token sai | Gọi `/auth/refresh` rồi thử lại một lần |
| `REFRESH_INVALID` | 401 | Refresh token không tồn tại | Đăng xuất |
| `REFRESH_EXPIRED` | 401 | Refresh token hết hạn | Đăng xuất |
| `REFRESH_REUSED` | 401 | Token cũ bị dùng lại — mọi phiên đã bị thu hồi | Đăng xuất, báo người dùng đăng nhập lại |
| `CREDENTIALS_INVALID` | 401 | Sai tài khoản/mật khẩu | Hiện lỗi tại form đăng nhập |
| `ACCOUNT_DISABLED` | 401/403 | Tài khoản bị khoá | Đăng xuất |
| `ROLE_FORBIDDEN` | 403 | Vai trò không được phép | Ẩn chức năng |
| `NOT_CLASS_OWNER` | 403 | Không phụ trách lớp học phần | Hiện lỗi |
| `NOT_ENROLLED` | 403 | Sinh viên không thuộc lớp | Hiện lỗi |
| `STUDENT_FORBIDDEN` | 403 | Không được xem dữ liệu sinh viên khác | Hiện lỗi |
| `SESSION_QR_STUDENT_ONLY` | 403 | Mã buổi học chỉ sinh viên quét | Hiện lỗi |
| `STUDENT_QR_STAFF_ONLY` | 403 | Mã sinh viên chỉ giảng viên quét | Hiện lỗi |
| `REVIEW_NEEDS_ADMIN` | 403 | Đơn nghỉ toàn bộ lớp cần quản trị duyệt | Hiện lỗi |
| `SESSION_NOT_FOUND` | 404 | Buổi học không tồn tại | Hiện lỗi |
| `LEAVE_NOT_FOUND` | 404 | Đơn không tồn tại | Hiện lỗi |
| `QR_MALFORMED` | 400 | Chuỗi QR không thuộc hệ thống | "Đây không phải mã của trường" |
| `QR_SIGNATURE_INVALID` | 400 | Chữ ký sai (mã bị sửa / giả) | "Mã QR không hợp lệ" |
| `QR_EXPIRED` | 400 | Mã đã hết hạn | "Hãy quét mã mới nhất" |
| `QR_NOT_YET_VALID` | 400 | Đồng hồ thiết bị lệch quá nhiều | "Kiểm tra giờ trên máy" |
| `QR_VERSION_UNSUPPORTED` | 400 | App quá cũ | Nhắc cập nhật ứng dụng |
| `SESSION_ID_REQUIRED` | 400 | Quét mã SV nhưng chưa chọn buổi | Bắt chọn buổi trước |
| `DATE_RANGE_INVALID` | 400 | Ngày kết thúc trước ngày bắt đầu | Hiện lỗi tại form |
| `VALIDATION_FAILED` | 400 | Dữ liệu gửi lên sai định dạng | Hiện lỗi tại form, đọc `details[]` |
| `QR_ALREADY_USED` | 409 | Nonce đã bị tiêu thụ (phát lại) | "Hãy quét mã mới nhất" |
| `SESSION_CLOSED` | 409 | Buổi chưa mở hoặc đã đóng điểm danh | Hiện lỗi |
| `LEAVE_OVERLAPPING` | 409 | Đã có đơn chờ duyệt trùng ngày | Hiện lỗi |
| `LEAVE_NOT_PENDING` | 409 | Đơn đã được xử lý | Tải lại danh sách |
| `INTERNAL_ERROR` | 500 | Lỗi hệ thống | Cho thử lại |

---

## 2. Xác thực

### `POST /auth/login`

```jsonc
// Request
{ "identifier": "2210001", "password": "…", "deviceId": "android-a1b2c3" }
```

`identifier` nhận **email hoặc mã số** (MSSV / mã giảng viên), không phân biệt
hoa thường. `deviceId` là tuỳ chọn nhưng nên gửi: mỗi thiết bị có một chuỗi
refresh token riêng, nhờ đó thu hồi được từng máy.

```jsonc
// 200
{
  "accessToken": "eyJhbGciOi…",
  "refreshToken": "9xK2…",
  "tokenType": "Bearer",
  "expiresIn": 900,
  "refreshExpiresAt": "2026-11-02T13:00:00.000Z",
  "user": {
    "id": "usr_sv01", "code": "2210001", "email": "an.pham@sv.dykhoa.edu.vn",
    "fullName": "Phạm Hoàng An", "role": "student",
    "faculty": "Công nghệ thông tin", "avatarUrl": null
  }
}
```

`role` ∈ `student` | `lecturer` | `admin`.

### `POST /auth/refresh`

```jsonc
// Request
{ "refreshToken": "9xK2…" }
```

Trả về **đúng hình dạng của `/auth/login`**, với cả `accessToken` và
`refreshToken` mới.

**Bắt buộc xoay vòng token:** refresh token cũ phải bị thu hồi ngay. Nếu một
token đã thu hồi được gửi lại (dấu hiệu token bị đánh cắp), máy chủ phải thu hồi
**toàn bộ** phiên của người dùng đó và trả `REFRESH_REUSED`.

### `POST /auth/logout`

```jsonc
// Request
{ "refreshToken": "9xK2…" }
// 200
{ "ok": true }
```

### `GET /auth/me`

```jsonc
// 200
{
  "user": { /* như trên */ },
  "classes": [
    { "id": "cls_it4409", "code": "IT4409", "name": "Công nghệ Web…",
      "term": "2026.1", "room": "D9-301", "lecturerName": "TS. Nguyễn Thị Lan" }
  ]
}
```

Sinh viên nhận các lớp **đã đăng ký**; giảng viên nhận các lớp **phụ trách**.

### `POST /auth/change-password`

```jsonc
{ "currentPassword": "…", "newPassword": "…" }   // newPassword ≥ 8 ký tự
```

Đổi mật khẩu phải thu hồi mọi refresh token của người dùng đó.

---

## 3. Định dạng mã QR

Đây là phần quan trọng nhất cần khớp đúng nếu web app tự hiện thực.

```
DKC1.<base64url(payload JSON)>.<base64url(HMAC-SHA256)>
```

- `HMAC-SHA256` tính trên chuỗi `"DKC1." + <base64url(payload)>`, khoá là
  `QR_SECRET` (phải khác `JWT_SECRET`).
- So sánh chữ ký phải dùng hàm so sánh thời gian cố định (`timingSafeEqual`).

Payload mã **buổi học** (giảng viên chiếu, sinh viên quét):

```jsonc
{ "v": 1, "t": "S", "sid": "ses_open_now", "n": "f3Kd9xQm2", "iat": 1790000000, "exp": 1790000030 }
```

Payload mã **sinh viên** (sinh viên mở, giảng viên quét):

```jsonc
{ "v": 1, "t": "U", "uid": "usr_sv01", "n": "a8Lp0zRt4", "iat": 1790000000, "exp": 1790000060 }
```

| Trường | Ý nghĩa |
|---|---|
| `v` | Phiên bản định dạng, hiện là `1`. Khác → `QR_VERSION_UNSUPPORTED` |
| `t` | `S` = buổi học, `U` = sinh viên |
| `sid` / `uid` | Mã buổi học / mã người dùng |
| `n` | Nonce ngẫu nhiên, dùng để chống phát lại |
| `iat` / `exp` | Epoch giây |

**Ba lớp bảo vệ, phải có đủ:**

1. **Ký phía máy chủ** — điện thoại chỉ hiển thị và quét, không tự chế được mã.
2. **Hạn cực ngắn + xoay vòng** — mã buổi học 30s, mã sinh viên 60s. Phản hồi
   kèm `refreshAfterSec` để client xin mã mới **trước khi** mã cũ hết hạn, nên
   màn hình không bao giờ hiện mã chết. Dung sai đồng hồ ±10s (`QR_CLOCK_SKEW_SEC`).
3. **Nonce dùng một lần** — máy chủ ghi lại cặp `(nonce, "<studentId>:<sessionId>")`.
   Lần thứ hai → `QR_ALREADY_USED`. Khoá gồm cả người tiêu thụ vì mã buổi học là
   mã chung: 50 sinh viên cùng quét một mã là hợp lệ, cùng **một** sinh viên quét
   hai lần thì không.

> **Giới hạn cần biết:** cơ chế này chặn chia sẻ ảnh chụp màn hình, nhưng không
> chặn được việc sinh viên A gọi video cho sinh viên B đang ngồi trong lớp để
> quét mã theo thời gian thực. Muốn chặn triệt để cần thêm ràng buộc vị trí
> (geofence/BLE) hoặc giảng viên quét mã sinh viên thay vì ngược lại — chiều
> `t = "U"` sinh ra đúng cho tình huống đó.

---

## 4. Lớp học và buổi học

### `GET /classes`

```jsonc
{ "items": [ { "id": "cls_it4409", "code": "IT4409", "name": "…", "term": "2026.1",
               "room": "D9-301", "lecturerId": "usr_gv01",
               "lecturerName": "TS. Nguyễn Thị Lan", "studentCount": 5 } ] }
```

### `GET /classes/{classId}/sessions`

```jsonc
{ "items": [ {
  "id": "ses_open_now", "classId": "cls_it4409", "title": "Buổi 5 — REST API",
  "room": "D9-301", "startsAt": "…", "endsAt": "…", "lateAfterMin": 15,
  "checkinState": "open", "openedAt": "…", "closedAt": null,
  "myStatus": "present"            // chỉ có khi người gọi là sinh viên
} ] }
```

### `GET /sessions/open`

Các buổi **đang mở điểm danh** liên quan tới người gọi — màn hình chính của app
dựa vào đây. Mỗi mục có thêm `classCode`, `className`.

### `POST /sessions` *(giảng viên, quản trị)*

```jsonc
{ "classId": "cls_it4409", "title": "Buổi 6", "room": "D9-301",
  "startsAt": "2026-10-10T00:00:00.000Z", "endsAt": "2026-10-10T02:30:00.000Z",
  "lateAfterMin": 15 }
// 201 → { "session": { … } }
```

### `POST /sessions/{id}/open` · `POST /sessions/{id}/close` *(giảng viên, quản trị)*

`close` đánh dấu **vắng** cho mọi sinh viên chưa có bản ghi:

```jsonc
{ "session": { … }, "markedAbsent": 3 }
```

### `GET /sessions/{id}/qr` *(giảng viên, quản trị)*

Buổi phải đang `open`, nếu không → `SESSION_CLOSED`.

```jsonc
{ "token": "DKC1.…", "expiresAt": "…", "ttlSec": 30, "refreshAfterSec": 18 }
```

### `GET /me/qr` *(sinh viên)*

```jsonc
{ "token": "DKC1.…", "studentCode": "2210001", "fullName": "Phạm Hoàng An",
  "expiresAt": "…", "ttlSec": 60, "refreshAfterSec": 36 }
```

---

## 5. Điểm danh

### `POST /attendance/check-in`

Một endpoint phục vụ **cả hai chiều quét**; máy chủ tự nhận biết loại mã.

```jsonc
{
  "qr": "DKC1.…",                              // bắt buộc — chuỗi đọc từ camera, nguyên văn
  "sessionId": "ses_open_now",                 // bắt buộc KHI quét mã sinh viên (t = "U")
  "clientUuid": "6f1c…",                       // nên có — khoá chống ghi trùng
  "deviceId": "android-a1b2c3",
  "scannedAt": "2026-10-03T07:02:11.000Z"      // giờ quét thật, cho bản ghi offline
}
```

Suy ra chiều điểm danh:

| Loại mã | Người gọi | Kết quả | `method` |
|---|---|---|---|
| `t = "S"` | sinh viên | chính người gọi được điểm danh | `qr_session` |
| `t = "U"` | giảng viên / quản trị | sinh viên trong mã được điểm danh | `qr_student` |

Mọi tổ hợp khác bị từ chối (`SESSION_QR_STUDENT_ONLY`, `STUDENT_QR_STAFF_ONLY`).

```jsonc
// 201 (bản ghi mới) hoặc 200 (đã tồn tại)
{
  "duplicate": false,
  "record": { "id": "att_…", "sessionId": "…", "studentId": "…",
              "status": "present", "method": "qr_session",
              "checkedInAt": "…", "recordedBy": "usr_sv01",
              "note": null, "clientUuid": "6f1c…", "updatedAt": "…" },
  "student": { "id": "usr_sv01", "code": "2210001", "fullName": "Phạm Hoàng An" },
  "sessionId": "ses_open_now"
}
```

`status`: `present` nếu quét trước `startsAt + lateAfterMin`, ngược lại `late`.
Mốc này tính theo `scannedAt` nếu có — nên bản ghi offline đồng bộ muộn vẫn được
tính đúng giờ quét thật.

> **Thứ tự kiểm tra bắt buộc:** tra `clientUuid` **trước** mọi bước khác. Một
> lượt quét đã ghi thành công nhưng phản hồi bị mất trên đường về sẽ được app
> gửi lại với đúng UUID cũ; lúc đó mã QR kèm theo đã hết hạn và nonce đã bị tiêu
> thụ, nên nếu xác thực QR trước thì lần gửi lại bị từ chối oan và sinh viên mất
> điểm danh.

### `POST /attendance/sync`

Đồng bộ hàng đợi offline. Tối đa 200 mục, mỗi mục **bắt buộc** có `clientUuid`.

```jsonc
{ "items": [ { "qr": "…", "sessionId": "…", "clientUuid": "…", "scannedAt": "…" } ] }
```

```jsonc
// 200 — luôn 200, kết quả từng mục nằm trong results[]
{
  "accepted": 1, "rejected": 1,
  "results": [
    { "clientUuid": "…", "ok": true, "duplicate": false, "record": { … }, "student": { … } },
    { "clientUuid": "…", "ok": false, "retryable": false,
      "error": { "code": "QR_MALFORMED", "message": "…" } }
  ]
}
```

Mỗi mục được xử lý độc lập — một lượt hỏng không làm hỏng cả lô.
`retryable: false` (mọi lỗi 4xx) nghĩa là app phải **bỏ mục đó khỏi hàng đợi**
thay vì thử lại vô hạn.

### `GET /sessions/{id}/attendance`

Giảng viên nhận danh sách đầy đủ kèm thống kê:

```jsonc
{
  "session": { … },
  "summary": { "total": 5, "present": 2, "late": 0, "excused": 1, "absent": 0, "pending": 2 },
  "items": [ { "studentId": "usr_sv01", "studentCode": "2210001",
               "fullName": "Phạm Hoàng An", "recordId": "att_…",
               "status": "present", "method": "qr_session",
               "checkedInAt": "…", "note": null } ]
}
```

Sinh viên gọi cùng endpoint chỉ nhận bản ghi của chính mình, `summary` là `null`.

### `POST /sessions/{id}/attendance` *(giảng viên, quản trị)*

Điểm danh tay — lối thoát khi điện thoại sinh viên hỏng hoặc camera không đọc được.

```jsonc
{ "studentId": "usr_sv01", "status": "present", "note": "Máy hết pin" }
// 200 → { "record": { … } }   // method = "manual"
```

### `GET /attendance/history`

Query: `studentId` (mặc định là chính mình), `classId`, `from`, `to`, `limit` (≤200), `offset`.

```jsonc
{
  "studentId": "usr_sv01",
  "summary": { "present": 3, "late": 0, "absent": 0, "excused": 1, "total": 4 },
  "items": [ { /* …AttendanceRecord…, */ "session": {
      "id": "…", "title": "…", "startsAt": "…", "endsAt": "…",
      "room": "D9-301", "classCode": "IT4409", "className": "Công nghệ Web…" } } ],
  "paging": { "limit": 50, "offset": 0, "count": 4 }
}
```

Sinh viên chỉ xem được của chính mình; giảng viên xem được sinh viên trong lớp
mình phụ trách; quản trị xem được tất cả.

---

## 6. Đơn xin phép

### `POST /leave-requests` *(sinh viên)*

```jsonc
{
  "classId": "cls_it4409",   // null = xin nghỉ TẤT CẢ các lớp
  "type": "sick",            // sick | personal | family | other
  "startDate": "2026-10-10",
  "endDate": "2026-10-10",   // bao gồm cả ngày này
  "reason": "Em bị sốt xuất huyết, có giấy nhập viện."   // ≥ 5 ký tự
}
// 201 → { "leaveRequest": { … } }
```

Chặn trùng: nếu sinh viên đã có đơn `pending` phủ lên cùng khoảng ngày và cùng
phạm vi lớp → `LEAVE_OVERLAPPING`.

### `GET /leave-requests`

Query: `status`, `classId`, `studentId`, `scope` (`mine` | `to-review`), `limit`, `offset`.

Phạm vi mặc định theo vai trò:

| Vai trò | Thấy gì |
|---|---|
| Sinh viên | Chỉ đơn của chính mình (bỏ qua mọi tham số mở rộng) |
| Giảng viên | Đơn thuộc các lớp mình phụ trách (dùng `scope=mine` để xem đơn của chính mình) |
| Quản trị | Tất cả |

Đơn `pending` **luôn được xếp lên đầu**, sau đó mới tới `createdAt` giảm dần.

```jsonc
{
  "items": [ {
    "id": "lv_…", "studentId": "usr_sv02", "classId": "cls_it4409",
    "type": "sick", "startDate": "2026-10-10", "endDate": "2026-10-10",
    "reason": "…", "attachmentUrl": null, "status": "pending",
    "reviewerId": null, "reviewNote": null, "reviewedAt": null,
    "createdAt": "…", "updatedAt": "…",
    "student": { "id": "usr_sv02", "code": "2210002", "fullName": "Lê Thanh Bình", "avatarUrl": null },
    "class": { "id": "cls_it4409", "code": "IT4409", "name": "Công nghệ Web…" },
    "reviewerName": null
  } ],
  "paging": { "limit": 30, "offset": 0, "total": 3 }
}
```

### `GET /leave-requests/pending-count` *(giảng viên, quản trị)*

```jsonc
{ "pending": 2 }
```

Dùng cho chấm đỏ trên tab. App gọi lại mỗi 30 giây.

### `GET /leave-requests/{id}`

### `POST /leave-requests/{id}/approve` *(giảng viên, quản trị)*

```jsonc
{ "note": "Đồng ý, em giữ gìn sức khoẻ." }   // tuỳ chọn
// 200
{ "leaveRequest": { "status": "approved", … }, "excusedSessions": 1 }
```

**Duyệt đơn phải tự cập nhật bảng điểm danh.** Mọi buổi học trong khoảng
`startDate…endDate`, thuộc lớp sinh viên có đăng ký (giới hạn theo `classId` nếu
đơn chỉ xin nghỉ một lớp), được đánh dấu `excused` với `method = "leave"`.

> **Bất biến quan trọng:** buổi nào sinh viên đã thực sự có mặt (`present` hoặc
> `late`) thì **giữ nguyên**. Đơn phép không bao giờ được ghi đè dữ liệu điểm
> danh thật. `excusedSessions` đếm số bản ghi thực sự bị đổi.

### `POST /leave-requests/{id}/reject` *(giảng viên, quản trị)*

```jsonc
{ "note": "Em bổ sung giấy khám bệnh rồi nộp lại nhé." }   // BẮT BUỘC, ≥ 3 ký tự
```

Bắt buộc lý do để sinh viên biết cần làm gì tiếp theo.

### `POST /leave-requests/{id}/cancel` *(sinh viên)*

Chỉ rút được đơn của chính mình và chỉ khi còn `pending`.

### Ai được duyệt đơn

| Đơn | Người duyệt |
|---|---|
| Có `classId` | Giảng viên phụ trách lớp đó, hoặc quản trị |
| `classId = null` (nghỉ mọi lớp) | **Chỉ quản trị** — không giảng viên nào bao quát hết các lớp |

Đơn đã xử lý không duyệt lại được → `LEAVE_NOT_PENDING`.

---

## 7. Danh sách kiểm tra khi web app hiện thực hợp đồng này

- [ ] `POST /auth/refresh` xoay vòng refresh token và thu hồi toàn bộ phiên khi phát hiện dùng lại
- [ ] `QR_SECRET` khác `JWT_SECRET`, cả hai ≥ 32 ký tự và không phải giá trị mẫu
- [ ] Chữ ký QR so sánh bằng hàm thời gian cố định
- [ ] Nonce QR lưu theo khoá `(nonce, "<studentId>:<sessionId>")` và được dọn định kỳ
- [ ] `clientUuid` là `UNIQUE` ở tầng cơ sở dữ liệu, và được tra **trước** khi xác thực QR
- [ ] `(sessionId, studentId)` là `UNIQUE` — mỗi sinh viên một bản ghi mỗi buổi
- [ ] Duyệt đơn phép không ghi đè bản ghi `present` / `late`
- [ ] `POST /attendance/sync` luôn trả 200 và báo lỗi từng mục, kèm cờ `retryable`
- [ ] Mọi lỗi dùng đúng hình dạng `{ "error": { "code", "message" } }` ở mục 1
