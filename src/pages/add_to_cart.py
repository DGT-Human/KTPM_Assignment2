import time
from selenium.webdriver.common.by import By
from .base_page import BasePage


# Lớp này chứa các phương thức để thực hiện các hành động về add to cart
class AddToCart(BasePage):
    def go_to_product(self, name):
        # Chọn vào sản phẩm  có tên là name

        self.driver.find_element(By.LINK_TEXT, name).click()
        time.sleep(3)

    def add_to_cart(self):
        # Thêm sản phẩm vào giỏ hàng

        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/form/div/button").click()
        time.sleep(3)

    def get_product_name(self):
        # Lấy tên của sản phẩm
        # Returns: str Tên sản phẩm

        name = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/h1").text
        return name

    def set_qty(self, qty):
        # Thiết lập số lượng sản phẩm

        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/form/div/input[1]").clear()
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/form/div/input[1]").send_keys(qty)
        time.sleep(3)

    def click_shopping_cart(self):
        # Click vào nút giỏ hàng

        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[4]/a/span").click()
        time.sleep(3)

    def click_view_fast_cart(self):
        # Click vào nút xem giỏ hàng nhanh

        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/button").click()
        time.sleep(3)

    def update_qty_multiple_products(self, qty):
        #Cập nhật số lượng của nhiều sản phẩm

        product_rows = self.driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr")
        # Nếu qty = 0 hoặc dưới 0 thì sẽ chạy vào lệnh này (Ví khi update nó sẽ mất sản phẩm đi và nhảy dòng lên)
        if qty == 0 or qty < 0:
            for _ in range(len(product_rows)):
                quantity_input = self.driver.find_element(By.XPATH, ".//input[@name='quantity']")
                quantity_input.clear()
                quantity_input.send_keys(str(qty))
                time.sleep(3)
                update_button = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[4]/form/div/button[1]")
                update_button.click()
                time.sleep(2)
        else:
            # Còn qty > 0 thì sẽ chạy này
            for _ in range(len(product_rows)):
                product_rows = self.driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr")
                product_row = product_rows[_]
                quantity_input = product_row.find_element(By.XPATH, ".//input[@name='quantity']")
                quantity_input.clear()
                quantity_input.send_keys(str(qty))
                time.sleep(3)
                update_button = product_row.find_element(By.XPATH, ".//button[1]")
                update_button.click()
                time.sleep(2)

    def remove_product_from_shopping_cart(self):
        # Xóa sản phẩm khỏi trang giỏ hàng

        product_rows = self.driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr")
        for _ in range(len(product_rows)):
            update_button = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr/td[4]/form/div/button[2]")
            update_button.click()
            time.sleep(2)

    def remove_product_on_view_fast_cart(self):
        # Xóa những sản phẩm khỏi giỏ hàng nhanh

        self.driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/ul/li/table/tbody/tr[1]/td[5]/form/button").click()
        time.sleep(2)

    def get_cart_product_qty_view_fast_cart(self):
        # Lấy số lượng sản phẩm trong trang xem sản phẩm
        # Returns: list Danh sách số lượng sản phẩm

        qty_elements = self.driver.find_elements(By.XPATH, '//tbody/tr')
        qty_values = []
        for element in qty_elements:
            qty_text = element.find_element(By.XPATH, ".//td[@class='text-end'][1]").text.strip()
            if qty_text.startswith('x'):
                qty_number = qty_text[1:].strip()
                qty_values.append(qty_number)

        return qty_values

    def calculate_cart_product_total_price(self):
        # Tính tổng giá các sản phẩm trong giỏ hàng
        # Returns: float Tổng giá sản phẩm

        # lấy số dòng trong shopping cart
        rows = self.driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr")
        total_price = 0

        for row in rows:
            # Lấy số lượng từng sản phẩm
            quantity = row.find_element(By.XPATH, ".//input[1]").get_attribute('value')
            if quantity == '':
                quantity = 0

            # Lấy số giá sản phẩm
            unit_price_element = row.find_element(By.XPATH, ".//td[contains(@class, 'text-end')][1]")
            unit_price = unit_price_element.text.strip()
            if unit_price == '':
                unit_price = 0.0
            else:
                unit_price = float(unit_price.replace('$', '').replace(',', ''))  # Xử lý ký tự '$' và ',' nếu có

            # print(quantity, unit_price)
            # Tính tổng tiền
            total_price += int(quantity) * unit_price

        return total_price

    def get_total_price_bill(self):
        # Lấy tổng giá các sản phẩm trên hóa đơn khi có sản phẩm
        # Returns: float Giá hóa đơn

        total_price = self.driver.find_element(By.XPATH,
                                               "/html/body/main/div[2]/div/div/div[1]/div/table/tfoot/tr[4]/td[2]").text
        total_price = float(total_price.replace('$', '').replace(',', ''))
        return float(total_price)

    def get_total_price_bill_without_product(self):
        # Lấy tổng giá khi không có sản phẩm (vì khi xóa sản phẩm khỏi giỏ thì phí thuế này kia mất đi làm cho tổng gia nằm ở dòng 2)
        # Returns: float Giá sản phẩm

        price = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tfoot/tr[2]/td[2]").text
        total_price = float(price.replace('$', '').replace(',', ''))
        return float(total_price)

    def get_lable_shopping_cart(self):
        # Lấy tiêu đề khi không có sản phẩm trong shopping cart
        return self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/p").text

    def get_message(self):
        #Lấy thông báo trong trang
        #Returns: str Thông báo

        message = self.driver.find_element(By.XPATH, "/html/body/div").text
        return message
