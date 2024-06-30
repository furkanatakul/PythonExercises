from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

WebDriverWait(driver, 10).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete"
)
driver.get(url)

prev_height = -1
max_scrolls = 100
scroll_count = 0

while scroll_count < max_scrolls:
    driver.execute_script("window.scrollTo(0, document.getElementsByClassName('catalogView')[0].scrollHeight);")
    time.sleep(1)
    new_height = driver.execute_script("return document.getElementsByClassName('catalogView')[0].scrollHeight")
    scroll_count += 1
    if new_height == prev_height:
        break
    prev_height = new_height

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"productName")))
elements = driver.find_elements(By.CLASS_NAME,"productName")
elements1 = driver.find_elements(By.CLASS_NAME,"newPrice")

j = 1
for i, t in zip(elements,elements1):
    print(f"{j}. Product: {i.text} Price: {t.text}")
    j +=1