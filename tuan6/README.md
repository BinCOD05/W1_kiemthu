# Tuần 6 – Team W1

Báo cáo chuyên đề: kiểm thử tự động với Selenium WebDriver, demo bài kiểm thử Đăng nhập trên
[the-internet.herokuapp.com](https://the-internet.herokuapp.com).

## Nội dung thư mục

| File | Mô tả |
|---|---|
| `slides.pdf` | Slide trình bày (tối đa 8 trang) |
| `notes.md` | Góp ý nhận được và điều team sẽ cải thiện |
| `test_login.py` | Bài kiểm thử Đăng nhập + bấm phím (`/login`, `/key_presses`) |
| `requirements.txt` | Thư viện cần cài |

## Yêu cầu

- Python 3.8 trở lên
- Google Chrome (Selenium 4 tự tải ChromeDriver, không cần cài riêng)

## Cách chạy

```bash
pip install -r requirements.txt
python -m unittest test_login.py -v
```

## Các test có trong `test_login.py`

| Test | Trang | Kiểm tra gì |
|---|---|---|
| `test_login_thanh_cong` | `/login` | Đăng nhập đúng → hiện thông báo vào khu vực bảo mật |
| `test_login_sai_mat_khau` | `/login` | Sai mật khẩu, gửi form bằng `Keys.ENTER` → hiện thông báo lỗi |
| `test_bam_phim_tab` | `/key_presses` | Nhấn `Keys.TAB` → trang hiện đúng tên phím |

Kết quả mong đợi: `Ran 3 tests ... OK`.
