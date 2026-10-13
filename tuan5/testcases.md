# Test case chức năng Đăng nhập – Tuần 5

**Team:** [Tên team, ví dụ W1]
**Đối tượng kiểm thử:** Sauce Demo – https://www.saucedemo.com/
**Công cụ dự kiến:** Python + Selenium WebDriver + pytest
**Trình duyệt:** Google Chrome
**Ngày viết:** [dd/mm/yyyy] (viết trước khi có code)

---

## TC01 – Đăng nhập thành công với tài khoản hợp lệ

| Mục | Nội dung |
|---|---|
| Mục đích | Kiểm tra người dùng nhập đúng tài khoản và mật khẩu thì đăng nhập được |
| Điều kiện trước | Đang ở trang Đăng nhập https://www.saucedemo.com/ |
| Dữ liệu | Username: `standard_user` <br> Password: `secret_sauce` |

**Các bước:**
1. Mở trang https://www.saucedemo.com/.
2. Nhập `standard_user` vào ô Username.
3. Nhập `secret_sauce` vào ô Password.
4. Bấm nút Login.

**Kết quả mong đợi:**
- Chuyển sang trang danh sách sản phẩm (địa chỉ có `inventory.html`).
- Tiêu đề trang hiển thị chữ **Products**.

---

## TC02 – Đăng nhập thất bại khi sai mật khẩu

| Mục | Nội dung |
|---|---|
| Mục đích | Kiểm tra hệ thống từ chối đăng nhập khi mật khẩu sai |
| Điều kiện trước | Đang ở trang Đăng nhập https://www.saucedemo.com/ |
| Dữ liệu | Username: `standard_user` <br> Password: `sai_mat_khau_123` |

**Các bước:**
1. Mở trang https://www.saucedemo.com/.
2. Nhập `standard_user` vào ô Username.
3. Nhập `sai_mat_khau_123` vào ô Password.
4. Bấm nút Login.

**Kết quả mong đợi:**
- Vẫn ở trang Đăng nhập, không vào được trang sản phẩm.
- Hiển thị thông báo lỗi: **"Epic sadface: Username and password do not match any user in this service"**.

---

## TC03 – Đăng nhập thất bại khi bỏ trống thông tin

| Mục | Nội dung |
|---|---|
| Mục đích | Kiểm tra hệ thống yêu cầu nhập thông tin trước khi đăng nhập |
| Điều kiện trước | Đang ở trang Đăng nhập https://www.saucedemo.com/ |
| Dữ liệu | Username: (để trống) <br> Password: (để trống) |

**Các bước:**
1. Mở trang https://www.saucedemo.com/.
2. Không nhập gì vào ô Username và ô Password.
3. Bấm nút Login.

**Kết quả mong đợi:**
- Vẫn ở trang Đăng nhập, không vào được trang sản phẩm.
- Hiển thị thông báo lỗi: **"Epic sadface: Username is required"**.

---

## Bảng tổng hợp

| Mã | Tên test case | Dữ liệu chính | Kết quả mong đợi | Kết quả thực tế |
|---|---|---|---|---|
| TC01 | Đăng nhập thành công | `standard_user` / `secret_sauce` | Vào trang Products | [Pass/Fail – điền sau khi chạy] |
| TC02 | Sai mật khẩu | `standard_user` / `sai_mat_khau_123` | Báo lỗi không khớp tài khoản | [Pass/Fail] |
| TC03 | Bỏ trống thông tin | Để trống cả hai ô | Báo lỗi "Username is required" | [Pass/Fail] |
