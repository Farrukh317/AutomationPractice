from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service(r"C:\Drivers\chromedriver_win64\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.get("https://dev.yuzee.click")

# driver.find_element(By.XPATH, "//div[@class='bg-white']//div[@class='row d-none d-md-flex']//a[contains(text(),'Sign in')]").clear()
driver.find_element(By.XPATH, "//div[@class='bg-white']//div[@class='row d-none d-md-flex']//a[contains(text(),'Sign in')]").click()
driver.find_element(By.XPATH, "//input[@placeholder='Email']").clear()
driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("Sign@yopmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin123@")

# text_msg = driver.find_element(By.XPATH, "//a[@type='password']/parent::*").text
# print(text_msg)

driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()

act_title=driver.title
exp_title="Yuzee: Login"

if act_title == exp_title:
    print("Login Successful")
else:
    print("Login Failed")

driver.close()
