# import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# options = uc.ChromeOptions()
# driver = uc.Chrome(options=options)
# driver.get("https://www.opencart.com/index.php?route=common/home")

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://dev.yuzee.click/")
# driver.find_element(By.XPATH, "(//a[contains(text(),'Join Yuzee')])[1]").click()
# genderselection=driver.find_element(By.XPATH, "//div[contains(text(),'Select gender')]")
# genderselection.click()

driver.get("https://testautomationpractice.blogspot.com/")

# driver.find_element(By.XPATH, "//div[@class='bg-white']//a[@class='dropdown-toggle'][normalize-space()='Categories']").click()
# driver.find_element(By.XPATH, "//div[@class='category-dropdown p-4 dropdown-menu show']//a[@class='cat-menu-txt'][normalize-space()='Healthcare & Medical']").click()

dropdownCat= Select(driver.find_element(By.ID, "country"))
dropdownCat.select_by_visible_text("Australia")
dropdownCat.select_by_index(4)

totalAvailableCountries = dropdownCat.options
print(len(totalAvailableCountries))

for opt in totalAvailableCountries:
    print(opt.text)

# select without pre-builin functions
for opt in totalAvailableCountries:
    if opt.text == "China":
        opt.click()
        break


sleep(3)

# dropDown=Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))
# dropDown.select_by_text("Oman")

# sleep(5)

driver.quit()