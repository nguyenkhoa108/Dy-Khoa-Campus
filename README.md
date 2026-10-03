# Dy Khoa Campus — kho mã này đã ngừng sử dụng

Mã nguồn trong kho này **đã bị gỡ bỏ**. Công việc được gộp vào các dự án
đang chạy thật bên dưới.

## Tìm mã nguồn ở đâu

| Thành phần | Kho mã |
|---|---|
| Ứng dụng di động (Expo / React Native) | [`nguyenkhoa108/dykhoacampus`](https://github.com/nguyenkhoa108/dykhoacampus) — thư mục `campus-mobile` |
| Web app (Flask + MySQL, chạy trên cPanel) | [`nguyenkhoa108/dykhoa-campus-app`](https://github.com/nguyenkhoa108/dykhoa-campus-app) |
| Giao diện web (template Jinja) | [`nguyenkhoa108/dykhoa-campus-templates`](https://github.com/nguyenkhoa108/dykhoa-campus-templates) |

API cho ứng dụng di động nằm ở `routes_api.py` và `routes_api_mobile.py`
trong kho web app. Đó là nguồn tham chiếu duy nhất về hợp đồng API — đọc
thẳng mã nguồn, không có tài liệu tách rời.

## Vì sao gỡ bỏ

Kho này từng chứa một ứng dụng di động và một API tham chiếu Node/Express,
dựng khi kho còn trống và chưa rõ hệ thống sẵn có. Sau khi đối chiếu với
web app đang vận hành, hoá ra:

- Web app **đã có sẵn** điểm danh QR và phê duyệt đơn xin phép, cùng khoảng
  45 endpoint JSON phục vụ ứng dụng di động.
- Ứng dụng Expo `campus-mobile` **đã triển khai và đang được dùng**, phủ gần
  trọn số endpoint đó.
- Mã trong kho này dựng trên một mô hình dữ liệu khác hẳn: định dạng mã QR
  riêng thay vì URL + TOTP, trạng thái điểm danh bốn mức thay vì một dòng
  "có mặt", đơn xin phép theo khoảng ngày thay vì theo từng buổi, một bảng
  `users` thay vì hai bảng `students` và `teachers`.

Giữ lại chỉ gây nhầm lẫn cho người đọc sau này, nên toàn bộ `mobile/`,
`server/` và `docs/` đã được gỡ. Lịch sử Git vẫn còn nếu cần tra lại.
