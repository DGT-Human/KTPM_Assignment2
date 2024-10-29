import time
from selenium.webdriver.common.by import By
from .base_page import BasePage


class AddToCart(BasePage):

    def go_to_product(self, name):
        self.driver.find_element(By.LINK_TEXT, name).click()
        time.sleep(3)

    def add_to_cart(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/form/div/button").click()
        time.sleep(3)

    def get_product_name(self):
        name = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/h1").text
        return name

    def get_product_price(self):
        price = self.driver.find_element(By.XPATH,
                                         "/html/body/main/div[2]/div/div/div[1]/div[2]/ul[2]/li[1]/h2/span").text
        return price

    def set_qty(self, qty):
        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/form/div/input[1]").clear()
        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/form/div/input[1]").send_keys(qty)
        time.sleep(3)

    def click_shopping_cart(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[4]/a/span").click()
        time.sleep(3)

    def click_view_items(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/button").click()
        time.sleep(3)

    def update_qty_multiple_products(self, qty):
        product_rows = self.driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr")
        if qty == 0 or qty < 0:
            for _ in range(len(product_rows)):
                quantity_input = self.driver.find_element(By.XPATH, ".//input[@name='quantity']")
                quantity_input.clear()
                quantity_input.send_keys(str(qty))
                time.sleep(1)
                update_button = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[4]/form/div/button[1]")
                update_button.click()
                time.sleep(2)
            return
        else:
            for _ in range(len(product_rows)):
                product_rows = self.driver.find_elements(By.XPATH,
                                                         "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr")
                product_row = product_rows[_]
                quantity_input = product_row.find_element(By.XPATH, ".//input[@name='quantity']")
                quantity_input.clear()
                quantity_input.send_keys(str(qty))
                time.sleep(1)
                update_button = product_row.find_element(By.XPATH, ".//button[1]")
                update_button.click()
                time.sleep(2)

    def remove_product_from_cart(self):
        product_rows = self.driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr")
        for _ in range(len(product_rows)):
            update_button = self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr/td[4]/form/div/button[2]")
            update_button.click()
            time.sleep(2)

    def remove_product_on_view_items(self):
        self.driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/ul/li/table/tbody/tr[1]/td[5]/form/button").click()
        time.sleep(2)

    def get_cart_product_name(self):
        product_elements = self.driver.find_elements_by_xpath('//tbody/tr')
        product_names = [
            element.find_element(By.XPATH, './/td[@class="text-start"]/a').text
            for element in product_elements
        ]
        return product_names

    def get_cart_product_qty_view_item(self):
        qty_elements = self.driver.find_elements(By.XPATH,'//tbody/tr')
        qty_values = []
        for element in qty_elements:
            qty_text = element.find_element(By.XPATH,".//td[@class='text-end'][1]").text.strip()
            if qty_text.startswith('x'):
                qty_number = qty_text[1:].strip()
                qty_values.append(qty_number)

        return qty_values

    def get_cart_product_total_price(self):
        rows = self.driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr")
        total_price = 0

        for row in rows:
            quantity = row.find_element(By.XPATH, ".//input[1]").get_attribute('value')
            if quantity == '':
                quantity = 0  #
            unit_price_element = row.find_element(By.XPATH, ".//td[contains(@class, 'text-end')][1]")
            unit_price = unit_price_element.text.strip()
            if unit_price == '':
                unit_price = 0.0
            else:
                unit_price = float(unit_price.replace('$', '').replace(',', ''))  # Xử lý ký tự '$' và ',' nếu có

            # print(quantity, unit_price)
            total_price += int(quantity) * unit_price

        return total_price

    def get_total_price_bill(self):
        total_price = self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[1]/div/table/tfoot/tr[4]/td[2]").text
        total_price = float(total_price.replace('$', '').replace(',', ''))
        return float(total_price)

    def get_price_bill(self):
        price = self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[1]/div/table/tfoot/tr[2]/td[2]").text
        total_price = float(price.replace('$', '').replace(',', ''))
        return float(total_price)

    def get_message(self):
        message = self.driver.find_element(By.XPATH, "/html/body/div").text
        return message
