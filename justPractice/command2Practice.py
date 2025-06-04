from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# driver.get("https://dev.yuzee.click")
# driver.back()
# driver.forward()
# driver.refresh()

print(driver.title)
print(driver.current_url)

driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
capturetext = driver.find_element(By.XPATH,"//input[@id='Email']")
capturetext.send_keys("email@email.com")
print(capturetext.text)
print(capturetext.get_attribute("value"))

btnlogin = driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print(btnlogin.text)
print(btnlogin.get_attribute("type"))


driver.quit()