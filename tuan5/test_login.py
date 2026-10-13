"""
Tuần 5 - Kiểm thử tự động chức năng Đăng nhập trên https://www.saucedemo.com
Công cụ: Python + Selenium WebDriver + pytest

Cách chạy (trong thư mục tuan-05):
    pip install selenium pytest
    pytest test_login.py -v

Ghi chú: từ Selenium 4.6 trở lên, Selenium Manager tự tải ChromeDriver
phù hợp với Chrome trên máy, không cần tải driver bằng tay.
"""

import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# ---------------------------------------------------------------------------
# Dữ liệu dùng chung
# ---------------------------------------------------------------------------
URL_DANG_NHAP = "https://www.saucedemo.com/"
TAI_KHOAN_DUNG = "standard_user"
MAT_KHAU_DUNG = "secret_sauce"
MAT_KHAU_SAI = "sai_mat_khau_123"

# Thư mục lưu ảnh chụp màn hình trình duyệt sau mỗi bài kiểm thử
THU_MUC_ANH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anh")

# Cách tìm các phần tử trên trang đăng nhập (dựa vào id và data-test của trang)
O_TAI_KHOAN = (By.ID, "user-name")
O_MAT_KHAU = (By.ID, "password")
NUT_DANG_NHAP = (By.ID, "login-button")
THONG_BAO_LOI = (By.CSS_SELECTOR, "[data-test='error']")
TIEU_DE_TRANG_CHINH = (By.CLASS_NAME, "title")


# ---------------------------------------------------------------------------
# Fixture: mở trình duyệt trước mỗi bài test và đóng lại sau khi test xong
# ---------------------------------------------------------------------------
@pytest.fixture
def trinh_duyet():
    tuy_chon = webdriver.ChromeOptions()
    # Tắt hộp thoại "Đổi mật khẩu / mật khẩu bị lộ" của Chrome,
    # vì hộp thoại này có thể che trang và làm bài test bị lỗi
    tuy_chon.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    driver = webdriver.Chrome(options=tuy_chon)
    driver.maximize_window()
    driver.get(URL_DANG_NHAP)

    yield driver  # Trả trình duyệt cho bài test sử dụng

    driver.quit()  # Đóng trình duyệt sau khi bài test kết thúc


# ---------------------------------------------------------------------------
# Hàm hỗ trợ
# ---------------------------------------------------------------------------
def dang_nhap(driver, tai_khoan, mat_khau):
    """Nhập tài khoản, mật khẩu rồi bấm nút Đăng nhập."""
    driver.find_element(*O_TAI_KHOAN).send_keys(tai_khoan)
    driver.find_element(*O_MAT_KHAU).send_keys(mat_khau)
    driver.find_element(*NUT_DANG_NHAP).click()


def lay_thong_bao_loi(driver):
    """Chờ tối đa 5 giây cho thông báo lỗi hiện ra rồi lấy nội dung chữ."""
    phan_tu = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(THONG_BAO_LOI)
    )
    return phan_tu.text


def chup_anh(driver, ten_file):
    """Lưu ảnh màn hình trình duyệt vào thư mục anh/ làm bằng chứng."""
    os.makedirs(THU_MUC_ANH, exist_ok=True)
    driver.save_screenshot(os.path.join(THU_MUC_ANH, ten_file))


# ---------------------------------------------------------------------------
# TC01 - Đăng nhập thành công với tài khoản hợp lệ
# ---------------------------------------------------------------------------
def test_tc01_dang_nhap_thanh_cong(trinh_duyet):
    dang_nhap(trinh_duyet, TAI_KHOAN_DUNG, MAT_KHAU_DUNG)

    # Chờ trang danh sách sản phẩm tải xong
    WebDriverWait(trinh_duyet, 5).until(EC.url_contains("inventory.html"))
    chup_anh(trinh_duyet, "tc01_dang_nhap_thanh_cong.png")

    # Kiểm tra: đã chuyển sang trang chính và tiêu đề là "Products"
    assert "inventory.html" in trinh_duyet.current_url
    assert trinh_duyet.find_element(*TIEU_DE_TRANG_CHINH).text == "Products"


# ---------------------------------------------------------------------------
# TC02 - Đăng nhập thất bại khi sai mật khẩu
# ---------------------------------------------------------------------------
def test_tc02_sai_mat_khau(trinh_duyet):
    dang_nhap(trinh_duyet, TAI_KHOAN_DUNG, MAT_KHAU_SAI)

    loi = lay_thong_bao_loi(trinh_duyet)
    chup_anh(trinh_duyet, "tc02_sai_mat_khau.png")

    # Kiểm tra: hiện đúng thông báo lỗi và vẫn ở trang đăng nhập
    assert loi == (
        "Epic sadface: Username and password do not match any user in this service"
    )
    assert "inventory.html" not in trinh_duyet.current_url


# ---------------------------------------------------------------------------
# TC03 - Đăng nhập thất bại khi bỏ trống thông tin
# ---------------------------------------------------------------------------
def test_tc03_bo_trong_thong_tin(trinh_duyet):
    dang_nhap(trinh_duyet, "", "")

    loi = lay_thong_bao_loi(trinh_duyet)
    chup_anh(trinh_duyet, "tc03_bo_trong_thong_tin.png")

    # Kiểm tra: hệ thống yêu cầu nhập tên đăng nhập và không cho vào trang chính
    assert loi == "Epic sadface: Username is required"
    assert "inventory.html" not in trinh_duyet.current_url
