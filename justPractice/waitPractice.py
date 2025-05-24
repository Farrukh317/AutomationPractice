from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("https://search.yahoo.com/")
# driver.implicitly_wait(10)
# driver.maximize_window()
# searchbox = driver.find_element(By.NAME, "q")
# searchbox.send_keys("selenium")
# searchbox.submit()


mywait = WebDriverWait(driver, 10, poll_frequency= 2, ignored_exceptions=[NoSuchElementException,
                                                       ElementNotVisibleException,
                                                       ElementNotSelectableException,
                                                       Exception]
                       )

driver.maximize_window()
searchbox = driver.find_element(By.NAME, "p")
searchbox.send_keys("selenium")
searchbox.submit()


searchlink=mywait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='d-b fz-20 lh-24 tc ls-024 fw-500'][normalize-space()='Selenium']")))
searchlink.click()

driver.quit()
