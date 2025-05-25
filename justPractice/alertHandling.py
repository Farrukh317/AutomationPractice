from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']").click()
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']").click()
cancelAlert = driver.switch_to.alert
cancelAlert.dismiss()
time.sleep(2)

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
alertWindow = driver.switch_to.alert
print(alertWindow.text)
alertWindow.send_keys("Alert input message")
# alertWindow.accept()
alertWindow.dismiss()


time.sleep(5)
driver.quit()