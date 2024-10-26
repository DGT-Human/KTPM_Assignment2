import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

@pytest.fixture(scope="function")
def driver():
    options = webdriver.EdgeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

class TestRegister:

    def test_register_valid(self, driver):
        driver.get("http://localhost/opencart/upload/")
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(., 'My Account')]").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Register')]").click()
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(3)
        firstname_input = driver.find_element(By.ID, "input-firstname")
        firstname_input.send_keys("Nguyen")
        lastname_input = driver.find_element(By.ID, "input-lastname")
        lastname_input.send_keys("B")
        email_input = driver.find_element(By.ID, "input-email")
        email_input.send_keys("b@b.com")
        password_input = driver.find_element(By.ID, "input-password")
        password_input.send_keys("12345")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='agree']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]").click()
        time.sleep(3)
        message = driver.find_element(By.XPATH, "//h1[text()='Your Account Has Been Created!']").text
        assert "Your Account Has Been Created!" in message

    def test_register_invalid_email(self, driver):
        driver.get("http://localhost/opencart/upload/")
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(., 'My Account')]").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Register')]").click()
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(3)
        firstname_input = driver.find_element(By.ID, "input-firstname")
        firstname_input.send_keys("Nguyen")
        lastname_input = driver.find_element(By.ID, "input-lastname")
        lastname_input.send_keys("B")
        email_input = driver.find_element(By.ID, "input-email")
        email_input.send_keys("")
        password_input = driver.find_element(By.ID, "input-password")
        password_input.send_keys("12345")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='agree']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]").click()
        time.sleep(3)
        message = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[3]/div/div").text
        assert "E-Mail Address does not appear to be valid!" in message


    def test_register_invalid_name(self, driver):
        driver.get("http://localhost/opencart/upload/")
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(., 'My Account')]").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Register')]").click()
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(3)
        firstname_input = driver.find_element(By.ID, "input-firstname")
        firstname_input.send_keys("")
        lastname_input = driver.find_element(By.ID, "input-lastname")
        lastname_input.send_keys("")
        email_input = driver.find_element(By.ID, "input-email")
        email_input.send_keys("c@c.com")
        password_input = driver.find_element(By.ID, "input-password")
        password_input.send_keys("12345")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='agree']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]").click()
        time.sleep(3)
        message1 = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[1]/div/div").text
        message2 = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[2]/div/div").text
        assert "First Name must be between 1 and 32 characters!" in message1
        assert "Last Name must be between 1 and 32 characters!" in message2

    def test_register_invalid_password(self, driver):
        driver.get("http://localhost/opencart/upload/")
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(., 'My Account')]").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Register')]").click()
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(3)
        firstname_input = driver.find_element(By.ID, "input-firstname")
        firstname_input.send_keys("Nguyen")
        lastname_input = driver.find_element(By.ID, "input-lastname")
        lastname_input.send_keys("B")
        email_input = driver.find_element(By.ID, "input-email")
        email_input.send_keys("b@b.com")
        password_input = driver.find_element(By.ID, "input-password")
        password_input.send_keys("")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='agree']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]").click()
        time.sleep(3)
        message = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[2]/div/div/div").text
        assert "Password must be between 4 and 20 characters!" in message

    def test_register_invalid_agree(self, driver):
        driver.get("http://localhost/opencart/upload/")
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(., 'My Account')]").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Register')]").click()
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(3)
        firstname_input = driver.find_element(By.ID, "input-firstname")
        firstname_input.send_keys("Nguyen")
        lastname_input = driver.find_element(By.ID, "input-lastname")
        lastname_input.send_keys("B")
        email_input = driver.find_element(By.ID, "input-email")
        email_input.send_keys("b@b.com")
        password_input = driver.find_element(By.ID, "input-password")
        password_input.send_keys("12345")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]").click()
        time.sleep(3)
        message = driver.find_element(By.XPATH, "/html/body/div").text
        assert "You must agree to the Privacy Policy!" in message

