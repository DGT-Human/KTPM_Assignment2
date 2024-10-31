import time
from src.driver.driver import Driver
from src.pages.register_page import RegisterPage


# Lớp này chứa các phương thức để thực hiện các kiểm tra trên trang đăng ký
class TestRegister(Driver):

    # Test case: kiểm tra đăng ký thành công
    def test_register_valid(self, driver):
        # Tạo đối tượng RegisterPage
        register_page = RegisterPage(driver)

        # Điều hướng đến trang đăng ký
        register_page.go_to_register()

        # Điền thông tin đăng ký hợp lệ
        register_page.fill_registration_form("Nguyen", "q", "q@qqqq.com", "12345")
        time.sleep(3)

        # Lấy thông báo thành công
        message = register_page.get_success_message()

        # So sánh kết quả với dự kiến
        assert message in "Your Account Has Been Created!"

    # Test case: kiểm tra đăng ký thất bại do mật khẩu không hợp lệ
    def test_register_invalid_password(self, driver):
        # Tạo đối tượng RegisterPage
        register_page = RegisterPage(driver)

        # Điều hướng đến trang đăng ký
        register_page.go_to_register()

        # Điền thông tin đăng ký không hợp lệ (mật khẩu rỗng)
        register_page.fill_registration_form("Nguyen", "B", "b@bbb.com", "")
        time.sleep(3)

        # Lấy thông báo lỗi mật khẩu
        message = register_page.get_error_message_password()

        # So sánh kết quả với dự kiến
        assert message in "Password must be between 4 and 20 characters!"

    # Test case: kiểm tra đăng ký thất bại do email không hợp lệ
    def test_register_invalid_email(self, driver):
        # Tạo đối tượng RegisterPage
        register_page = RegisterPage(driver)

        # Điều hướng đến trang đăng ký
        register_page.go_to_register()

        # Điền thông tin đăng ký không hợp lệ (email rỗng)
        register_page.fill_registration_form("Nguyen", "B", "", "12345")
        time.sleep(3)

        # Lấy thông báo lỗi email
        message = register_page.get_error_message_email()

        # So sánh kết quả với dự kiến
        assert message in "E-Mail Address does not appear to be valid!"

    # Test case: kiểm tra đăng ký thất bại do tên không hợp lệ
    def test_register_invalid_name(self, driver):
        # Tạo đối tượng RegisterPage
        register_page = RegisterPage(driver)

        # Điều hướng đến trang đăng ký
        register_page.go_to_register()

        # Điền thông tin đăng ký không hợp lệ (tên trống)
        register_page.fill_registration_form("", "", "b@bb.com", "12345")

        # Chờ 3 giây để đảm bảo trang được tải đầy đủ
        time.sleep(3)

        # Lấy thông báo lỗi tên
        message1 = register_page.get_error_message_firstname()
        message2 = register_page.get_error_message_lastname()

        # So sánh kết quả với dự kiến
        assert message1 in "First Name must be between 1 and 32 characters!"
        assert message2 in "Last Name must be between 1 and 32 characters!"

    # Test case: kiểm tra đăng ký thất bại do email đã đăng ký
    def test_register_email_exist(self, driver):
        # Tạo đối tượng RegisterPage
        register_page = RegisterPage(driver)
        # Điều hướng đến trang đăng ký
        register_page.go_to_register()
        # Điền thông tin đăng ký không hợp lệ (email đã đăng ký)
        register_page.fill_registration_form("Nguyen", "B", "b@b.com", "12345")
        time.sleep(3)
        # So sánh kết quả với dự kiến
        message = register_page.get_error_message()
        assert message in "Warning: E-Mail Address is already registered!"

    # Test case: kiểm tra đăng ký thất bại do mật khẩu dài
    def test_register_password_long(self, driver):
        # Tạo đối tượng RegisterPage
        register_page = RegisterPage(driver)
        # Điều hướng đến trang đăng ký
        register_page.go_to_register()
        # Điền thông tin đăng ký không hợp lệ (email đã đăng ký)3
        register_page.fill_registration_form("Nguyen", "B", "w@w.com", "1234513131313131313131331311313213123112311313131")
        time.sleep(3)
        # So sánh kết quả với dự kiến
        message = register_page.get_error_message_password()
        assert message in "Password must be between 4 and 20 characters!"

    # Test case: kiểm tra đăng ký thể mật khẩu ngắn
    def test_register_password_short(self, driver):
        # Tạo đối tượng RegisterPage
        register_page = RegisterPage(driver)
        # Điều hướng đến trang đăng ký
        register_page.go_to_register()
        # Đi neger đăng ký không hợp lệ (email không đăng ký)3
        register_page.fill_registration_form("Nguyen", "B", "w@w.com", "12")
        time.sleep(3)
        # So sánh kết quả với dự kiến
        message = register_page.get_error_message_password()
        assert message in "Password must be between 4 and 20 characters!"

    # Test case: kiểm tra đăng ký tên quá dài
    def test_register_name_long(self, driver):
        # Tạo đối tượng RegisterPage
        register_page = RegisterPage(driver)
        # Điều hướng đến trang đăng ký
        register_page.go_to_register()
        # Đi neger đăng ký không hợp lệ (email không đăng ký)3
        register_page.fill_registration_form("Nguyenasdsadsadsadsadsadsadsadsaddadasdasdsdadadsadsadsa", "Nguyenasdsadsadsadsadsadsadsadsaddadasdasdsadsadsadsadsad", "w@w.com", "12345")
        time.sleep(3)
        # So sánh kết quả với dự kiến
        message1 = register_page.get_error_message_firstname()
        message2 = register_page.get_error_message_lastname()
        assert message1 in "First Name must be between 1 and 32 characters!"
        assert message2 in "Last Name must be between 1 and 32 characters!"


    # Test case: kiểm tra đăng ký thất bại do không chọn chính sách
    def test_register_policy_not_check(self, driver):
        # Tạo đối tượng RegisterPage
        register_page = RegisterPage(driver)
        # Điều hướng đầu trang đăng ký
        register_page.go_to_register()
        # Đi neger đăng ký không hợp lệ (email không đăng ký)3
        register_page.fill_registration_form("Nguyen", "B", "w@w.com", "12345", False)
        time.sleep(3)
        # So sánh kết quả với dự kiến
        message = register_page.get_error_message()
        assert message in "Warning: You must agree to the Privacy Policy!"