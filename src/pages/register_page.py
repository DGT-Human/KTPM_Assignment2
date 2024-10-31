import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

# Lớp này chứa các phương thức để thực hiện các hành động trên trang đăng ký
class RegisterPage(BasePage):

    # Phương thức để điều hướng đến trang đăng ký
    def go_to_register(self):
        # Điều hướng đến trang chủ
        self.driver.get("http://localhost/opencart/upload/")

        # Tìm và click vào nút "My Account" trên menu
        self.driver.find_element(By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(., 'My Account')]").click()

        # Chờ 10 giây để đảm bảo trang được tải đầy đủ
        time.sleep(10)

        # Tìm và click vào nút "Register" trên menu
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Register')]").click()

        # Chờ 10 giây để đảm bảo trang được tải đầy đủ
        time.sleep(10)

    # Phương thức để điền thông tin vào form đăng ký
    def fill_registration_form(self, firstname, lastname, email, password, agree=True):
        # Kéo trang xuống để hiển thị form đăng ký
        self.scroll_to(0, 200)

        # Tìm và điền thông tin vào trường "First Name"
        self.driver.find_element(By.ID, "input-firstname").send_keys(firstname)

        # Tìm và điền thông tin vào trường "Last Name"
        self.driver.find_element(By.ID, "input-lastname").send_keys(lastname)

        # Tìm và điền thông tin vào trường "Email"
        self.driver.find_element(By.ID, "input-email").send_keys(email)

        # Tìm và điền thông tin vào trường "Password"
        self.driver.find_element(By.ID, "input-password").send_keys(password)

        # Nếu đồng ý với điều khoản sử dụng thì tick vào checkbox
        if agree:
            self.driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='agree']").click()

        # Tìm và click vào nút "Continue"
        self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]").click()

    # Phương thức để lấy thông báo thành công sau khi đăng ký
    def get_success_message(self):
        # Tìm và lấy thông báo thành công
        return self.driver.find_element(By.XPATH, "//h1[text()='Your Account Has Been Created!']").text

    # Phương thức để lấy thông báo lỗi sau khi đăng ký
    def get_error_message(self):
        # Tìm và lấy thông báo lỗi
        return self.driver.find_element(By.XPATH, "/html/body/div").text

    # Phương thức để lấy thông báo lỗi về tên
    def get_error_message_firstname(self):
        # Tìm và lấy thông báo lỗi về tên đầu
        return self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[1]/div/div").text

    # Phương thức để lấy thông báo lỗi về họ
    def get_error_message_lastname(self):
        # Tìm và lấy thông báo lỗi về tên cuối
        return self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[2]/div/div").text

    # Phương thức để lấy thông báo lỗi về email
    def get_error_message_email(self):
        # Tìm và lấy thông báo lỗi về email
        return self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[3]/div/div").text

    # Phương thức để lấy thông báo lỗi về mật này
    def get_error_message_password(self):
        # Tìm và lấy thông báo lỗi về mật khẩu
        return self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[2]/div/div/div").text
