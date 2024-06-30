from selenium import webdriver
from githubUser import username, password
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class Github:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
        self.signIn()
    def signIn(self):
        self.browser.get("https://github.com/login")
        self.browser.maximize_window()
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "login")))
        self.browser.find_element(By.NAME,"login").send_keys(self.username)
        self.browser.find_element(By.NAME,"password").send_keys(self.password)
        self.browser.find_element(By.NAME, "commit").click()
        time.sleep(15)
        self.getFollowers()

    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".d-table.table-fixed")))

        items = self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed")
        print(items)
        for i in items:
            self.followers.append(i.find_element(By.CLASS_NAME,"Link--secondary").text)
        print(self.followers)

github = Github()

