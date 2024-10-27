import time
from src.driver.driver import Driver
from src.pages.Navigation import Navigation

class TestNavigation(Driver):
    def test_navigation_desktop(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_desktops()
        navigation.show_all_desktops()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=20"
        assert navigation.get_success_show_all_desktops() == "list-group-item active"
        time.sleep(3)
        navigation.go_to_desktops()
        navigation.go_to_pc()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=20_26"
        assert navigation.get_success_go_to_pc() == "list-group-item active"
        time.sleep(3)
        navigation.go_to_desktops()
        navigation.go_to_mac()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=20_27"
        assert navigation.get_success_go_to_mac() == "list-group-item active"

    def test_navigation_laptops(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_laptops()
        navigation.show_all_laptops()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=18"
        assert navigation.get_success_show_all_laptops() == "list-group-item active"
        time.sleep(3)
        navigation.go_to_laptops()
        navigation.go_to_macs()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=18_46"
        assert navigation.get_success_go_to_macs() == "list-group-item active"
        time.sleep(3)
        navigation.go_to_laptops()
        navigation.go_to_windows_laptops()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=18_45"
        assert navigation.get_success_go_to_windows_laptops() == "list-group-item active"

    def test_navigation_components(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_components()
        navigation.show_all_components()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=25"
        assert navigation.get_success_show_all_components() == "list-group-item active"
        time.sleep(3)
        navigation.go_to_components()
        navigation.go_to_mice_and_trackballs()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=25_29"
        assert navigation.get_success_go_to_mice_and_trackballs() == "list-group-item active"
        time.sleep(3)
        navigation.go_to_components()
        navigation.go_to_monitors()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=25_28"
        assert navigation.get_success_go_to_monitors() == "list-group-item active"
        time.sleep(3)
        navigation.go_to_components()
        navigation.go_to_printers()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=25_30"
        assert navigation.get_success_go_to_printers() == "list-group-item active"
        time.sleep(3)
        navigation.go_to_components()
        navigation.go_to_scanners()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=25_31"
        assert navigation.get_success_go_to_scanners() == "list-group-item active"
        time.sleep(3)
        navigation.go_to_components()
        navigation.go_to_cameras()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=25_32"
        assert navigation.get_success_go_to_cameras() == "list-group-item active"
