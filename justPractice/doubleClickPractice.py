from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)

driver.get("https://testautomationpractice.blogspot.com/")
field1=driver.find_element(By.XPATH, "(//input[@id='field1'])[1]")
field1.clear()
field1.send_keys("newData")
copyButton=driver.find_element(By.XPATH, "//button[@ondblclick='myFunction1()']")

act=ActionChains(driver)
act.double_click(copyButton).click().perform()


time.sleep(3)

driver.quit()