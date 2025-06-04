from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

numberOfRows=len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
numberOfColumns=len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th"))
print(numberOfRows)
print(numberOfColumns)

data=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]").text
print(data)


# for i in range(2,numberOfRows+1):
#     for j in range(1,numberOfColumns+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(i)+"]/td["+str(j)+"]").text
#         print(data, end='           ')
#     print()

for r in range(2,numberOfRows+1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(2)+"]").text
    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(1)+"]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[" + str(4) + "]").text
        print(bookName, "   ", authorName, "   ", price)


driver.quit()