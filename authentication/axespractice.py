from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service(r"C:\Drivers\chromedriver_win64\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers")

text_msg1 = driver.find_element(By.XPATH, "//a[contains(text(), 'Carysil L')]/self::a").text
print(text_msg1)

text_msg2 = driver.find_element(By.XPATH, "//a[contains(text(), 'Carysil L')]/parent::td").text
print(text_msg2)

text_msg3 = driver.find_elements(By.XPATH, "//a[contains(text(), 'Carysil L')]/ancestor::tr/child::td")
print(len(text_msg3))

text_msg4 = driver.find_element(By.XPATH, "//a[contains(text(), 'Carysil L')]/ancestor::tr").text
print(text_msg4)

text_msg5 = driver.find_elements(By.XPATH, "//a[contains(text(), 'Carysil L')]/ancestor::tr/descendant::*")
print(text_msg5)
print(len(text_msg5))

text_msg6 = driver.find_elements(By.XPATH, "//a[contains(text(), 'Carysil L')]/ancestor::tr/following::*")
print(len(text_msg6))

text_msg7 = driver.find_elements(By.XPATH, "//a[contains(text(), 'Carysil L')]/ancestor::tr/following-sibling::*")
print(len(text_msg7))

text_msg8 = driver.find_elements(By.XPATH, "//a[contains(text(), 'Carysil L')]/ancestor::tr/preceding::tr")
print(len(text_msg8))

text_msg9 = driver.find_elements(By.XPATH, "//a[contains(text(), 'Carysil L')]/ancestor::tr/preceding-sibling::tr")
print(len(text_msg9))


driver.close()