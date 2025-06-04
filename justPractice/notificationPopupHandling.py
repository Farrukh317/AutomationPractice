import time
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By

ops=webdriver.ChromeOptions()
ops.add_argument('--disable-notifications')

driver = webdriver.Chrome(options=ops)
driver.maximize_window()

driver.get("https://whatmylocation.com/")
time.sleep(3)



driver.quit()