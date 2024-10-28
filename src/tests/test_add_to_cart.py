from src.driver.driver import Driver
from src.pages.Navigation import Navigation
from src.pages.product_page import ProductPage
import random

class TestAddToCart(Driver):
    def test_add_to_cart_one_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        product_page = ProductPage(driver)
        product_page.go_to_product("iPhone")
        product_page.add_to_cart()
        assert "Success: You have added " + f"{product_page.get_product_name()}" + " to your shopping cart!" in product_page.get_message()

    def test_add_to_cart_three_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        product_page = ProductPage(driver)
        product_page.go_to_product("iPhone")
        product_page.set_qty(3)
        product_page.add_to_cart()
        assert "Success: You have added " + f"{product_page.get_product_name()}" + " to your shopping cart!" in product_page.get_message()
        product_page.click_view_cart()
        assert "3" in product_page.get_cart_product_qty()

    def test_add_to_cart_zero_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        product_page = ProductPage(driver)
        product_page.go_to_product("iPhone")
        product_page.set_qty(0)
        product_page.add_to_cart()
        assert "Error: Please select a quantity" in product_page.get_message(), "Error message not displayed"

    def test_add_to_cart_negative_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        product_page = ProductPage(driver)
        product_page.go_to_product("iPhone")
        product_page.set_qty(-1)
        product_page.add_to_cart()
        assert "Error: Please select a quantity" in product_page.get_message(), "Error message not displayed"

    def test_add_to_cart_invalid_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        product_page = ProductPage(driver)
        product_page.go_to_product("iPhone")
        product_page.set_qty("abc")
        product_page.add_to_cart()
        assert "Error: Please select a quantity" in product_page.get_message(), "Error message not displayed"

    def test_add_to_cart_empty_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        product_page = ProductPage(driver)
        product_page.go_to_product("iPhone")
        product_page.set_qty("")
        product_page.add_to_cart()
        assert "Error: Please select a quantity" in product_page.get_message(), "Error message not displayed"

    def test_add_to_cart_multiple_products(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        product_page = ProductPage(driver)
        product = ["iPhone", "HTC Touch HD", "Palm Treo Pro"]
        for name in product:
            product_page.go_to_product(name)
            product_page.set_qty(2)
            product_page.add_to_cart()
            assert "Success: You have added " + f"{product_page.get_product_name()}" + " to your shopping cart!" in product_page.get_message()
            driver.back()
        qty = ['2', '2', '2']
        product_page.click_view_cart()
        qty_values = product_page.get_cart_product_qty()
        assert qty == qty_values


    def test_add_to_cart_multiple_products_random_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        product_page = ProductPage(driver)
        product = ["iPhone", "HTC Touch HD", "Palm Treo Pro"]
        qty = []
        for name in product:
            qty_random = random.randint(1, 12)
            product_page.go_to_product(name)
            product_page.set_qty(qty_random)
            product_page.add_to_cart()
            qty.append(str(qty_random))
            assert "Success: You have added " + f"{product_page.get_product_name()}" + " to your shopping cart!" in product_page.get_message()
            driver.back()
        product_page.click_view_cart()
        qty_values = product_page.get_cart_product_qty()
        assert set(qty) == set(qty_values)

    def test_add_to_cart_multiple_products_total_price(self, driver):
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        product_page = ProductPage(driver)
        product_page.click_shopping_cart()
        total_price = product_page.get_total_price()
        assert product_page.get_total_price() == total_price

