import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Driver():
    @pytest.fixture(scope="function")
    def driver(self):
        options = webdriver.EdgeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
        driver = webdriver.Edge(options=options)
        driver.maximize_window()
        yield driver
        driver.quit()