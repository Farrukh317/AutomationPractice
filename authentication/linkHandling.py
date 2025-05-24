from datetime import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Boo").click()

numberOfLinks=driver.find_elements(By.TAG_NAME, "a")
print(len(numberOfLinks))

for link in numberOfLinks:
    print(link.text)



sleep(5)

driver.quit()