import time
from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductPage(BasePage):

    def go_to_product(self, name):
        self.driver.find_element(By.LINK_TEXT, name).click()
        time.sleep(3)

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/form/div/button").click()
        time.sleep(3)

    def get_product_name(self):
        name = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/h1").text
        return name

    def get_product_price(self):
        price = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/ul[2]/li[1]/h2/span").text
        return price

    def set_qty(self, qty):
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/form/div/input[1]").clear()
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/form/div/input[1]").send_keys(qty)
        time.sleep(3)

    def click_shopping_cart(self):
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[4]/a/span").click()
        time.sleep(3)

    def click_view_cart(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/button").click()
        time.sleep(3)

    def get_cart_product_name(self):
        product_elements = self.driver.find_elements_by_xpath('//tbody/tr')
        product_names = [
            element.find_element(By.XPATH, './/td[@class="text-start"]/a').text
            for element in product_elements
        ]
        return product_names

    def get_cart_product_qty(self):
        qty_elements = self.driver.find_elements(By.XPATH, '//tbody/tr')
        qty_values = []
        for element in qty_elements:
            qty_text = element.find_element(By.XPATH,
                                            ".//td[@class='text-end'][1]").text.strip()
            if qty_text.startswith('x'):
                qty_number = qty_text[1:].strip()
                qty_values.append(qty_number)

        return qty_values

    def get_cart_product_price(self):
        prices = self.driver.find_elements(By.XPATH, '//tbody/tr')
        result = []
        for element in prices:
            price_text = element.find_element(By.XPATH,
                                              ".//td[@class='text-end'][1]").text.strip()
            if price_text.startswith('x'):
                qty_number = price_text[1:].strip()
            if price_text.startswith('$'):
                price_number = price_text[1:].strip()
                result.append(float(price_number) * float(qty_number))

        return result

    def get_total_price(self):
        total_price = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tfoot/tr[1]/td[2]").text
        total_price[1:].strip()
        return total_price

    def get_message(self):
        message = self.driver.find_element(By.XPATH, "/html/body/div").text
        return message