import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://env1.yuzee.click/")

# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

driver.maximize_window()

print(driver.title)
print(driver.current_url)
print(driver.page_source)

searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print(searchbox.is_displayed())
print(searchbox.is_enabled())

radiocheckM = driver.find_element(By.XPATH, "//input[@id='gender-male']")
print(radiocheckM.is_selected())
radioF = driver.find_element(By.XPATH, "//input[@id='gender-female']")
print(radioF.is_selected())

print("After mark as Male")
radiocheckM.click()
print(radiocheckM.is_selected())
print(radioF.is_selected())

print("After mark as Female")
radioF.click()
print(radiocheckM.is_selected())
print(radioF.is_selected())

driver.find_element(By.LINK_TEXT, "Facebook").click()

time.sleep(15)

driver.quit()
