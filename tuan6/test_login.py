"""
Demo tuần 6 – Team W1
Chạy: python -m unittest test_login.py -v
Cần: pip install selenium   (Selenium 4 tự tải ChromeDriver)
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

BASE_URL = "https://the-internet.herokuapp.com"


class TestLogin(unittest.TestCase):

    def setUp(self):
        # Mở trình duyệt trước MỖI test
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        # Đóng trình duyệt sau MỖI test
        self.driver.quit()

    def test_login_thanh_cong(self):
        d = self.driver
        d.get(BASE_URL + "/login")
        d.find_element(By.ID, "username").send_keys("tomsmith")
        d.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        d.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        flash = d.find_element(By.ID, "flash").text
        self.assertIn("You logged into a secure area!", flash)

    def test_login_sai_mat_khau(self):
        d = self.driver
        d.get(BASE_URL + "/login")
        d.find_element(By.ID, "username").send_keys("tomsmith")
        pw = d.find_element(By.ID, "password")
        pw.send_keys("saimatkhau")
        pw.send_keys(Keys.ENTER)  # gửi form bằng phím Enter thay vì bấm nút

        flash = d.find_element(By.ID, "flash").text
        self.assertIn("Your password is invalid!", flash)


class TestKeyPresses(unittest.TestCase):
    """Phần thêm: liên quan chức năng 1 của W1 (/key_presses)."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_bam_phim_tab(self):
        d = self.driver
        d.get(BASE_URL + "/key_presses")
        d.find_element(By.ID, "target").send_keys(Keys.TAB)
        self.assertEqual(d.find_element(By.ID, "result").text, "You entered: TAB")


if __name__ == "__main__":
    unittest.main(verbosity=2)
