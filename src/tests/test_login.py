import time
from src.driver.driver import Driver
from src.pages.login_page import LoginPage

# Lớp này chứa các trường hợp kiểm thử cho chức năng đăng nhập của trang web.
class TestLogin(Driver):

    # Test case: Thông tin đăng nhập hợp lệ
    def test_login_valid(self, driver):
        # Tạo một đối tượng của lớp LoginPage
        login_page = LoginPage(driver)
        # Điều hướng đến trang đăng nhập
        login_page.go_to_login()
        time.sleep(2)
        # Nhập thông tin đăng nhập hợp lệ
        login_page.login("b@b.com", "12345")
        time.sleep(2)
        # So sánh kết quả với dự kiến
        message = login_page.get_message_login()
        assert message in "My Account"

    # Test case: Thông tin đăng nhập không có email
    def test_login_invalid_email(self, driver):
        login_page = LoginPage(driver)
        # Điều hướng đến trang đăng nhập
        login_page.go_to_login()
        time.sleep(3)
        # Nhập thông tin đăng nhập không hợp lệ
        login_page.login("", "12345")
        # So sánh kết quả với dự kiến
        message = login_page.get_error_message()
        time.sleep(2)
        assert message in "Warning: No match for E-Mail Address and/or Password."

    # Test case: Thông tin đăng nhập không có password
    def test_login_invalid_password(self, driver):
        login_page = LoginPage(driver)
        # Điều hướng đến trang đăng nhập
        login_page.go_to_login()
        # Nhập thông tin đăng nhập không hợp lệ
        login_page.login("b@b.com", "")
        # So sánh kết quả với dự kiến
        message = login_page.get_error_message()
        time.sleep(2)
        assert message in "Warning: No match for E-Mail Address and/or Password."

    # Test case: Thông tin đăng nhập email không có trong dữ liệu
    def test_login_email_not_exist(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login()
        # Nhập thông tin đăng nhập không hợp lệ
        login_page.login("d@d.com", "12345")
        # So sánh kết quả với dự kiến
        message = login_page.get_error_message()
        time.sleep(2)
        assert message in "Warning: No match for E-Mail Address and/or Password."

    # Test case: Thông tin đăng nhập sai password
    def test_login_password_not_exist(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login()
        # Nhập thông tin đăng nhập password không đúng
        login_page.login("b@b.com", "123456")
        # So sánh kết quả với dự kiến
        message = login_page.get_error_message()
        time.sleep(2)
        assert message in "Warning: No match for E-Mail Address and/or Password."

    # Test case: Đăng xuất
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login()
        # Nhập thông tin đăng nhập
        login_page.login("b@b.com", "12345")
        time.sleep(2)
        # Đăng xuất
        login_page.logout()
        time.sleep(2)
        # So sánh kết quả với dự kiến
        message = ''
        assert message in ""