import pytest
from selenium import webdriver


class Driver():
    @pytest.fixture(scope="function")
    def driver(self):
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=options)
        driver.maximize_window()
        yield driver
        driver.quit()

    @pytest.fixture(scope="function")
    def driver_chrome(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        yield driver
        driver.quit()