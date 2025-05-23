from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.get("https://dev.yuzee.click")
driver.back()
driver.forward()
driver.refresh()

print(driver.title)
print(driver.current_url)
driver.quit()