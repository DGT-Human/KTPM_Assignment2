import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import Select

class Checkout(BasePage, Select):
    def click_shopping_cart(self):
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[4]/a").click()
        time.sleep(3)

    def click_checkout(self):
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[3]/div[2]/a"))
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[3]/div[2]/a").click()
        time.sleep(3)

    def click_guest_checkout(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[1]/div[1]/div[2]").click()
        time.sleep(3)

    def set_checkout_guest_checkbox(self, firstname = None, lastname = None, email = None, company = None, address1 = None, address2 = None, city = None,  postcode = None, country = None, region = None, wish = False):
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[1]/input").send_keys(firstname)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[2]/input").send_keys(lastname)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[3]/input").send_keys(email)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[1]/input").send_keys(company)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[2]/input").send_keys(address1)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[3]/input").send_keys(address2)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[4]/input").send_keys(city)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[5]/input").send_keys(postcode)
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[6]/select"))
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[6]/select").click()
        time.sleep(2)
        Select(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[6]/select")).select_by_visible_text(country)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[6]/select").click()
        Select(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[7]/select")).select_by_visible_text(region)
        if wish:
            self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/div[2]/div/div[1]/input").click()

    def set_checkout_register_checkbox(self, firstname, lastname, email, company, address1, address2, city,  postcode, country, region, password, wish = False, read = False):
        self.set_checkout_guest_checkbox(firstname, lastname, email, company, address1, address2, city,  postcode, country, region, wish)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input").send_keys(password)
        if read:
            self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/div[2]/div/div[2]/input").click()
        time.sleep(3)

    def click_continue_button(self):
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/div[2]/div/button").click()
        time.sleep(3)

    def choose_shipping_method(self):
        time.sleep(3)
        self.scroll_to_element(self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div[1]/fieldset/div[1]/button"))
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[1]/fieldset/div[1]/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[1]/input").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/button").click()
        time.sleep(1)

    def choose_payment_method(self):
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div[2]/fieldset/div[1]/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[1]/input").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/button").click()
        time.sleep(1)

    def confirm_order(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button").click()
        time.sleep(3)

    def get_message(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/h1").text
        return message

    def get_error_message_email_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/div/div").text
        return message

    def get_error_message_password_not_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/div[1]/div[1]/fieldset/div/div/div").text
        return message

    def get_error_message_fname_not_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[1]/div").text
        return message

    def get_error_message_lname_not_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[2]/div").text
        return message

    def get_error_message_address_not_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[2]/div").text
        return message

    def get_error_message_city_not_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[4]/div").text
        return message

    def get_error_message_email_not_exist(self):
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[3]/div").text
        return message

    def get_error_policy(self):
        message = self.driver.find_element(By.XPATH, "/html/body/div/div").text
        return message