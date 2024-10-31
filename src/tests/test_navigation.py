import time
from src.driver.driver import Driver
from src.pages.Navigation import Navigation

# Lớp TestNavigation này chứa các phương thức để thực hiện các kiểm tra chuyển trang (navigation)
class TestNavigation(Driver):

    # Test case: Kiểm tra navigation với desktops
    def test_navigation_desktop(self, driver):
        # Truy cập đến trang chủ
        driver.get("http://localhost/opencart/upload/")
        # Khởi tao đối tượng Navigation
        navigation = Navigation(driver)
        # Điều hướng trang show all desktops
        navigation.go_to_desktops()
        navigation.show_all_desktops()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=20"
        assert navigation.get_success_show_all_desktops() in "list-group-item active"
        assert navigation.get_label() in "Desktops"
        time.sleep(3)
        # Điều hướng trang desktops
        navigation.go_to_desktops()
        navigation.go_to_pc()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=20_26"
        assert navigation.get_success_go_to_pc() in "list-group-item active"
        assert navigation.get_label() in "Desktops"
        time.sleep(3)
        # Điều hướng trang mac
        navigation.go_to_desktops()
        navigation.go_to_mac()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=20_27"
        assert navigation.get_success_go_to_mac() in "list-group-item active"
        assert navigation.get_label() in "Desktops"

    # Test case: Kiểm tra navigation với laptops
    def test_navigation_laptops(self, driver):
        # Truy cập đến trang chủ
        driver.get("http://localhost/opencart/upload/")
        # Khởi tao đối tượng Navigation
        navigation = Navigation(driver)
        # Điều hướng trang show all laptops
        navigation.go_to_laptops()
        navigation.show_all_laptops()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=18"
        assert navigation.get_success_show_all_laptops() in "list-group-item active"
        assert navigation.get_label() in "Laptops & Notebooks"
        time.sleep(3)
        # Điều hướng trang macbooks
        navigation.go_to_laptops()
        navigation.go_to_macbooks()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=18_46"
        assert navigation.get_success_go_to_macbooks() in "list-group-item active"
        assert navigation.get_label() in "Laptops & Notebooks"
        time.sleep(3)
        # Điều hướng trang windows
        navigation.go_to_laptops()
        navigation.go_to_windows_laptops()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=18_45"
        assert navigation.get_success_go_to_windows_laptops() in "list-group-item active"
        assert navigation.get_label() in "Laptops & Notebooks"

    # Test case: Kiểm tra navigation với components
    def test_navigation_components(self, driver):
        # Truy cập đến trang chủ
        driver.get("http://localhost/opencart/upload/")
        # Khởi tao đối tượng Navigation
        navigation = Navigation(driver)
        # Điều hướng trang show all components
        navigation.go_to_components()
        navigation.show_all_components()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=25"
        assert navigation.get_success_show_all_components() in "list-group-item active"
        assert navigation.get_label() in "Components"
        time.sleep(3)
        # Điều hướng trang mice and trackballs
        navigation.go_to_components()
        navigation.go_to_mice_and_trackballs()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=25_29"
        assert navigation.get_success_go_to_mice_and_trackballs() in "list-group-item active"
        assert navigation.get_label() in "Components"
        time.sleep(3)
        # Điều hướng trang monitors
        navigation.go_to_components()
        navigation.go_to_monitors()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=25_28"
        assert navigation.get_success_go_to_monitors() in "list-group-item active"
        assert navigation.get_label() in "Components"
        time.sleep(3)
        # Điều hướng trang printers
        navigation.go_to_components()
        navigation.go_to_printers()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=25_30"
        assert navigation.get_success_go_to_printers() in "list-group-item active"
        assert navigation.get_label() in "Components"
        time.sleep(3)
        # Điều hướng trang scanners
        navigation.go_to_components()
        navigation.go_to_scanners()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=25_31"
        assert navigation.get_success_go_to_scanners() in "list-group-item active"
        assert navigation.get_label() in "Components"
        time.sleep(3)
        # Điều hướng trang web cameras
        navigation.go_to_components()
        navigation.go_to_web_cameras()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=25_32"
        assert navigation.get_success_go_to_web_cameras() in "list-group-item active"
        assert navigation.get_label() in "Components"

    # Test case: Kiểm tra navigation với tablets
    def test_navigation_tablets(self, driver):
        # Truy cập đến trang chủ
        driver.get("http://localhost/opencart/upload/")
        # Khởi tao đối tượng Navigation
        navigation = Navigation(driver)
        # Điều hướng trang tablets
        navigation.go_to_tablets()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=57"
        assert navigation.get_success_go_to_tablets() in "list-group-item active"
        assert navigation.get_label() in "Tablets"

    # Test case: Kiểm tra navigation với software
    def test_navigation_software(self, driver):
        # Truy cập đến trang chủ
        driver.get("http://localhost/opencart/upload/")
        # Khởi tao đối tượng Navigation
        navigation = Navigation(driver)
        # Điều h⑜ng trang software
        navigation.go_to_software()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=17"
        assert navigation.get_success_go_to_software() in "list-group-item active"
        assert navigation.get_label() in "Software"

    # Test case: Kiểm tra navigation với phones and PDAs
    def test_navigation_phones_and_PDAs(self, driver):
        # Truy cập định dạng trang chủ
        driver.get("http://localhost/opencart/upload/")
        # Khởi tao đối tượng Navigation
        navigation = Navigation(driver)
        # Điều hướng trang phones and PDAs
        navigation.go_to_phones_and_PDAs()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=24"
        assert navigation.get_success_go_to_phones_and_PDAs() in "list-group-item active"
        assert navigation.get_label() in "Phones & PDAs"

    # Test case: Kiểm tra navigation với cameras
    def test_navigation_cameras(self, driver):
        # Truy cập định dạng trang chủ
        driver.get("http://localhost/opencart/upload/")
        # Khởi tao đối tượng Navigation
        navigation = Navigation(driver)
        navigation.go_to_cameras()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=33"
        assert navigation.get_success_go_to_cameras() in "list-group-item active"
        assert navigation.get_label() in "Cameras"

    # Test case: Kiểm tra navigation với mp3 players
    def test_navigation_mp3_players(self, driver):
        # Truy cập định dạng trang chủ
        driver.get("http://localhost/opencart/upload/")
        # Khởi tao đối tượng Navigation
        navigation = Navigation(driver)
        # Điều hướng trang mp3 players
        navigation.go_to_mp3()
        navigation.go_to_show_all_mp3()
        # So sánh kết quả với dự kiến
        assert driver.current_url in "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=34"
        assert navigation.get_success_go_to_mp3() in "list-group-item active"
        assert navigation.get_label() in "MP3 Players"

