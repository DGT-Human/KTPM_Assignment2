import time
from src.driver.driver import Driver
from src.pages.login_page import LoginPage


class TestLogin(Driver):
    def test_login_valid(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login()
        time.sleep(3)
        login_page.login("b@b.com", "12345")
        time.sleep(3)
        message = login_page.get_message_login()
        assert "My Account" in message

    def test_login_invalid_email(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login()
        time.sleep(3)
        login_page.login("", "12345")
        message = login_page.get_error_message()
        time.sleep(3)
        assert "Warning: No match for E-Mail Address and/or Password." in message

    def test_login_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login()
        login_page.login("b@b.com", "")
        message = login_page.get_error_message()
        time.sleep(3)
        assert "Warning: No match for E-Mail Address and/or Password." in message

    def test_login_email_not_exist(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login()
        login_page.login("d@d.com", "12345")
        message = login_page.get_error_message()
        time.sleep(3)
        assert "Warning: No match for E-Mail Address and/or Password." in message

    def test_login_password_not_exist(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login()
        login_page.login("b@b.com", "123456")
        message = login_page.get_error_message()
        time.sleep(3)
        assert "Warning: No match for E-Mail Address and/or Password." in message

    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login()
        login_page.login("b@b.com", "12345")
        time.sleep(3)
        login_page.logout()
        time.sleep(3)
        message = ''
        assert "" in message