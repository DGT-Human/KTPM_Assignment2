import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

# Lớp Login kế thừa từ lớp BasePage chứa các chức năng của login
class LoginPage(BasePage):
    # Phương thức đến trang login
    def go_to_login(self):
        # Truy cập trang chủ của opencart
        self.driver.get("http://localhost/opencart/upload/")

        # Click MyAccount để thực hiện login
        self.driver.find_element(By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(., 'My Account')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]").click()
        time.sleep(3)

    # Phương thức thực hiện đăng nhập (email, password)
    def login(self, email, password):
        # Điền email
        email_input = self.driver.find_element(By.ID, "input-email")
        email_input.send_keys(email)

        # Điền password
        password_input = self.driver.find_element(By.ID, "input-password")
        password_input.send_keys(password)
        time.sleep(3)
        # Click login
        self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]").click()
        time.sleep(3)

    # Phương thức thực hiện đăng xuất
    def logout(self):
        # Chọn MyAccount để thực hiện đăng xuất
        self.driver.find_element(By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(., 'My Account')]").click()
        time.sleep(3)
        # Chọn Logout để thực hiện đăng xuất
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/a").click()

    # Phương thức xác nhận đăng nhập thành công
    def get_message_login(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/h2[1]").text
        return message

    # Phương thức xác nhận lỗi
    def get_error_message(self):
        return self.driver.find_element(By.XPATH, "/html/body/div").text



