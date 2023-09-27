from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.set_page_load_timeout(20)

driver.get("https://www.google.com")

driver.find_element_by_name("q").send_keys("Automation step by step")

driver.find_element_by_name("btnK").click()

print("Script executed successfully")

driver.close()

driver.quit()



