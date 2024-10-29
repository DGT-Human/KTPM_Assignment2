from src.driver.driver import Driver
from .test_add_to_cart import TestAddToCart
from src.pages.checkout import Checkout


class TestCheckout(TestAddToCart, Driver):

    def test_checkout_guest(self, driver):
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        checkout.click_guest_checkout()
        checkout.set_checkout_guest_checkbox("Tien", "Du", "dugiatien@gmail.com", "SG", "145/5", "address2", "HCM", "12345", "Viet Nam", "Ho Chi Minh City", True)
        checkout.click_continue_button()
        checkout.choose_shipping_method()
        checkout.choose_payment_method()
        checkout.confirm_order()
        assert checkout.get_message() == "Your order has been placed!"

    def test_checkout_register(self, driver):
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        checkout.set_checkout_register_checkbox("Tien", "Du", "dugiatien1345@gmail.com", "SG", "145/5", "address2", "HCM", "12345", "Viet Nam", "Ho Chi Minh City", 123456, True, True)
        checkout.click_continue_button()
        checkout.choose_shipping_method()
        checkout.choose_payment_method()
        checkout.confirm_order()
        assert checkout.get_message() == "Your order has been placed!"

    def test_checkout_register_email_exist(self, driver):
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        checkout.set_checkout_register_checkbox("Tien", "Du", "dugiatien1345@gmail.com", "SG", "145/5", "address2", "HCM", "12345", "Viet Nam", "Ho Chi Minh City", 123456, True, True)
        checkout.click_continue_button()
        assert checkout.get_error_message_email_exist() == "Warning: E-Mail Address is already registered!"
        # checkout.choose_shipping_method()
        # checkout.choose_payment_method()
        # checkout.confirm_order()

    def test_checkout_register_password_not_exist(self, driver):
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        checkout.set_checkout_register_checkbox("Tien", "Du", "dugiatien1345@gmail.com", "SG", "145/5", "address2", "HCM", "12345", "Viet Nam", "Ho Chi Minh City", "", True, False)
        checkout.click_continue_button()
        assert checkout.get_error_message_password_not_exist() == "Password must be between 4 and 20 characters!"

    def test_checkout_guest_invalid(self, driver):
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        checkout.click_guest_checkout()
        checkout.set_checkout_guest_checkbox("", "", "", "", "", "", "", "", "Viet Nam", "Ho Chi Minh City", True)
        checkout.click_continue_button()
        assert checkout.get_error_message_fname_not_exist() == "First Name must be between 1 and 32 characters!"
        assert checkout.get_error_message_lname_not_exist() == "Last Name must be between 1 and 32 characters!"
        assert checkout.get_error_message_address_not_exist() == "Address 1 must be between 3 and 128 characters!"
        assert checkout.get_error_message_city_not_exist() == "City must be between 2 and 128 characters!"
        assert checkout.get_error_message_email_not_exist() == "E-Mail address does not appear to be valid!"

    def test_checkout_register_invalid(self, driver):
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        checkout.set_checkout_register_checkbox("", "", "", "", "", "", "", "", "Viet Nam", "Ho Chi Minh City", 123456, False, False)
        checkout.click_continue_button()
        assert checkout.get_error_message_fname_not_exist() == "First Name must be between 1 and 32 characters!"
        assert checkout.get_error_message_lname_not_exist() == "Last Name must be between 1 and 32 characters!"
        assert checkout.get_error_message_address_not_exist() == "Address 1 must be between 3 and 128 characters!"
        assert checkout.get_error_message_city_not_exist() == "City must be between 2 and 128 characters!"
        assert checkout.get_error_message_email_not_exist() == "E-Mail address does not appear to be valid!"
        assert checkout.get_error_policy() == "Warning: You must agree to the Privacy Policy!"

    def test_checkout_register_password_to_long(self, driver):
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        checkout.set_checkout_register_checkbox("Tien", "Du", "dugiatien134325@gmail.com", "SG", "145/5", "address2", "HCM", "12345", "Viet Nam", "Ho Chi Minh City", 1234563123131231231231231231231321331232131232131, True, True)
        checkout.set_checkout_register_checkbox("Tien", "Du", "dugiatien1345@gmail.com", "SG", "145/5", "address2", "HCM", "12345", "Viet Nam", "Ho Chi Minh City", 12, True, True)
        checkout.click_continue_button()
        assert checkout.get_error_message_password_not_exist() == "Password must be between 4 and 20 characters!"

    def test_checkout_register_password_to_short(self, driver):
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        checkout.set_checkout_register_checkbox("Tien", "Du", "dugiatien1313345@gmail.com", "SG", "145/5", "address2", "HCM", "12345", "Viet Nam", "Ho Chi Minh City", 12, True, True)
        checkout.click_continue_button()
        assert checkout.get_error_message_password_not_exist() == "Password must be between 4 and 20 characters!"