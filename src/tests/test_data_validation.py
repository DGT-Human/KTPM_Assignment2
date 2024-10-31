from src.driver.driver import Driver
from src.pages.data_valid.data_validation import DataValidation
from src.pages.Navigation import Navigation

# Lớp TestDataValidation chứa các hàm test case (DataValidation) cho lớp Navigation
class TestDataValidation(Driver):

    # Test case: Kiểm tra hiển thị tất cả sản phẩm trong show all desktops
    def test_data_validation_show_all_desktops(self, driver):
        # Truy cập đến trang chủ
        driver.get("http://localhost/opencart/upload/")
        # Khởi tao đối tượng Navigation
        navigation = Navigation(driver)
        # Điều hướng trang show all desktops
        navigation.go_to_desktops()
        navigation.show_all_desktops()
        # Khởi tạo đối tượng DataValidation
        data_validation = DataValidation(driver)
        # Lấy kết quả danh sách sản phẩm
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['IMac']
        # So sánh kết quả với kết quả mong đợi
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    # Test case: Kiểm tra hiện thị tất cả san pham mac
    def test_data_validation_show_desktops_mac(self, driver):
        # Truy cập đến trang chủ
        driver.get("http://localhost/opencart/upload/")
        # Khởi tao đối tượng Navigation
        navigation = Navigation(driver)
        # Điều hướng trang mac
        navigation.go_to_desktops()
        navigation.go_to_mac()
        # Khởi tạo đối tượng DataValidation
        data_validation = DataValidation(driver)
        # Lấy kết quả danh sách sản phẩm
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['iMac']
        # So sánh kết quả với kết quả mong đợi
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    # Test case: Kiểm tra hiện thị tất cả san pham pc
    def test_data_validation_show_desktops_pc(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_desktops()
        navigation.go_to_pc()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = []
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    # Test case: Kiểm tra hiện thị tất cả sản phẩm laptop
    def test_data_validation_show_all_laptops(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_laptops()
        navigation.show_all_laptops()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['MacBook', 'HP LP3065', 'MacBook Air', 'MacBook Pro', 'Sony VAIO']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    # Test case: Kiểm tra hiện thị tất cả sản phẩm macbooks
    def test_data_validation_show_macbooks(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_laptops()
        navigation.go_to_macbooks()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['MacBook', 'MacBook Air', 'MacBook Pro']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    # Test case: Kiểm tra hiện thị tất cả sản phẩm laptop windows
    def test_data_validation_show_laptops_windows(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_laptops()
        navigation.go_to_windows_laptops()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['HP LP3065', 'Sony VAIO']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    # Test case: Kiểm tra hiện thị tất cả sản phẩm monitor
    def test_data_validation_show_monitors(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_components()
        navigation.go_to_monitors()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['Apple Cinema 30"', 'Samsung SyncMaster 941BW']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    # Test case: Kiểm tra hiện thị tất cả sản phẩm components
    def test_data_validation_show_all_components(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_components()
        navigation.show_all_components()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['Apple Cinema 30"', 'Samsung SyncMaster 941BW']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    # Test case: Kiểm tra hiện thị tất cả sản phẩm tablet
    def test_data_validation_show_all_tablets(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_tablets()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['Samsung Galaxy Tab 10.1']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    # Test case: Kiểm tra hiện thị tất cả sản phẩm Phones and PDAs
    def test_data_validation_show_all_Phones_and_PDAs(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_phones_and_PDAs()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['HTC Touch HD', 'Palm Treo Pro', 'iPhone']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    # Test case: Kiểm tra hiện thị tất cả sản phẩm Cameras
    def test_data_validation_show_all_cameras(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_cameras()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['Nikon D300', 'Canon EOS 5D']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"

    # Test case: Kiểm tra hiện thị tất cả sản phẩm mp3 players
    def test_data_validation_show_all_mp3_players(self, driver):
        driver.get("http://localhost/opencart/upload/")
        navigation = Navigation(driver)
        navigation.go_to_mp3()
        navigation.go_to_show_all_mp3()
        data_validation = DataValidation(driver)
        displayed_product_names = data_validation.data_validation_show_product()
        expected_product_names = ['iPod Classic', 'iPod Nano', 'iPod Shuffle', 'iPod Touch']
        assert set(displayed_product_names) == set(expected_product_names), f"Expected {expected_product_names}, but got {displayed_product_names}"