from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button=driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

action=ActionChains(driver)
action.context_click(button).perform()

time.sleep(3)
driver.quit()
