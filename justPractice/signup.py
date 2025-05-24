import time
import random
from typing import final

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://env1.yuzee.click")
driver.maximize_window()

try:
    sliders = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, "div.owl-item div.row.align-items-center.fade-in"
        ))
    )
    print(f"Total Sliders found: {len(sliders)}")
except Exception as e:
    print(f"Error: {e}")

# sliders = driver.find_element(By.CSS_SELECTOR, "div[class='owl-item ng-tns-c355-0 ng-trigger ng-trigger-autoHeight ng-star-inserted cloned animated owl-animated-out fadeOut'] div[class='row align-items-center fade-in ng-star-inserted']")
# print(len(sliders))

links = driver.find_element(By.TAG_NAME, "a").get_attribute("href")
print(len(links))

driver.find_element(By.CSS_SELECTOR, ".btn.theme-btn.btn-blue.mr-1").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Given Name(s)']").send_keys("newMan")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Surname']").send_keys("oldWomen")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Date of Birth']").click()
driver.find_element(By.CSS_SELECTOR, "select[title='Select year']").send_keys("1950")
driver.find_element(By.CSS_SELECTOR, "select[title='Select month']").send_keys("May")
driver.find_element(By.CSS_SELECTOR, "div[aria-label='Wednesday, May 10, 1950'] div[class='btn-light ng-star-inserted']").click()
# driver.find_element(By.XPATH, "//ng-select[@id='gender']//div[@class='ng-select-container']").click()
# driver.find_element(By.XPATH, "//div[@id='ab78ae282a2a-1']").click()

# Open the gender dropdown
driver.find_element(By.XPATH, "//ng-select[@id='gender']//div[@role='combobox']").click()

# Wait and click the 'Male' option based on visible text
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ng-option') and normalize-space()='Male']"))
).click()

driver.find_element(By.ID, "postal_code").send_keys("3500")

random_number = random.randint(100, 9999)
email = f"heybro{random_number}@yopmail.com"
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email Address']").send_keys(email)

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("Admin123.")
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-blue theme-btn w-50']").click()

time.sleep(7)

driver.close()
