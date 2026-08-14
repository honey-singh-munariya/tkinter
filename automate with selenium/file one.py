from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.google.com")

driver.maximize_window()

input = driver.find_element("name","q")
input.send_keys("selenium")
time.sleep(5)

butoon = driver.find_element("name","btnK")
butoon.click()

driver.back()
time.sleep(5)
driver.forward()
time.sleep(4)

driver.quit()