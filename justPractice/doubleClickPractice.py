from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)

driver.get("https://testautomationpractice.blogspot.com/")
copyButton=driver.find_element(By.XPATH, "//button[@ondblclick='myFunction1()']")

act=ActionChains(driver)
act.double_click(copyButton).click().perform()


time.sleep(3)

driver.quit()