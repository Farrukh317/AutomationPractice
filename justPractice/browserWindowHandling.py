import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# windowid=driver.current_window_handle
# print(windowid)
time.sleep(3)
driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()
windowids=driver.window_handles


# parentWindowId=windowids[0]
# childWindowId=windowids[1]
# print(parentWindowId, childWindowId)
# driver.switch_to.window(childWindowId)
# print(driver.title)
# driver.switch_to.window(parentWindowId)
# print(driver.title)

for winid in windowids:
    driver.switch_to.window(winid)
    if driver.title=="OrangeHRM":
        driver.close()

driver.quit()
