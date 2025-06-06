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
sourceOfElementToBeDragable=driver.find_element(By.ID, "draggable")
destinationOfElementToBeDragable=driver.find_element(By.ID, "droppable")


act=ActionChains(driver)
act.drag_and_drop(sourceOfElementToBeDragable,destinationOfElementToBeDragable).perform()


time.sleep(3)

driver.quit()