import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/my-account/")
driver.maximize_window()
driver.implicitly_wait(2)

#driver.switch_to.frame("login_page")
driver.find_element(By.ID,"username").send_keys("Sn531916644")
print("enter data")
time.sleep(5)

driver.close()