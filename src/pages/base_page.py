import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y});")

    def scroll_to_element(self, element):
        """Cuộn đến một phần tử cụ thể trên trang."""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)