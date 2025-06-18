import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location=os.getcwd()


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    # preferences={"download.default_directory":"C:\\Users\\Farru\\Desktop\\PythonProject1"}

    preferences = {"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)


    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=ops)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    ops.set_preference("browser.download.manager/showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2) # 0 for desktop, 1 for download folder, 2 for desired location
    ops.set_preference("browser.download.dir", location)
    driver = webdriver.Firefox(options=ops)
    return driver

# driver = chrome_setup()

driver=firefox_setup()
driver.maximize_window()
driver.get("https://www.examplefile.com/document/pdf/1-mb-pdf")
driver.find_element(By.XPATH,"//a[@title='1 MB PDF Download']").click()

time.sleep(5)

driver.quit()