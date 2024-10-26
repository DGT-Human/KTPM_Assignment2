import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class Navigation(BasePage):
    def go_to_desktops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/a").click()
        time.sleep(3)

    def show_all_desktops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/a").click()
        time.sleep(3)

    def get_show_all_desktops(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[1]')).get_attribute('class')

    def go_to_pc(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[1]/a").click()
        time.sleep(3)

    def get_go_to_pc(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[2]')).get_attribute('class')

    def go_to_mac(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[2]/a").click()
        time.sleep(3)

    def get_go_to_mac(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[3]')).get_attribute('class')
    def go_to_laptops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)


