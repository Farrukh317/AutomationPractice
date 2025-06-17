from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)

driver.get("https://text-compare.com/")

input1=driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

input1.send_keys("This is first input")

act=ActionChains(driver)

act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

act.send_keys(Keys.TAB)
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(3)

driver.quit()