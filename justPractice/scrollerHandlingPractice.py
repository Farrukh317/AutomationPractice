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

# scrolldown page by pixels
driver.execute_script("window.scrollBy(0,2000)","")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ", value)
time.sleep(3)

# scrolldown page till the element is visible
homeLink=driver.find_element(By.XPATH, "//a[@class='home-link']")
driver.execute_script("arguments[0].scrollIntoView();", homeLink)
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ", value)
time.sleep(3)

# scrolldown to page end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ", value)
time.sleep(3)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ", value)


time.sleep(3)

driver.quit()