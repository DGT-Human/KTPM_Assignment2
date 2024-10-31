import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import Select

# Lớp Search kế thừa từ lớp BasePage chứa các chức năng của thanh tìm kiếm
class Search(BasePage):

    # Phương thức tìm kiếm sản phẩm theo tên
    def search_product(self, product_name):
        time.sleep(3)
        # Tìm kiếm và xóa nội dung trong tìm kiếm
        self.driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/input").clear()
        # Nhập tên sản phẩm
        self.driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/input").send_keys(product_name)
        time.sleep(2)
        # Tìm kiếm và click vào nút tìm kiếm
        self.driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/button").click()
        time.sleep(3)

    # Phương thức lấy nội dung tìm kiếm
    def get_info_search(self):
        # Tìm kiếm và lấy nội dung
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/h1").text
        # Trả về nội dùng tìm
        return message

    # Phương thức chọn danh mục sản phẩm
    def select_category(self, category):
        #Select cho phần tử chứa danh mục sản phẩm
        select = Select(self.driver.find_element(By.ID, "input-category"))
        # Chọn danh mục sản phẩm theo tên
        select.select_by_visible_text(category)
        time.sleep(3)

    # Phương thức tìm kiếm sản phẩm trong mô tả sản phẩm
    def search_in_product_descriptions(self):
        # click vào nút tìm kiếm trong mô tả sản phẩm
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[1]/div/input").click()

    # Phương thức tìm kiếm sản phẩm trong danh mục con
    def search_in_subcategory(self):
        # click vào nút tìm kiếm trong danh mục con
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[2]/div/input").click()

    # Phương thức tìm kiếm sản phẩm theo tiêu chí sản phẩm
    def search_product_criteria(self, product_name):
        # Tìm kiếm và xóa nội dung trong tìm kiếm
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[1]/input").clear()
        # Nhập tên sản phẩm vào ô tìm kiếm sản phẩm
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[1]/input").send_keys(product_name)
        time.sleep(2)

    # Phương thức click vào nút tìm kiếm
    def click_search_button(self):
        # Click vào nút tìm kiếm
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[3]/div/button").click()