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
        assert navigation.get_show_all_desktops() == "list-group-item active"
        time.sleep(3)
        navigation.go_to_desktops()
        navigation.go_to_pc()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=20_26"
        assert navigation.get_go_to_pc() == "list-group-item active"
        time.sleep(3)
        navigation.go_to_desktops()
        navigation.go_to_mac()
        assert driver.current_url == "http://localhost/opencart/upload/index.php?route=product/category&language=en-gb&path=20_27"
        assert navigation.get_go_to_mac() == "list-group-item active"