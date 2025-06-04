from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
# month=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
# year=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

requiredMonth="July"
requiredYear="2027"

while True:
    month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if month == requiredMonth and year == requiredYear:
        break
    else:
        navForward=driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']")
        navForward.click()
#############################
#################

time.sleep(3)
driver.quit()