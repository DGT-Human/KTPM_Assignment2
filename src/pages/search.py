import time
from selenium.webdriver.common.by import By
from .base_page import BasePage


class Search(BasePage):
    def search_product(self, product_name):
        self.driver.find_element(By.NAME, "search").clear()
        self.driver.find_element(By.NAME, "search").send_keys(product_name)
        self.driver.find_element(By.NAME, "search").submit()
        time.sleep(3)