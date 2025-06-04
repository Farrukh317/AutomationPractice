from itertools import count

import requests
from requests import request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("http://www.deadlinkcity.com/")

allLinks = driver.find_elements(By.TAG_NAME, "a")
count = 0

for link in allLinks:
    url = link.get_attribute("href")
    try:
        response = requests.head(url)
    except:
        None
    if response.status_code >= 400:
        print(response, "   ", url, " is broken")
        count += 1
    else:
        print(response, "   ", url, " is valid link")

print("Total number of broken link : ", count)

driver.quit()