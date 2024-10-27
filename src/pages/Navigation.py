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

    def get_success_show_all_desktops(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[1]')).get_attribute('class')

    def go_to_pc(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[1]/a").click()
        time.sleep(3)

    def get_success_go_to_pc(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[2]')).get_attribute('class')

    def go_to_mac(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[2]/a").click()
        time.sleep(3)

    def get_success_go_to_mac(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[3]')).get_attribute('class')

    def go_to_laptops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)

    def show_all_laptops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/a").click()
        time.sleep(3)

    def get_success_show_all_laptops(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[2]')).get_attribute('class')

    def go_to_macs (self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/div/ul/li[1]/a").click()
        time.sleep(3)

    def get_success_go_to_macs(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[3]')).get_attribute('class')

    def go_to_windows_laptops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/div/ul/li[2]/a").click()
        time.sleep(3)

    def get_success_go_to_windows_laptops(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[4]')).get_attribute('class')


    def go_to_components(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/a").click()
        time.sleep(3)

    def show_all_components(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/a").click()
        time.sleep(3)

    def get_success_show_all_components(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[3]')).get_attribute('class')

    def go_to_mice_and_trackballs(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[1]/a").click()
        time.sleep(3)

    def get_success_go_to_mice_and_trackballs(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[4]')).get_attribute('class')
    
    def go_to_monitors(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[2]/a").click()
        time.sleep(3)

    def get_success_go_to_monitors(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[5]')).get_attribute('class')

    def go_to_printers(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[3]/a").click()
        time.sleep(3)

    def get_success_go_to_printers(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[6]')).get_attribute('class')

    def go_to_scanners(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[4]/a").click()
        time.sleep(3)

    def get_success_go_to_scanners(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[7]')).get_attribute('class')

    def go_to_cameras(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[5]/a").click()
        time.sleep(3)

    def get_success_go_to_cameras(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[8]')).get_attribute('class')