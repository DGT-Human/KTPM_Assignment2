class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to(self, x, y):
        self.driver.execute_script(f"window.scrollBy({x}, {y});")
