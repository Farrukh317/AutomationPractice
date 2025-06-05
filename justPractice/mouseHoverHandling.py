from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)

driver.get("https://testautomationpractice.blogspot.com/")
mouse=driver.find_element(By.XPATH, "//div[@id='sidebar-right-1']//div[6]//button")
laptop=driver.find_element(By.XPATH, "//div[@id='sidebar-right-1']//div[6]//button/following-sibling::*/a[2]")


act=ActionChains(driver)
act.move_to_element(mouse).move_to_element(laptop).click().perform()



time.sleep(3)

driver.quit()