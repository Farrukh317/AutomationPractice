from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.automationtesting.in/Frames.html")

driver.switch_to.frame("SingleFrame")
driver.find_element(By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/input[1]").send_keys("123456789")
driver.switch_to.default_content()

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']"))
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']"))
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("1234567890")

time.sleep(3)

driver.quit()