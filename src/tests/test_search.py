from src.driver.driver import Driver
from src.pages.search import Search
from src.pages.data_valid.data_validation import DataValidation


# Lớp TestSearch kế thừa từ lớp Driver chứa các test case
class TestSearch(Driver):

    # Test case: Tìm kiếm sản phẩm hợp lệ
    def test_search_valid(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Search để thực hiện tìm kiếm
        search = Search(driver)

        # Tạo đối tượng Search để thực hiện tìm kiếm
        data_validation = DataValidation(driver)

        # Tìm kiếm sản phẩm với từ khóa "iPhone"
        search.search_product("iPhone")

        # Lấy danh sách sản phẩm tìm thấy
        product_name_search = data_validation.data_validation_show_product()
        product_name = ['iPhone']

        # So sánh kết quả với dự kiến
        assert product_name_search == product_name
        assert search.get_info_search() in "Search - iPhone"

    # Test case: Tìm kiếm sản phẩm với từ khóa rỗng
    def test_search_empty(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Search để thực hiện tìm kiếm
        search = Search(driver)

        # Tạo đối tượng DataValidation để kiểm tra kết quả
        data_validation = DataValidation(driver)

        # Tìm kiếm này để thực hiện tìm kiếm
        search.search_product("")

        # Lấy danh sách sản phẩm tìm thấy
        product_name_search = data_validation.data_validation_show_product()
        product_name = []

        # So sánh kết quả với dự kiến
        assert product_name_search == product_name
        assert search.get_info_search() in "Search"

    # Test case: Tìm kiếm này không thể tìm ra
    def test_search_invalid(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Search để thực hiện tìm kiếm
        search = Search(driver)

        # Tạo đối tượng DataValidation để kiểm tra kết quả
        data_validation = DataValidation(driver)

        # Tìm kiếm sản phẩm với từ khóa "invalid"
        search.search_product("invalid")

        # Lấy danh sách sản phẩm tìm thấy
        product_name_search = data_validation.data_validation_show_product()
        product_name = []

        # So sánh kết quả với dự kiến
        assert product_name_search == product_name
        assert search.get_info_search() in "Search - invalid"

    # Test case: Tìm kiếm sản phẩm với ký tự đặc biệt
    def test_search_special_characters(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Search để thực hiện tìm kiếm
        search = Search(driver)

        # Tạo đối tượng DataValidation để kiểm tra kết quả
        data_validation = DataValidation(driver)

        # Tìm kiếm sản phẩm với từ khóa "iPhone!@#"
        search.search_product("iPhone!@#")

        # Lấy danh sách sản phẩm tìm thấy
        product_name_search = data_validation.data_validation_show_product()
        product_name = []

        # So sánh kết quả với dự kiến
        assert product_name_search == product_name
        assert search.get_info_search() in "Search - iPhone!@#"

    # Test case: Tìm kiếm sản phẩm với ký tự %
    def test_search_special_characters_percent(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Search để thực hiện tìm kiếm
        search = Search(driver)

        # Tạo đối tượng DataValidation để kiểm tra kết quả
        data_validation = DataValidation(driver)

        # Tìm kiếm sản phẩm với từ khóa "%"
        search.search_product("%")

        # Lấy danh sách của sản phẩm tìm thấy
        product_name_search = data_validation.data_validation_show_product()
        product_name = []

        # So sánh kết quả với dự kiến
        assert product_name_search == product_name
        assert search.get_info_search() in "Search - %"

    # Test case: Tìm kiếm sản phẩm với danh mục cụ thể
    def test_search_with_category(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Search để thực hiện tìm kiếm
        search = Search(driver)

        # Tạo đối tượng DataValidation để kiểm tra kết quả
        data_validation = DataValidation(driver)

        # Tìm kiếm sản phẩm với từ khóa "i"
        search.search_product("i")

        # Chọn danh mục "Phones & PDAs"
        search.select_category("Phones & PDAs")

        # Nhấp vào nút tìm kiếm
        search.click_search_button()

        # Lấy danh sách sản phẩm tìm thấy
        product_name_search = data_validation.data_validation_show_product()
        product_name = ['iPhone']

        # So sánh kết quả với dự kiến
        assert product_name_search == product_name
        assert search.get_info_search() in "Search - i"

    # Test case: Tìm kiếm sản phẩm với danh mục cụ thể nhưng sản phẩm không hợp lệ
    def test_search_with_category_invalid_product(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Search để thực hiện tìm kiếm
        search = Search(driver)

        # Tạo đối tượng DataValidation để kiểm tra kết quả
        data_validation = DataValidation(driver)

        # Tìm kiếm sản phẩm với từ khóa "i"
        search.search_product("i")

        # Chọn danh mục "Tablets" (danh mục này không có sản phẩm hợp lệ với từ khóa "i")
        search.select_category("Tablets")

        # Nhấp vào nút tìm kiếm
        search.click_search_button()

        # Lấy danh sách sản phẩm tìm thấy
        product_name_search = data_validation.data_validation_show_product()

        # Danh sách sản phẩm dự kiến (trống vì không có sản phẩm hợp lệ)
        product_name = []

        # So sánh kết quả với dự kiến
        assert product_name_search == product_name
        assert search.get_info_search() in "Search - i"

    # Test case: Tìm kiếm sản phẩm với danh mục cụ thể nhưng từ khóa tìm kiếm không hợp lệ
    def test_search_with_category_invalid_search(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Search để thực hiện tìm kiếm
        search = Search(driver)

        # Tạo đối tượng DataValidation để kiểm tra kết quả
        data_validation = DataValidation(driver)

        # Tìm kiếm sản phẩm với từ khóa rỗng (không hợp lệ)
        search.search_product("")

        # Chọn danh mục "Tablets"
        search.select_category("Tablets")

        # Nhấp vào nút tìm kiếm
        search.click_search_button()

        # Lấy danh sách sản phẩm tìm thấy
        product_name_search = data_validation.data_validation_show_product()

        # Danh sách sản phẩm dự kiến (trống vì không có sản phẩm hợp lệ)
        product_name = []

        # So sánh kết quả với dự kiến
        assert product_name_search == product_name
        assert search.get_info_search() in "Search"


    # Test case: Tìm kiếm sản phẩm với từ khóa có độ dài tối đa
    def test_search_max_length(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Search để thực hiện tìm kiếm
        search = Search(driver)

        # Tạo đối tượng DataValidation để kiểm tra kết quả
        data_validation = DataValidation(driver)

        # Tạo từ khóa có độ dài tối đa (255 ký tự)
        max_length_query = "a" * 255

        # Tìm kiếm sản phẩm với từ khóa có độ dài tối đa
        search.search_product(max_length_query)

        # Lấy danh sách sản phẩm tìm thấy
        product_name_search = data_validation.data_validation_show_product()

        # So sánh kết quả với dự kiến (danh sách sản phẩm trống)
        assert product_name_search == []

    # Tìm kiếm sản phẩm trong mô tả sản phẩm
    def test_search_in_product_descriptions(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Search để thực hiện tìm kiếm
        search = Search(driver)

        # Tạo đối tượng DataValidation để kiểm tra kết quả
        data_validation = DataValidation(driver)

        # Tìm kiếm sản phẩm với từ khóa "iPhone"
        search.search_product("iPhone")

        # Tìm kiếm sản phẩm trong mô tả sản phẩm
        search.search_in_product_descriptions()

        # Nhấp vào nút tìm kiếm
        search.click_search_button()

        # Lấy danh sách sản phẩm tìm thấy
        product_name_search = data_validation.data_validation_show_product()

        # Danh sách sản phẩm dự kiến
        product_name = ['iPhone', 'iPod Nano', 'iPod Touch']

        # So sánh kết quả với dự kiến
        assert product_name_search == product_name
        assert search.get_info_search() in "Search - iPhone"

    # Tìm kiếm sản phẩm trong mô tả sản phẩm với từ khóa không hợp lệ với search_criteria
    def test_search_in_product_descriptions_invalid_with_search_criteria(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Search để thực hiện tìm kiếm
        search = Search(driver)

        # Tạo đối tượng DataValidation để kiểm tra kết quả
        data_validation = DataValidation(driver)

        # Tìm kiếm sản phẩm với từ khóa "iPhone"
        search.search_product("iPhone")

        # Kiểm tra tên sản phẩm tìm thấy
        assert search.get_info_search() in "Search - iPhone"

        # Tìm kiếm sản phẩm với từ khóa không hợp lệ
        search.search_product_criteria('invalid')

        # Tìm kiếm sản phẩm trong mô tả sản phẩm
        search.search_in_product_descriptions()

        # Nhấp vào nút tìm kiếm
        search.click_search_button()

        # Lấy danh sách sản phẩm tìm thấy
        product_name_search = data_validation.data_validation_show_product()

        # Danh sách sản phẩm dự kiến (trống)
        product_name = []

        # So sánh kết quả với dự kiến
        assert product_name_search == product_name
        assert search.get_info_search() in "Search - invalid"

    # Tìm kiếm sản phẩm trong danh mục con
    def test_search_in_subcategory(self, driver):
        # Truy cập trang chủ của opencart
        driver.get("http://localhost/opencart/upload/")

        # Tạo đối tượng Search để thực hiện tìm kiếm
        search = Search(driver)

        # Tạo đối tượng DataValidation để kiểm tra kết quả
        data_validation = DataValidation(driver)

        # Tìm kiếm sản phẩm với từ khóa "i"
        search.search_product("i")

        # Chọn danh mục "Components"
        search.select_category("Components")

        # Tìm kiếm sản phẩm trong danh mục con
        search.search_in_subcategory()

        # Nhấp vào nút tìm kiếm
        search.click_search_button()

        # Lấy danh sách sản phẩm tìm thấy
        product_name_search = data_validation.data_validation_show_product()

        # Danh sách sản phẩm dự kiến
        product_name = ['Apple Cinema 30"']

        # So sánh kết quả với dự kiến
        assert product_name_search == product_name
