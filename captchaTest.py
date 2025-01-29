from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/errors/validateCaptcha?amzn=zfo48zUOttdqhICeG0xW1Q%3D%3D&amzn-r=%2F&field-keywords=earphoneWIRELESS+")
assert "Amazon" in driver.title
elem = driver.find_element(By.TAG_NAME, "IMG")
src = elem.get_attribute("src")

print(src)
assert "No results found." not in driver.page_source

time.sleep(5)

driver.close()