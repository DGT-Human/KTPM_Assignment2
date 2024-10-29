from src.driver.driver import Driver
from src.pages.Navigation import Navigation
from src.pages.add_to_cart import AddToCart
import random


class TestAddToCart(Driver):
    def test_add_to_cart_one_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        add_to_cart.go_to_product("iPhone")
        add_to_cart.add_to_cart()
        assert "Success: You have added " + f"{add_to_cart.get_product_name()}" + " to your shopping cart!" in add_to_cart.get_message()


    def test_add_to_cart_zero_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        add_to_cart.go_to_product("iPhone")
        add_to_cart.set_qty(0)
        add_to_cart.add_to_cart()
        assert "Error: Please select a quantity" in add_to_cart.get_message(), "Error message not displayed"

    def test_add_to_cart_negative_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        add_to_cart.go_to_product("iPhone")
        add_to_cart.set_qty(-1)
        add_to_cart.add_to_cart()
        assert "Error: Please select a quantity" in add_to_cart.get_message(), "Error message not displayed"

    def test_add_to_cart_invalid_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        add_to_cart.go_to_product("iPhone")
        add_to_cart.set_qty("abc")
        add_to_cart.add_to_cart()
        assert "Error: Please select a quantity" in add_to_cart.get_message(), "Error message not displayed"

    def test_add_to_cart_empty_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        add_to_cart.go_to_product("iPhone")
        add_to_cart.set_qty("")
        add_to_cart.add_to_cart()
        assert "Error: Please select a quantity" in add_to_cart.get_message(), "Error message not displayed"

    def test_add_to_cart_multiple_products_random_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        product = ["iPhone", "HTC Touch HD", "Palm Treo Pro"]
        qty = []
        for name in product:
            qty_random = random.randint(1, 12)
            add_to_cart.go_to_product(name)
            add_to_cart.set_qty(qty_random)
            add_to_cart.add_to_cart()
            qty.append(str(qty_random))
            assert "Success: You have added " + f"{add_to_cart.get_product_name()}" + " to your shopping cart!" in add_to_cart.get_message()
            driver.back()
        add_to_cart.click_view_items()
        qty_values = add_to_cart.get_cart_product_qty_view_item()
        assert set(qty) == set(qty_values)

    def test_add_to_cart_multiple_products_total_price(self, driver):
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        add_to_cart = AddToCart(driver)
        add_to_cart.click_shopping_cart()
        total_price = add_to_cart.get_cart_product_total_price()
        assert round(add_to_cart.get_total_price_bill(), 1) == round(total_price, 1)

    def test_update_cart_one_product(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        self.test_add_to_cart_one_quantity(driver)
        add_to_cart.click_shopping_cart()
        add_to_cart.update_qty_multiple_products(3)
        assert "Success: You have modified your shopping cart!" in add_to_cart.get_message()
        total_price = add_to_cart.get_cart_product_total_price()
        assert round(add_to_cart.get_total_price_bill(), 1) == round(total_price, 1)

    def test_update_cart_multiple_products(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        add_to_cart.click_shopping_cart()
        add_to_cart.update_qty_multiple_products(3)
        assert "Success: You have modified your shopping cart!" in add_to_cart.get_message()
        total_price = add_to_cart.get_cart_product_total_price()
        assert round(add_to_cart.get_total_price_bill(), 1) == round(total_price, 1)

    def test_update_cart_multiple_products_zero_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        add_to_cart.click_shopping_cart()
        add_to_cart.update_qty_multiple_products(0)
        assert "Success: You have modified your shopping cart!" in add_to_cart.get_message()
        total_price = add_to_cart.get_price_bill()
        assert total_price == 0

    def test_update_cart_multiple_products_negative_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        add_to_cart.click_shopping_cart()
        add_to_cart.update_qty_multiple_products(-3)
        assert "Success: You have modified your shopping cart!" in add_to_cart.get_message()
        total_price = add_to_cart.get_price_bill()
        assert total_price == 0

    def test_remove_product_from_cart(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        self.test_add_to_cart_one_quantity(driver)
        add_to_cart.click_shopping_cart()
        add_to_cart.remove_product_from_cart()
        total_price = add_to_cart.get_price_bill()
        assert total_price == 0

    def test_remove_product_on_view_items(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        self.test_add_to_cart_one_quantity(driver)
        add_to_cart.click_view_items()
        add_to_cart.remove_product_on_view_items()
        assert 'Success: You have removed an item from your shopping cart!' in add_to_cart.get_message()