import time
from src.driver.driver import Driver
from src.pages.responsive_design import ResponsiveDesign


class TestResponsive(Driver):

    def check_top_menu_elements(self, responsive):
        """Kiểm tra sự hiện diện của các phần tử trong menu trên cùng."""
        assert responsive.check_currency_dropdown_displayed(), "Currency dropdown is not displayed"
        assert responsive.check_phone_icon_displayed(), "Phone icon is not displayed"
        assert responsive.check_my_account_displayed(), "My Account icon is not displayed"
        assert responsive.check_wishlist_displayed(), "Wishlist is not displayed"
        assert responsive.check_shopping_cart_displayed(), "Shopping cart icon is not displayed"
        assert responsive.check_checkout_displayed(), "Checkout icon is not displayed"

    def check_header_elements(self, responsive):
        """Kiểm tra sự hiện diện của các phần tử trong header."""
        assert responsive.check_logo_displayed(), "Logo is not displayed"
        assert responsive.check_search_box_displayed(), "Search input is not displayed"
        assert responsive.check_cart_item_count_displayed(), "Menu is not displayed"
        assert responsive.check_cart_displayed(), "Cart icon is not displayed"
        assert responsive.check_checkout_displayed(), "Checkout icon is not displayed"

    def check_menu_categories(self, responsive):
        """Kiểm tra sự hiện diện của các phần tử trong menu categories."""
        assert responsive.check_menu_displayed(), "Menu is not displayed"
        assert responsive.check_menu_categories_displayed(), "Menu categories is not displayed"

    def check_list_product_home(self, responsive):
        """Kiểm tra sự hiện diện của các phần tử trong list product home."""
        assert responsive.check_list_product_displayed(), "List product home is not displayed"

    def check_footer_elements(self, responsive):
        """Kiểm tra sự hiện diện của các phần tử trong footer."""
        assert responsive.check_footer_displayed(), "Footer is not displayed"
        assert responsive.check_footer_links_displayed(), "Footer links is not displayed"

    def check_product_details(self, responsive):
        """Kiểm tra sự hiện diện của các phần tử trong product details."""
        assert responsive.check_images_product_detail_displayed(), "Images product detail is not displayed"
        assert responsive.check_product_name_displayed(), "Product name is not displayed"
        assert responsive.check_product_detail_displayed(), "Product detail is not displayed"
        assert responsive.check_product_description_displayed(), "Product description is not displayed"
        assert responsive.check_specification_displayed(), "Specification is not displayed"
        assert responsive.check_review_displayed(), "Review is not displayed"
    def test_responsive(self, driver):
        screen_sizes = [
            (1920, 1080),  # Desktop
            (1366, 768),  # Laptop
            (768, 1024),  # Tablet
            (375, 667),  # Mobile
        ]
        for width, height in screen_sizes:
            # Set kích thức cửa sổ
            driver.set_window_size(width, height)
            time.sleep(2)
            # Truy cập trang chủ
            driver.get("http://localhost/opencart/upload/")
            # Khởi tao đối tượng ResponsiveDesign
            responsive = ResponsiveDesign(driver)
            # Kiểm tra sự hiện diện của các phần tử trong responsive
            self.check_top_menu_elements(responsive)
            self.check_header_elements(responsive)
            if width > 768:
                assert responsive.check_menu_displayed(), "Menu is not displayed"
            else:
                self.check_menu_categories(responsive)
            self.check_list_product_home(responsive)
            self.check_footer_elements(responsive)
            driver.get("http://localhost/opencart/upload/index.php?route=product/product&language=en-gb&product_id=43")
            time.sleep(3)
            self.check_product_details(responsive)