import unittest

from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.chrome(executable_path = "../drivers/chromedriver.exe")
        self.driver.implicitly.wait(10)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()

