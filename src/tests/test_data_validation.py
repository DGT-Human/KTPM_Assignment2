import time
from src.driver.driver import Driver
from src.pages.data_validation import DataValidation
from src.pages.Navigation import Navigation
class TestDataValidation(Driver):
    def test_data_validation_show_all_desktops(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_desktops()
        navigation.show_all_desktops()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['IMac', 'Desktop']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    def test_data_validation_show_all_laptops(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_laptops()
        navigation.show_all_laptops()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['MacBook', 'HP LP3065', 'MacBook Air', 'MacBook Pro', 'Sony VAIO']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    def test_data_validation_show_macs(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_laptops()
        navigation.go_to_macs()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['MacBook', 'MacBook Air', 'MacBook Pro']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    def test_data_validation_show_laptops_windows(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_laptops()
        navigation.go_to_windows_laptops()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['HP LP3065', 'Sony VAIO']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    def test_data_validation_show_monitors(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_components()
        navigation.go_to_monitors()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['Apple Cinema 30"', 'Samsung SyncMaster 941BW']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    def test_data_validation_show_all_components(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_components()
        navigation.show_all_components()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['Apple Cinema 30"', 'Samsung SyncMaster 941BW']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"


    def test_data_validation_show_all_tablets(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_tablets()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['Samsung Galaxy Tab 10.1']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    def test_data_validation_show_all_Phones_and_PDAs(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['HTC Touch HD', 'Palm Treo Pro', 'iPhone']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"