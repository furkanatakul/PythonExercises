from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://google.com")
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME,"q")))
searchBarByName = driver.find_element(By.NAME,"q")

#searchBarByClassName = driver.find_element(By.CLASS_NAME,"gLFyf")
#print(searchBarByName)
#print(searchBarByClassName)
searchBarByName.send_keys("Furkan Atakul")
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME,"btnK")))
buttonByName = driver.find_element(By.NAME,"btnK")
buttonByName.click()

while True:
    continue