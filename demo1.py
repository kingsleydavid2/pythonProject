from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://google.com")

frombtn = driver.find_element_by_name("btnK").click()

driver.close()

driver.quit()

print("Done")

li = [10, 20, 30]
n = len(li)
print("The length of list is: ", n)



