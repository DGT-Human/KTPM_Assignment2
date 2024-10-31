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
