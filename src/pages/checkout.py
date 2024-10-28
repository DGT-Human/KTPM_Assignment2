import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class Checkout(BasePage):
    def click_shopping_cart(self):
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[4]/a").click()
        time.sleep(3)

    def click_checkout(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[3]/div[2]/a").click()
        time.sleep(3)

