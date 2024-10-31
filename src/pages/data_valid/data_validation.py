import time
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

# Lớp DataValidation chứa chức năng kiểm tra danh sách sản phẩm tìm thấy
class DataValidation(BasePage):

    # Phương thức hợp lệ tìm kiếm được kiểm tra kết quả
    def data_validation_show_product(self):
        time.sleep(5)
        # Tìm kiếm danh sách sản phẩm tìm thấy
        products = self.driver.find_elements(By.CSS_SELECTOR, '.product-thumb h4 a')
        product_names = [product.text for product in products]
        # return danh sách sản phẩm tìm thấy
        return product_names
