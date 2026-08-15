from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

# Search box
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Honey")

# Click search
search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()

# Wait for results
wait = WebDriverWait(driver, 10)
results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")))

print(str(len(results)) + " products found")
for item in results[:10]:   # show first 10
    print(item.text)

driver.quit()



# click = driver.find_element(By.ID,"nav-search-submit-button")
# click.click()
# time.sleep(5)

# select = driver.find_element(By.LINK_TEXT,'Fresh')

# select.click()                                                                            
# driver.refresh()
# driver.back()
# time.sleep(4)
# driver.forward()
# time.sleep(4)
# driver.quit()