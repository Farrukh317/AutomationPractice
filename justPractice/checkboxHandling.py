from datetime import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# checkbox= driver.find_element(By.XPATH, "//label[normalize-space()='Sunday']")
# checkbox.click()

# sleep(10)

allcheckboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print(len(allcheckboxes))

# for i in range(len(allcheckboxes)):
#         allcheckboxes[i].click()

# multiple checkbox by choice
# for checkbox in allcheckboxes:
#     weekname=checkbox.get_attribute("id")
#     if weekname=="monday" or weekname=="sunday" or weekname=="wednesday":
#         checkbox.click()

# last 4 selection logic
# for i in range(len(allcheckboxes)-4, len(allcheckboxes)):
#     allcheckboxes[i].click()

# select first 2 checkboxes
for i in range(len(allcheckboxes)):
    if i<2:
        allcheckboxes[i].click()

# clear all checkboxes
for allcheckboxes in allcheckboxes:
    if allcheckboxes.is_selected():
        allcheckboxes.click()
        sleep(2)


driver.quit()