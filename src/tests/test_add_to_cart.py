import pytest

from src.driver.driver import Driver
from src.pages.Navigation import Navigation
from src.pages.add_to_cart import AddToCart
import random


# Định nghĩa lớp TestAddToCart chứa các test case
class TestAddToCart(Driver):

    # Test case: thêm 1 sản phẩm vs số lượng là 1
    def test_add_to_cart_one_quantity(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Navigation để điều hướng trang web
        navigation = Navigation(driver)
        # Điều hướng đến trang "Phones & PDAs"
        navigation.go_to_phones_and_PDAs()

        # Tạo đối tượng AddToCart để thêm sản phẩm vào giỏ hàng
        add_to_cart = AddToCart(driver)
        # Đến trang chi tiết sản phẩm của 'iPhone'
        add_to_cart.go_to_product("iPhone")
        # Thêm sản phẩm vào giỏ hàng
        add_to_cart.add_to_cart()

        # So sánh kết quả với dự kiến
        assert add_to_cart.get_message() in "Success: You have added " + f"{add_to_cart.get_product_name()}" + " to your shopping cart!"


    # Test case: thêm sản phẩm với số lượng là 0
    def test_add_to_cart_zero_quantity(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Navigation để điều hướng trang web
        navigation = Navigation(driver)
        # Điều hướng đến trang "Phones & PDAs"
        navigation.go_to_phones_and_PDAs()

        # Tạo đối tượng AddToCart để thêm sản phẩm vào giỏ hàng
        add_to_cart = AddToCart(driver)
        # Đến trang chi tiết sản phẩm của 'iPhone'
        add_to_cart.go_to_product("iPhone")
        # Đặt số lượng sản phẩm là 0
        add_to_cart.set_qty(0)
        # Thêm sản phẩm vào giỏ hàng
        add_to_cart.add_to_cart()

        # So sánh kết quả với dự kiến
        assert add_to_cart.get_message() in "Error: Please select a quantity", "Error message not displayed"


    # Test case: thêm sản phẩm với số lượng là -1
    def test_add_to_cart_negative_quantity(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Navigation để điều hướng trang web
        navigation = Navigation(driver)
        # Điều hướng đến trang "Phones & PDAs"
        navigation.go_to_phones_and_PDAs()

        # Tạo đối tượng AddToCart để thêm sản phẩm vào giỏ hàng
        add_to_cart = AddToCart(driver)
        # Đến trang chi tiết sản phẩm của 'iPhone'
        add_to_cart.go_to_product("iPhone")
        # Đặt số lượng sản phẩm là -1
        add_to_cart.set_qty(-1)
        # Thêm sản phẩm vào giỏ hàng
        add_to_cart.add_to_cart()

        # So sánh kết quả với dự kiến
        assert add_to_cart.get_message() in "Error: Please select a quantity" , "Error message not displayed"


    # Test case: thêm sản phẩm với số lượng là chuỗi "abc"
    def test_add_to_cart_invalid_quantity(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Navigation để điều hướng trang web
        navigation = Navigation(driver)
        # Điều hướng đến trang "Phones & PDAs"
        navigation.go_to_phones_and_PDAs()

        # Tạo đối tượng AddToCart để thêm sản phẩm vào giỏ hàng
        add_to_cart = AddToCart(driver)
        # Đến trang chi tiết sản phẩm của 'iPhone'
        add_to_cart.go_to_product("iPhone")
        # Đặt số lượng sản phẩm là chuỗi "abc"
        add_to_cart.set_qty("abc")
        # Thêm sản phẩm vào giỏ hàng
        add_to_cart.add_to_cart()

        # So sánh kết quả với dự kiến
        assert add_to_cart.get_message() in "Error: Please select a quantity", "Error message not displayed"

    # Test case: thêm sản phẩm với số lượng rỗng
    def test_add_to_cart_empty_quantity(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")
        # Tạo đối tượng Navigation để điều hướng trang web
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()

        # Tạo đối tượng AddToCart để thêm sản phẩm vào giỏ hàng
        add_to_cart = AddToCart(driver)
        add_to_cart.go_to_product("iPhone")
        add_to_cart.set_qty("")
        add_to_cart.add_to_cart()

        # So sánh kết quả với dự kiến
        assert add_to_cart.get_message() in "Error: Please select a quantity", "Error message not displayed"

    # Test case: thêm nhiều sản phẩm vào giỏ hàng với số lượng ngẫu nhiên

    def test_add_to_cart_multiple_products_random_quantity(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")
        # Tạo đối tượng Navigation để điều hướng trang web
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()

        # Tạo đối tượng AddToCart để thêm sản phẩm vào giỏ hàng
        add_to_cart = AddToCart(driver)
        # Danh sách sản phẩm cần thêm vào giỏ hàng
        product = ["iPhone", "HTC Touch HD", "Palm Treo Pro"]
        # Danh sách số lượng sản phẩm
        qty = []
        for name in product:
            # Tạo số lượng sản phẩm ngẫu nhiên từ 1 đến 12
            qty_random = random.randint(1, 12)
            add_to_cart.go_to_product(name)
            # Đặt số lượng sản phẩm là random
            add_to_cart.set_qty(qty_random)
            add_to_cart.add_to_cart()
            # Thêm số lượng random đó vào mảng
            qty.append(str(qty_random))
            # So sánh kết quả với dự kiến: Có thêm vào giỏ thành công không
            assert add_to_cart.get_message() in "Success: You have added " + f"{add_to_cart.get_product_name()}" + " to your shopping cart!"
            driver.back()
        # Click xem giỏ hàng nhanh (Xem View_fast_cart có đúng không)
        add_to_cart.click_view_fast_cart()
        # So sánh kết quả với dự kiến: danh sách số lượng sản phẩm nên trùng với danh sách số lượng sản phẩm ngẫu nhiên
        qty_values = add_to_cart.get_cart_product_qty_view_fast_cart()
        assert set(qty) == set(qty_values)

        # Click chuyển sang trang shopping cart
        add_to_cart.click_shopping_cart()
        # Tính tổng hóa đơn
        total_price = add_to_cart.calculate_cart_product_total_price()
        # So sánh kết quả với dự kiến: Tổng giá tính toán và tổng giá hiển thị bằng nhau
        assert round(add_to_cart.get_total_price_bill(), 1) == round(total_price, 1)


    # Test case: cập nhật số lượng của một sản phẩm trong giỏ hàng
    def test_update_cart_one_product(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")
        # Tạo đối tượng Navigation để điều hướng trang web
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()

        # Tạo đối tượng AddToCart để thêm sản phẩm vào giỏ hàng
        add_to_cart = AddToCart(driver)

        # Gọi hàm test thêm một sản phẩm vào giỏ hàng
        self.test_add_to_cart_one_quantity(driver)
        add_to_cart.click_shopping_cart()

        # Cập nhật số lượng của sản phẩm trong giỏ hàng
        add_to_cart.update_qty_multiple_products(3)

        # So sánh kết quả với dự kiến: thông báo "Success: You have modified your shopping cart!"
        assert add_to_cart.get_message() in "Success: You have modified your shopping cart!"
        #Tính tổng giá
        total_price = add_to_cart.calculate_cart_product_total_price()
        # So sánh kết quả với dự kiến: tổng giá tiền nên trùng với giá tiền hiển thị trên trang
        assert round(add_to_cart.get_total_price_bill(), 1) == round(total_price, 1)

    # Test case: cập nhật số lượng của nhiều sản phẩm trong giỏ hàng
    def test_update_cart_multiple_products(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")
        # Tạo đối tượng Navigation để điều hướng trang web
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()

        # Tạo đối tượng AddToCart để thêm sản phẩm vào giỏ hàng
        add_to_cart = AddToCart(driver)

        # Gọi hàm test thêm nhiều sản phẩm vào giỏ hàng với số lượng ngẫu nhiên
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        add_to_cart.update_qty_multiple_products(3)

        # So sánh kết quả với dự kiến: thông báo "Success: You have modified your shopping cart!"
        assert add_to_cart.get_message() in "Success: You have modified your shopping cart!"
        # Tính tổng giá hóa đơn
        total_price = add_to_cart.calculate_cart_product_total_price()
        # So sánh kết quả với dự kiến: tổng giá tiền nên trùng với giá tiền hiển thị trên trang
        assert round(add_to_cart.get_total_price_bill(), 1) == round(total_price, 1)

    # Test case: cập nhật số lượng là '0' của nhiều sản phẩm trong giỏ hàng (giống code trên)
    def test_update_cart_multiple_products_zero_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        add_to_cart.click_shopping_cart()
        add_to_cart.update_qty_multiple_products(0)
        assert add_to_cart.get_message() in "Success: You have modified your shopping cart!"
        total_price = add_to_cart.get_total_price_bill_without_product()
        assert total_price == 0

    # Test case: cập nhật số lượng là '-1' của nhiều sản phẩm trong giỏ hàng (giống code trên)
    def test_update_cart_multiple_products_negative_quantity(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        add_to_cart.click_shopping_cart()
        add_to_cart.update_qty_multiple_products(-3)
        assert add_to_cart.get_message() in "Success: You have modified your shopping cart!"
        total_price = add_to_cart.get_total_price_bill_without_product()
        assert total_price == 0

    # Test case: xoá sản phẩm khỏi giỏ hàng
    def test_remove_product_from_shopping_cart(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")
        # Tạo đối tượng Navigation để điều hướng trang web
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()

        # Tạo đối tượng AddToCart để thêm sản phẩm vào giỏ hàng
        add_to_cart = AddToCart(driver)

        # Gọi hàm test thêm nhiều sản phẩm vào giỏ hàng với số lượng ngẫu nhiên
        self.test_add_to_cart_multiple_products_random_quantity(driver)
        add_to_cart.click_shopping_cart()

        # Xoá sản phẩm khỏi giỏ hàng
        add_to_cart.remove_product_from_shopping_cart()
        # So sánh kết quả với dự kiến
        assert add_to_cart.get_lable_shopping_cart() in 'Your shopping cart is empty!'

    # Test case: xoá sản phẩm khỏi giỏ hàng trên trang xem nhanh giỏ hàng
    def test_remove_product_on_view_fast_cart(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        add_to_cart = AddToCart(driver)
        # Gọi hàm test thêm một sản phẩm vào giỏ hàng với số lượng nhất định
        self.test_add_to_cart_one_quantity(driver)

        # Click vào trang xem nhanh giỏ hàng
        add_to_cart.click_view_fast_cart()
        # Xoá sản phẩm khỏi giỏ hàng trên trang xem nhanh giỏ hàng
        add_to_cart.remove_product_on_view_fast_cart()
        # So sánh kết quả với dự kiến: thông báo "Success: You have removed an item from your shopping cart!"
        assert add_to_cart.get_message() in 'Success: You have removed an item from your shopping cart!'