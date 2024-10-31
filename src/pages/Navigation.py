import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

# Lớp này chứa các phương thức để thực hiện các hành động chuyển trang trên trang web.
class Navigation(BasePage):

    # Phương thức chọn vào desktops
    def go_to_desktops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/a").click()
        time.sleep(3)

    # Phương thức chuyển trang hiển thị tất cả desktops
    def show_all_desktops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/a").click()
        time.sleep(3)

    # Phương thức xác nhận hành động chuyển trang hiển thị tất cả desktops
    def get_success_show_all_desktops(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[1]')).get_attribute('class')

    # Phương thức chuyển trang hiện thị PC
    def go_to_pc(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[1]/a").click()
        time.sleep(3)

    # Phương thức xác nhận hành động chuyển trang hiện thị PC
    def get_success_go_to_pc(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[2]')).get_attribute('class')

    # Phương thức chuyển trang hiện thị Mac
    def go_to_mac(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[2]/a").click()
        time.sleep(3)

    # Phương thức xác nhận hành động chuyển trang hiện thị Mac
    def get_success_go_to_mac(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[3]')).get_attribute('class')

    # Phương thức chọn laptop
    def go_to_laptops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)

    # Phương thức chuyển trang hiện thị tất cả laptop
    def show_all_laptops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/a").click()
        time.sleep(3)

    # Phương thức xác nhận hành động chuyển trang hiện thị tất cả laptop
    def get_success_show_all_laptops(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[2]')).get_attribute('class')

    # Phương thức chuyển trang hiện thị macbooks
    def go_to_macbooks(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/div/ul/li[1]/a").click()
        time.sleep(3)

    # Phương thức xác nhận hành động chuyển trang hiện thị macbooks
    def get_success_go_to_macbooks(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[3]')).get_attribute('class')

    # Phương thức chuyển trang hiện thị windows
    def go_to_windows_laptops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/div/ul/li[2]/a").click()
        time.sleep(3)

    # Phương thức xác nhận hành động chuyển trang hiện thị windows
    def get_success_go_to_windows_laptops(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[4]')).get_attribute('class')

    # Phương thức chọn vào components
    def go_to_components(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/a").click()
        time.sleep(3)

    # Phương thức chuyển trang hiện thị tất cả components
    def show_all_components(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/a").click()
        time.sleep(3)

    # Phương thức xác nhận hành động chuyển trang hiện thị tất cả components
    def get_success_show_all_components(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[3]')).get_attribute('class')

    # Phương thức chuyển trang hiện thị mice and trackballs
    def go_to_mice_and_trackballs(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[1]/a").click()
        time.sleep(3)

    # Phương thức xác nhận hành động chuyển trang hiện thị mice and trackballs
    def get_success_go_to_mice_and_trackballs(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[4]')).get_attribute('class')

    # Tương tự
    #     !
    #     V
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

    def go_to_web_cameras(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[5]/a").click()
        time.sleep(3)

    def get_success_go_to_web_cameras(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[8]')).get_attribute('class')

    def go_to_tablets(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[4]/a").click()
        time.sleep(3)

    def get_success_go_to_tablets(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[4]')).get_attribute('class')

    def go_to_software(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[5]/a").click()
        time.sleep(3)

    def get_success_go_to_software(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[5]')).get_attribute('class')

    def go_to_phones_and_PDAs(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[6]/a").click()
        time.sleep(3)

    def get_success_go_to_phones_and_PDAs(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[6]')).get_attribute('class')

    def go_to_cameras(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[7]/a").click()
        time.sleep(3)

    def get_success_go_to_cameras(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[7]')).get_attribute('class')

    def go_to_mp3(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[8]/a").click()
        time.sleep(3)

    def go_to_show_all_mp3(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[8]/div/a").click()
        time.sleep(3)

    def get_success_go_to_mp3(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[8]')).get_attribute('class')

    # Phương thức lấy label navigation
    def get_label(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/div/h2')).text