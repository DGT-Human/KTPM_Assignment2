# KTPM_Assignment-2_

## Giới thiệu:
- Do một số vấn đề về Web Demo trên mạng nên em đã cài đặt Web OpenCart về chạy Localhost.
- OpenCart là một nền tảng thương mại điện tử mã nguồn mở, cho phép bạn xây dựng và quản lý cửa hàng trực tuyến dễ dàng. Hướng dẫn này bao gồm các bước cài đặt OpenCart và cấu hình môi trường kiểm thử với Selenium.

## Yêu Cầu Hệ Thống

### 1. Yêu Cầu Phần Mềm
- **PHP**: Phiên bản 8.2 hoặc cao hơn.
- **Python**: Phiên bản 3.12 hoặc 3.9 trở lên
  
### 2. Yêu Cầu Cơ Sở Dữ Liệu
- **MySQL**: Phiên bản 5.5 hoặc cao hơn.

### 3. Yêu Cầu Web Server
- **Web Server**: Apache.

### 4. Yêu Cầu Kiểm Thử Selenium
- **Trình duyệt**: Microsoft Edge, Firefox hoặc bất kỳ trình duyệt nào hỗ trợ WebDriver.
- **WebDriver**: GeckoDriver cho Firefox hoặc EdgeDriver cho Microsoft Edge.
- **Ngôn ngữ lập trình**: Python Selenium.
- **Thư viện Selenium**: Cài đặt thư viện Selenium cho ngôn ngữ lập trình.

## Hướng dẫn cài đặt

### Bước 1: Cài đặt OpenCart
   - Truy cập trang web chính thức của OpenCart [openCart.com](https://www.opencart.com/) và tải phiên bản mới nhất về.
   - Và làm theo hướng dẫn ở [Youtube](https://www.youtube.com/watch?v=GftTTFm58d8)

### Bước 2: Cài đặt Selenium

1. **Cài đặt Python**:
   - Tải và cài đặt Python từ [python.org](https://www.python.org/downloads/).

2. **Cài đặt thư viện Selenium**:
   - Mở terminal và chạy lệnh sau để cài đặt thư viện Selenium:
     ```bash
     pip install selenium
     ```
3. **Tải và cài đặt WebDriver**:
   - Tải [GeckoDriver](https://github.com/mozilla/geckodriver/releases) cho Firefox hoặc [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) cho Microsoft Edge.
   - Đặt WebDriver vào thư mục đã thêm vào PATH hoặc chỉ định đường dẫn trong script của bạn.
     
4. **Chạy chương trình**
   - Clone source code về, vào folder tests sẽ có các file test các chức năng.
   - Ví dụ: test_login.py 
   ```bash
     python test_login.py
     ```
   Sẽ bắt đầu chạy file test_login

# Chức Năng Đã Kiểm Thử

## 1. Đăng nhập/Đăng xuất (Login/Logout)
- **Test case**: 6
- **Kết quả**: Tất cả đều Passed

## 2. Đăng ký (Register)
- **Test case**: 9
- **Kết quả**: Tất cả đều Passed

## 3. Thêm sản phẩm vào giỏ hàng (Add To Cart)
- **Test case**: 12
- **Kết quả**: 4 bị Fail

## 4. Kiểm tra dữ liệu hiển thị (Data Validation)
- **Test case**: 12
- **Kết quả**: 4 bị Fail

## 5. Tìm kiếm (Search)
- **Test case**: 12
- **Kết quả**: 1 bị Fail

## 6. Thanh toán (Checkout)
- **Test case**: 9
- **Kết quả**: Tất cả đều Passed

## 7. Điều hướng (Navigation)
- **Test case**: 8
- **Kết quả**: Tất cả đều Passed

## 8. Thiết kế responsive (Responsive Design)
- **Test case**: 1
- **Kết quả**: Passed


# Chức năng Kiểm thử

## 1. Chức năng Đăng nhập/Đăng xuất (Login/Logout)

- **TestLogin::test_login_valid**: Kiểm tra đăng nhập thành công với email và mật khẩu hợp lệ.
- **TestLogin::test_login_invalid_email**: Kiểm tra đăng nhập khi không nhập email.
- **TestLogin::test_login_invalid_password**: Kiểm tra đăng nhập khi không nhập mật khẩu.
- **TestLogin::test_login_email_not_exist**: Kiểm tra đăng nhập với email chưa đăng ký.
- **TestLogin::test_login_password_not_exist**: Kiểm tra đăng nhập với mật khẩu sai.
- **TestLogin::test_logout**: Kiểm tra đăng xuất thành công khi người dùng đã đăng nhập.

## 2. Chức năng Đăng ký (Register)

- **TestRegister::test_register_valid**: Kiểm tra đăng ký thành công với thông tin hợp lệ (email, mật khẩu, tên).
- **TestRegister::test_register_invalid_password**: Kiểm tra đăng ký khi mật khẩu để trống.
- **TestRegister::test_register_invalid_email**: Kiểm tra đăng ký với email không hợp lệ (ví dụ: thiếu dấu "@" hoặc định dạng sai).
- **TestRegister::test_register_invalid_name**: Kiểm tra đăng ký khi tên để trống.
- **TestRegister::test_register_email_exist**: Kiểm tra đăng ký với email đã tồn tại trong hệ thống.
- **TestRegister::test_register_password_long**: Kiểm tra đăng ký với mật khẩu dài hơn 20 ký tự.
- **TestRegister::test_register_password_short**: Kiểm tra đăng ký với mật khẩu ngắn hơn 4 ký tự.
- **TestRegister::test_register_name_long**: Kiểm tra đăng ký với tên dài hơn 32 ký tự.
- **TestRegister::test_register_policy_not_check**: Kiểm tra đăng ký khi không chấp nhận chính sách bảo mật (checkbox không được chọn).

## 3. Chức năng Thêm vào giỏ hàng (Add To Cart)

- **TestAddToCart::test_add_to_cart_one_quantity**: Kiểm tra thêm sản phẩm vào giỏ hàng với số lượng là 1.
- **TestAddToCart::test_add_to_cart_zero_quantity**: Kiểm tra thêm sản phẩm vào giỏ hàng với số lượng bằng 0.
- **TestAddToCart::test_add_to_cart_negative_quantity**: Kiểm tra thêm sản phẩm vào giỏ hàng với số lượng âm.
- **TestAddToCart::test_add_to_cart_invalid_quantity**: Kiểm tra thêm sản phẩm vào giỏ hàng với số lượng không hợp lệ (nhập ký tự chữ thay vì số).
- **TestAddToCart::test_add_to_cart_empty_quantity**: Kiểm tra thêm sản phẩm vào giỏ hàng khi không nhập số lượng.
- **TestAddToCart::test_add_to_cart_multiple_products_random_quantity**: Kiểm tra thêm nhiều sản phẩm vào giỏ hàng với số lượng ngẫu nhiên.
- **TestAddToCart::test_update_cart_one_product**: Kiểm tra cập nhật số lượng cho một sản phẩm trong giỏ hàng.
- **TestAddToCart::test_update_cart_multiple_products**: Kiểm tra cập nhật số lượng cho nhiều sản phẩm trong giỏ hàng.
- **TestAddToCart::test_update_cart_multiple_products_zero_quantity**: Kiểm tra cập nhật số lượng về 0 cho nhiều sản phẩm trong giỏ hàng.
- **TestAddToCart::test_update_cart_multiple_products_negative_quantity**: Kiểm tra cập nhật số lượng âm cho nhiều sản phẩm trong giỏ hàng.
- **TestAddToCart::test_remove_product_from_shopping_cart**: Kiểm tra xóa sản phẩm khỏi giỏ hàng.
- **TestAddToCart::test_remove_product_on_view_fast_cart**: Kiểm tra xóa sản phẩm nhanh chóng từ biểu tượng giỏ hàng.

## 4. Chức năng Kiểm tra dữ liệu hiển thị (Data Validation)

- **TestDataValidation::test_data_validation_show_all_desktops**: Kiểm tra danh sách sản phẩm hiển thị cho tất cả các sản phẩm desktop.
- **TestDataValidation::test_data_validation_show_macbooks**: Kiểm tra danh sách sản phẩm hiển thị cho MacBook.
- **TestDataValidation::test_data_validation_show_laptops_windows**: Kiểm tra danh sách sản phẩm hiển thị cho laptop Windows.
- **TestDataValidation::test_data_validation_show_all_components**: Kiểm tra danh sách sản phẩm hiển thị cho tất cả các thành phần (components).
- **TestDataValidation::test_data_validation_show_desktops_mac**: Kiểm tra danh sách sản phẩm Mac trong danh mục Desktops.
- **TestDataValidation::test_data_validation_show_desktops_pc**: Kiểm tra danh sách sản phẩm PC trong danh mục Desktops.
- **TestDataValidation::test_data_validation_show_all_laptops**: Kiểm tra danh sách sản phẩm cho tất cả laptop.
- **TestDataValidation::test_data_validation_show_monitors**: Kiểm tra danh sách sản phẩm cho màn hình.
- **TestDataValidation::test_data_validation_show_all_tablets**: Kiểm tra danh sách sản phẩm cho tất cả máy tính bảng.
- **TestDataValidation::test_data_validation_show_all_Phones_and_PDAs**: Kiểm tra danh sách sản phẩm cho tất cả điện thoại và PDAs.
- **TestDataValidation::test_data_validation_show_all_cameras**: Kiểm tra danh sách sản phẩm cho tất cả máy ảnh.
- **TestDataValidation::test_data_validation_show_all_mp3_players**: Kiểm tra danh sách sản phẩm cho tất cả máy nghe nhạc MP3.

## 5. Chức năng Tìm kiếm (Search)

- **TestSearch::test_search_valid**: Tìm kiếm sản phẩm với từ khóa hợp lệ.
- **TestSearch::test_search_empty**: Tìm kiếm khi không nhập từ khóa.
- **TestSearch::test_search_invalid**: Tìm kiếm với từ khóa không tồn tại.
- **TestSearch::test_search_special_characters**: Tìm kiếm với từ khóa chứa ký tự đặc biệt.
- **TestSearch::test_search_special_characters_percent**: Tìm kiếm với từ khóa chứa ký tự phần trăm (%).
- **TestSearch::test_search_with_category**: Tìm kiếm sản phẩm trong danh mục cụ thể.
- **TestSearch::test_search_with_category_invalid_product**: Tìm kiếm sản phẩm không tồn tại trong danh mục.
- **TestSearch::test_search_with_category_invalid_search**: Tìm kiếm với danh mục và từ khóa không hợp lệ.
- **TestSearch::test_search_max_length**: Tìm kiếm với từ khóa có độ dài tối đa.
- **TestSearch::test_search_in_product_descriptions**: Tìm kiếm trong mô tả sản phẩm.
- **TestSearch::test_search_in_product_descriptions_invalid_with_search_criteria**: Tìm kiếm trong mô tả sản phẩm với tiêu chí tìm kiếm không hợp lệ.
- **TestSearch::test_search_in_subcategory**: Tìm kiếm trong danh mục con.

## 6. Chức năng Thanh toán (Checkout)

- **TestCheckout::test_checkout_guest**: Thanh toán dưới dạng khách hàng không đăng ký.
- **TestCheckout::test_checkout_register**: Thanh toán và đăng ký tài khoản mới.
- **TestCheckout::test_checkout_with_login**: Thanh toán khi người dùng đã đăng nhập.
- **TestCheckout::test_checkout_guest_invalid**: Thanh toán với thông tin không hợp lệ dưới dạng khách hàng không đăng ký.
- **TestCheckout::test_checkout_register_invalid**: Thanh toán với thông tin không hợp lệ khi đăng ký tài khoản mới.
- **TestCheckout::test_checkout_register_password_invalid**: Thanh toán với mật khẩu không hợp lệ khi đăng ký.
- **TestCheckout::test_checkout_register_password_to_long**: Thanh toán với mật khẩu dài quá mức khi đăng ký.
- **TestCheckout::test_checkout_register_password_to_short**: Thanh toán với mật khẩu ngắn quá mức khi đăng ký.
- **TestCheckout::test_checkout_register_email_exist**: Thanh toán với email đã tồn tại.

## 7. Chức năng Điều hướng (Navigation)

- **TestNavigation::test_navigation_desktop**: Điều hướng đến danh mục Desktops.
- **TestNavigation::test_navigation_laptops**: Điều hướng đến danh mục Laptops.
- **TestNavigation::test_navigation_components**: Điều hướng đến danh mục Components.
- **TestNavigation::test_navigation_tablets**: Điều hướng đến danh mục Tablets.
- **TestNavigation::test_navigation_software**: Điều hướng đến danh mục Software.
- **TestNavigation::test_navigation_phones_and_PDAs**: Điều hướng đến danh mục Phones & PDAs.
- **TestNavigation::test_navigation_cameras**: Điều hướng đến danh mục Cameras.
- **TestNavigation::test_navigation_mp3_players**: Điều hướng đến danh mục MP3 Players.

## 8. Chức năng Thiết kế Responsive (Responsive Design)

- **TestResponsive::test_responsive**: Kiểm thử khả năng hiển thị của trang web trên các thiết bị khác nhau.
