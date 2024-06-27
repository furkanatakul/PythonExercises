import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    def test_Unirorn(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")
        username_bar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        username_bar.send_keys("selenium")
        password_bar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_bar.send_keys("selenium")
        loginButton = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "login"))
        )
        loginButton.click()
        alertMessage = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "woocommerce-error"))
        )
        assert "Incorrect username or password" in alertMessage
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
