import time
from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    def go_to_login(self):
        self.driver.get("http://localhost/opencart/upload/")
        self.driver.find_element(By.XPATH,
                                 "//a[contains(@class, 'dropdown-toggle') and contains(., 'My Account')]").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]").click()
        time.sleep(10)

    def login(self, email, password):
        email_input = self.driver.find_element(By.ID, "input-email")
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.ID, "input-password")
        password_input.send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]").click()
        time.sleep(3)

    def logout(self):
        self.driver.find_element(By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(., 'My Account')]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/a").click()

    def get_message_login(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/h2[1]").text
        return message

    def get_error_message(self):
        return self.driver.find_element(By.XPATH, "/html/body/div").text



