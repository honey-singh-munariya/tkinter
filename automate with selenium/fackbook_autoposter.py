from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://www.fackbook.com')

button_1 = driver.find_element(By.XPATH,'.//*[@id="_r_2_"]')
button_1.send_keys("61571277110790")
button_2 = driver.find_element(By.XPATH,'//*[@id="login_form"]/div/div[1]/div/div[2]/div/div')
button_2.send_keys("983353")

login = driver.find_element(By.XPATH,'//*[@id="login_form"]/div/div[1]/div/div[2]/div/div')
login.click()
status = driver.find_element(By.XPATH,".//*[@name='xhpc_message']")
time.sleep(5)
status.send_keys("Hii, there")
time.sleep(4)
button=driver.find_element(By.TAG_NAME,'button')
time.sleep(4)
for buttons in button:
    if button.text== 'Post':
        button.click()

driver.quit()