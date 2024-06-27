import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TestSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_search(self) -> None:
        driver = self.driver
        driver.get("https://pypi.org/")

        search_bar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "search"))
        )

        search_bar.send_keys("selenium")
        search_bar.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".package-snippet"))
        )

        assert "There was no results for" not in driver.page_source

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
