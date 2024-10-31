import time

from src.driver.driver import Driver
from src.pages.checkout import Checkout

# Lớp TestCheckout để thực hiện các kiểm tra trên trang checkout
class TestCheckout(Driver):

    # Test case: checkout cho khách hàng không đăng nhập hoặc đăng ký
    def test_checkout_guest(self, driver):
        from src.tests.test_add_to_cart import TestAddToCart
        # Gọi lại hàm add sản phẩm random bên add to cart
        TestAddToCart.test_add_to_cart_multiple_products_random_quantity(self, driver)
        # Tạo đối tượng checkout để thực hiện các bước thanh toán
        checkout = Checkout(driver)
        # Click vào shopping cart
        checkout.click_shopping_cart()
        # Chọn vào thanh toán
        checkout.click_checkout()
        # Chọn tùy chọn khách hàng không đăng nhập hoặc đăng ký
        checkout.click_guest_checkout()
        # Điền thông tin checkout vào
        checkout.set_checkout_guest_checkbox("Tien", "Du", "nqqqq@gmail.com", "SG", "145/5", "address2", "HCM", "12345", "Viet Nam", "Ho Chi Minh City", True)
        # Chọn tiếp tục để lưu thông tin
        checkout.click_continue_button()
        # Chọn phương thức vận chuyển
        checkout.choose_shipping_method()
        # Chọn phương thức thanh toán
        checkout.choose_payment_method()
        # Chọn xác nhận đơn hàng
        checkout.confirm_order()
        # So sánh kết quả với dự kiến: "Your order has been placed!"
        assert checkout.get_message() in "Your order has been placed!"

    # Test case: checkout cho khách hàng đăng ký
    def test_checkout_register(self, driver):
        from src.tests.test_add_to_cart import TestAddToCart
        # Gọi lại hàm add sản phẩm random bên add to cart
        TestAddToCart.test_add_to_cart_multiple_products_random_quantity(self, driver)

        # Tạo đối tượng checkout để thực hiện các bước thanh toán
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()

        # Tùy chọn khách hàng muốn đăng ký
        checkout.set_checkout_register_checkbox("Tien", "Du", "yqqqq@gmail.com", "SG", "145/5", "address2", "HCM", "12345", "Viet Nam", "Ho Chi Minh City", 123456, True, True)
        checkout.click_continue_button()
        checkout.choose_shipping_method()
        checkout.choose_payment_method()
        checkout.confirm_order()

        # So sánh kết quả với dự kiến: "Your order has been placed!"
        assert checkout.get_message() in "Your order has been placed!"

    # Test case: checkout cho khách hàng đăng ký với email đã được đăng ký
    def test_checkout_register_email_exist(self, driver):
        from src.tests.test_add_to_cart import TestAddToCart
        # Gọi lại hàm add sản phẩm random bên add to cart
        TestAddToCart.test_add_to_cart_multiple_products_random_quantity(self, driver)
        # Tạo đối tượng checkout để thực hiện các bước thanh toán
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        # Tùy chọn khách hàng muốn đăng ký (Điền Email đã được tạo)
        checkout.set_checkout_register_checkbox("Tien", "Du", "dugiatien1345@gmail.com", "SG", "145/5", "address2", "HCM", "12345", "Viet Nam", "Ho Chi Minh City", 123456, True, True)
        checkout.click_continue_button()

        # So sánh kết quả với dự kiến: "Warning: E-Mail Address is already registered!"
        assert checkout.get_error_message_email_exist() in "Warning: E-Mail Address is already registered!"


    # Test case: checkout cho khách hàng đăng ký với mật khẩu không tồn tại
    def test_checkout_register_password_invalid(self, driver):
        from src.tests.test_add_to_cart import TestAddToCart
        # Gọi lại hàm add to cart 1 sản phẩm vs số lượng là 1
        TestAddToCart.test_add_to_cart_one_quantity(self, driver)
        # Tạo đối tượng checkout để thực hiện các bước thanh toán
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        # Tùy chọn khách hàng muốn đăng ký (không điền mật khẩu)
        checkout.set_checkout_register_checkbox("Tien", "Du", "dugiatien1345@gmail.com", "SG", "145/5", "address2", "HCM", "12345", "Viet Nam", "Ho Chi Minh City", "", True, False)
        checkout.click_continue_button()
        # So sánh kết quả với dự kiến: "Password must be between 4 and 20 characters!"
        assert checkout.get_error_message_password_not_exist() in "Password must be between 4 and 20 characters!"

    # Test case: checkout cho khách hàng không đăng nhập/đăng ký với thông tin không hợp lệ
    def test_checkout_guest_invalid(self, driver):
        from src.tests.test_add_to_cart import TestAddToCart
        # Gọi lại hàm add to cart 1 sản phẩm vs số lượng là 1
        TestAddToCart.test_add_to_cart_one_quantity(self, driver)
        # Tạo đối tượng checkout để thực hiện các bước thanh toán
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        # Chọn tùy chọn khách hàng không đăng nhập hoặc đăng ký
        checkout.click_guest_checkout()
        # Không điền gì cả
        checkout.set_checkout_guest_checkbox("", "", "", "", "", "", "", "", "Viet Nam", "Ho Chi Minh City", True)
        checkout.click_continue_button()
        # So sánh kết quả với dự kiến
        assert checkout.get_error_message_fname_not_exist() in "First Name must be between 1 and 32 characters!"
        assert checkout.get_error_message_lname_not_exist() in "Last Name must be between 1 and 32 characters!"
        assert checkout.get_error_message_address_not_exist() in "Address 1 must be between 3 and 128 characters!"
        assert checkout.get_error_message_city_not_exist() in "City must be between 2 and 128 characters!"
        assert checkout.get_error_message_email_not_exist() in "E-Mail address does not appear to be valid!"

    # Test case: checkout cho khách hàng đăng ký với thông tin không hợp lệ
    def test_checkout_register_invalid(self, driver):
        from src.tests.test_add_to_cart import TestAddToCart
        # Gọi lại hàm add to cart 1 sản phẩm vs số lượng là 1
        TestAddToCart.test_add_to_cart_one_quantity(self, driver)
        # Tạo đối tượng checkout để thực hiện các bước thanh toán
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        # Tùy chọn khách hàng muốn đăng ký (không điền gì cả)
        checkout.set_checkout_register_checkbox("", "", "", "", "", "", "", "", "Viet Nam", "Ho Chi Minh City", 123456, False, False)
        checkout.click_continue_button()
        # So sánh kết quả với dự kiến
        assert checkout.get_error_message_fname_not_exist() in "First Name must be between 1 and 32 characters!"
        assert checkout.get_error_message_lname_not_exist() in "Last Name must be between 1 and 32 characters!"
        assert checkout.get_error_message_address_not_exist() in "Address 1 must be between 3 and 128 characters!"
        assert checkout.get_error_message_city_not_exist() in "City must be between 2 and 128 characters!"
        assert checkout.get_error_message_email_not_exist() in "E-Mail address does not appear to be valid!"
        assert checkout.get_error_policy() in "Warning: You must agree to the Privacy Policy!"

    # Test case: checkout cho khách hàng đăng ký với mật khẩu dài
    def test_checkout_register_password_to_long(self, driver):
        from src.tests.test_add_to_cart import TestAddToCart
        # Gọi lại hàm add to cart 1 sản phẩm vs số lượng là 1
        TestAddToCart.test_add_to_cart_one_quantity(self,driver)
        # Tạo đối tượng checkout để thực hiện các bước thanh toán
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        checkout.set_checkout_register_checkbox("Tien", "Du", "dugiatien134325@gmail.com", "SG", "145/5", "address2", "HCM", "12345", "Viet Nam", "Ho Chi Minh City", 1234563123131231231231231231231321331232131232131, True, True)
        checkout.click_continue_button()
        # So sánh kết quả với dự kiến
        assert checkout.get_error_message_password_not_exist() in "Password must be between 4 and 20 characters!"

    # Test case: checkout cho khách hàng đăng ký với mật khẩu ngắn
    def test_checkout_register_password_to_short(self, driver):
        from src.tests.test_add_to_cart import TestAddToCart
        # Gọi lại hàm add to cart 1 sản phẩm vs số lượng là 1
        TestAddToCart.test_add_to_cart_one_quantity(self,driver)
        # Tạo đối tượng checkout để thực hiện các bước thanh toán
        checkout = Checkout(driver)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        checkout.set_checkout_register_checkbox("Tien", "Du", "dugiatien1313345@gmail.com", "SG", "145/5", "address2", "HCM", "12345", "Viet Nam", "Ho Chi Minh City", 12, True, True)
        checkout.click_continue_button()
        # So sánh kết quả với dự kiến
        assert checkout.get_error_message_password_not_exist() in "Password must be between 4 and 20 characters!"

    # Test case: checkout cho khách hàng đã đăng ký và thực hiện đăng nhập
    def test_checkout_with_login(self, driver):
        from src.tests.test_login import TestLogin
        # Gọi lại hàm Login bên test_login
        TestLogin.test_login_valid(self,driver)
        from src.tests.test_add_to_cart import TestAddToCart
        # Gọi lại hàm add to cart 1 sản phẩm vs số lượng là 1
        TestAddToCart.test_add_to_cart_one_quantity(self, driver)
        checkout = Checkout(driver)
        time.sleep(2)
        checkout.click_shopping_cart()
        checkout.click_checkout()
        # Chọn thông tin đã được tạo trước đó
        checkout.choose_address_login('D Tiến, DGT, 145/5 Phan Văn Khỏe, TPHCM, Ho Chi Minh City, Viet Nam')
        checkout.choose_shipping_method()
        checkout.choose_payment_method()
        checkout.confirm_order()
        # So sánh kết quả với dự kiến
        assert checkout.get_message() in "Your order has been placed!"
