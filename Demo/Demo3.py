import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search(self):
        self.driver.get("http://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)





    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
