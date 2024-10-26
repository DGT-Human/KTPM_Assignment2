import time
from Assignment.src.pages.base_page import BasePage
from Assignment.src.driver.driver import Driver
from Assignment.src.pages.register_page import RegisterPage


class TestRegister(Driver):
    def test_register_valid(self, driver):
        register_page = RegisterPage(driver)
        register_page.go_to_register()
        register_page.fill_registration_form("Nguyen", "E", "e@e.com", "12345")
        time.sleep(3)
        message = register_page.get_success_message()
        assert "Your Account Has Been Created!" in message

    def test_register_invalid_password(self, driver):
        register_page = RegisterPage(driver)
        register_page.go_to_register()
        register_page.fill_registration_form("Nguyen", "B", "b@b.com", "")
        time.sleep(3)
        message = register_page.get_error_message_password()
        assert "Password must be between 4 and 20 characters!" in message

    def test_register_invalid_email(self, driver):
        register_page = RegisterPage(driver)
        register_page.go_to_register()
        register_page.fill_registration_form("Nguyen", "B", "", "12345")
        time.sleep(3)
        message = register_page.get_error_message_email()
        assert "E-Mail Address does not appear to be valid!" in message

    def test_register_invalid_name(self, driver):
        register_page = RegisterPage(driver)
        register_page.go_to_register()
        register_page.fill_registration_form("", "", "b@b.com", "12345")
        time.sleep(3)
        message1 = register_page.get_error_message_firstname()
        message2 = register_page.get_error_message_lastname()
        assert "First Name must be between 1 and 32 characters!" in message1
        assert "Last Name must be between 1 and 32 characters!" in message2

    def test_register_invalid_agree(self, driver):
        register_page = RegisterPage(driver)
        register_page.go_to_register()
        register_page.fill_registration_form("Nguyen", "B", "b@b.com", "12345", False)
        time.sleep(3)
        message = register_page.get_error_message_agree()
        assert "You must agree to the Privacy Policy!" in message



