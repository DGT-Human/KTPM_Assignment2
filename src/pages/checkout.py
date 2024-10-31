import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import Select


# Lớp Checkout để thực hiện các hành động trên trang checkout
class Checkout(BasePage, Select):

    # Click vào nút giỏ hàng
    def click_shopping_cart(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[4]/a").click()
        time.sleep(3)

    # Click vào nút checkout
    def click_checkout(self):
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[3]/div[2]/a"))
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[3]/div[2]/a").click()
        time.sleep(3)

    # Click vào nút checkout cho khách hàng không đăng nhập hoặc đăng ký
    def click_guest_checkout(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[1]/div[1]/div[2]").click()
        time.sleep(3)

    # Điền thông tin cho khách hàng không đăng nhập
    def set_checkout_guest_checkbox(self, firstname = None, lastname = None, email = None, company = None, address1 = None, address2 = None, city = None,  postcode = None, country = None, region = None, wish = False):
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[1]/input").send_keys(firstname) # First Name
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[2]/input").send_keys(lastname) # Last name
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[3]/input").send_keys(email) # Email
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[1]/input").send_keys(company) # Công ty
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[2]/input").send_keys(address1) # Địa chỉ 1
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[3]/input").send_keys(address2) # Địa chỉ 2
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[4]/input").send_keys(city) # Thành phố
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[5]/input").send_keys(postcode) # PostCode
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[6]/select")) # cuộn xuống
        time.sleep(2)
        Select(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[6]/select")).select_by_visible_text(country) # chọn nước
        time.sleep(2)
        Select(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[7]/select")).select_by_visible_text(region) # chọn khu vực
        if wish: # Click vào Wish
            self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/div[2]/div/div[1]/input").click()

    # Đặt thông tin cho khách hàng đăng ký
    def set_checkout_register_checkbox(self, firstname, lastname, email, company, address1, address2, city,  postcode, country, region, password, wish = False, read = False):
        # Gọi lại hàm thông tin khách hàng không đăng ký
        self.set_checkout_guest_checkbox(firstname, lastname, email, company, address1, address2, city,  postcode, country, region, wish)
        # Nhập mật khẩu
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input").send_keys(password)
        # Nếu read = True thì sẽ chọn vào
        if read:
            self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/div[2]/div/div[2]/input").click()
        time.sleep(3)

    # Click vào nút tiếp tục
    def click_continue_button(self):
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/div[2]/div/button").click()
        time.sleep(3)

    # Chọn phương thức vận chuyển
    def choose_shipping_method(self):
        time.sleep(3)
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[1]/fieldset/div[1]/input"))
        self.driver.find_element(By.ID, "button-shipping-methods").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[1]/input").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/button").click()
        time.sleep(1)

    # Chọn phương thức thanh toán
    def choose_payment_method(self):
        self.driver.find_element(By.ID, "button-payment-methods").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[1]/input").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/button").click()
        time.sleep(1)

    def choose_address_login(self, address):
        Select(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[2]/select")).select_by_visible_text(address)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div/div/button").click()
    # Chọn xác nhận đơn hàng
    def confirm_order(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button").click()
        time.sleep(3)

    # Lấy thông báo trên trang
    def get_message(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/h1").text
        return message

    # Lấy thông báo lỗi khi email đã tồn tại
    def get_error_message_email_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/div/div").text
        return message

    # Lấy thông báo lỗi khi mật khẩu không tồn tại
    def get_error_message_password_not_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/div[1]/div[1]/fieldset/div/div/div").text
        return message

    # Lấy thông báo lỗi khi họ không tồn tại
    def get_error_message_fname_not_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[1]/div").text
        return message

    # Lấy thông báo lỗi khi tên không tồn tại
    def get_error_message_lname_not_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[2]/div").text
        return message

    # Lấy thông báo lỗi khi địa chỉ không tồn tại
    def get_error_message_address_not_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[2]/div").text
        return message

    # Lấy thông báo lỗi khi thành phố không tồn tại
    def get_error_message_city_not_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[4]/div").text
        return message

    # Lấy thông báo lỗi khi eamil không tồn tại
    def get_error_message_email_not_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[3]/div").text
        return message

    # Lấy thông báo lỗi khi không đồng ý policy
    def get_error_policy(self):
        message = self.driver.find_element(By.XPATH, "/html/body/div/div").text
        return message