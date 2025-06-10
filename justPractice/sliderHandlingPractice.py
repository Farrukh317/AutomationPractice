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

minSlider=driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default'][1]")
maxSlider=driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default'][2]")

print(minSlider.location)   # {'x': 890, 'y': 2020}
print(maxSlider.location)   # {'x': 1020, 'y': 2020}

act=ActionChains(driver)
act.drag_and_drop_by_offset(minSlider, 50, 0).perform()
act.drag_and_drop_by_offset(maxSlider, -20, 0).perform()

print(minSlider.location)   # {'x': 940, 'y': 2020}
print(maxSlider.location)   # {'x': 998, 'y': 2020}


time.sleep(3)

driver.quit()