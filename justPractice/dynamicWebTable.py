from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
usernameField = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
usernameField.send_keys("Admin")
passwordField= wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
passwordField.send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

adminSearch=wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Admin']")))
adminSearch.click()

time.sleep(3)
rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='oxd-table-body']/div")))
totalRows = len(rows)
print("Total Rows:", totalRows)

counter=0
for r in range(1, totalRows+1):
    numberOfStatus = driver.find_element(By.XPATH, "//div["+str(r)+"]/div[1]/div[5]").text
    # print(numberOfStatus)
    if numberOfStatus =="Enabled":
        counter+=1
print("Enable User: ", counter)
print("Disable Users", totalRows-counter)

essUser=0
for i in range(1, totalRows+1):
    numberOfUsers=driver.find_element(By.XPATH, "//div[@role='rowgroup']/div["+str(i)+"]/div[1]/div[2]").text
    print("User: ", numberOfUsers)
    userRole=driver.find_element(By.XPATH, "//div[contains(text(),'ESS')]")
    print("Role: ", userRole.text)
    if userRole.text == "ESS":
         essUser+=1

print("ESS User Role: ", essUser)

time.sleep(3)

driver.quit()