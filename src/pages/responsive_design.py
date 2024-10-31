import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

# Lớp ResponsiveDesign chứa các chức năng của responsive design
class ResponsiveDesign(BasePage):

    # Phương thức set kích thước cửa sổ
    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)
        time.sleep(3)

    def check_element_displayed(self, by, value):
        """Kiểm tra xem phần tử có hiển thị không."""
        try:
            element = self.driver.find_element(by, value)
            return element.is_displayed()
        except Exception as e:
            print(f"Error finding element {value}: {e}")
            return False

# Phương thức kiểm tra xem phần tử có hiện thị hay không

    # Phần Top Nav
    def check_currency_dropdown_displayed(self):
        return self.check_element_displayed(By.ID, "form-currency")

    def check_phone_icon_displayed(self):
        return self.check_element_displayed(By.CSS_SELECTOR, ".fa-phone")

    def check_my_account_displayed(self):
        return self.check_element_displayed(By.CSS_SELECTOR, ".fa-user")

    def check_wishlist_displayed(self):
        return self.check_element_displayed(By.ID, "wishlist-total")

    def check_shopping_cart_displayed(self):
        return self.check_element_displayed(By.CSS_SELECTOR, ".fa-cart-shopping")

    def check_checkout_displayed(self):
        return self.check_element_displayed(By.CSS_SELECTOR, ".fa-share")

    # Phần Header
    def check_logo_displayed(self):
        return self.check_element_displayed(By.ID, "logo")

    def check_search_box_displayed(self):
        return self.check_element_displayed(By.NAME, "search")

    def check_cart_displayed(self):
        return self.check_element_displayed(By.ID, "header-cart")

    def check_cart_item_count_displayed(self):
        return self.check_element_displayed(By.CSS_SELECTOR, "#header-cart .btn-lg")

    def check_view_cart_link_displayed(self):
        return self.check_element_displayed(By.LINK_TEXT, "View Cart")

    # Phần Menu Categories
    def check_menu_displayed(self):
        return self.check_element_displayed(By.ID, "menu")

    def check_menu_categories_displayed(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/button").click()
        time.sleep(1)
        return self.check_element_displayed(By.CSS_SELECTOR, "#narbar-menu > ul")

    def check_list_product_displayed(self):
        return self.check_element_displayed(By.CSS_SELECTOR, ".product-thumb")

    # Phần Footer
    def check_footer_displayed(self):
        footer = self.driver.find_element(By.TAG_NAME, 'footer')
        return footer.find_elements(By.CLASS_NAME, 'col-sm-3')

    def check_footer_links_displayed(self):
        footer = self.driver.find_element(By.TAG_NAME, 'footer')
        return footer.find_elements(By.TAG_NAME, 'a')

    # Phần Product Details
    def check_images_product_detail_displayed(self):
        return self.check_element_displayed(By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(1) > div > a > img")

    def check_product_name_displayed(self):
        return self.check_element_displayed(By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(2) > h1")

    def check_product_detail_displayed(self):
        return self.check_element_displayed(By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(2) > ul")

    def check_product_description_displayed(self):
        return self.check_element_displayed(By.CSS_SELECTOR, "#content > ul > li:nth-child(2) > a")

    def check_specification_displayed(self):
        time.sleep(2)
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/ul/li[2]/a"))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/ul/li[2]/a").click()
        return self.check_element_displayed(By.CSS_SELECTOR, "#content > ul > li:nth-child(2) > a")

    def check_review_displayed(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/ul/li[3]/a").click()
        return self.check_element_displayed(By.CSS_SELECTOR, "#content > ul > li:nth-child(3) > a")
