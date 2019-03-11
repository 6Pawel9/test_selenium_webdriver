import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.google.com/")

    def test_search_box(self):
        driver = self.driver
        driver.find_element_by_name("q")

    def test_login_button(self):
        driver = self.driver
        driver.find_element_by_id("gb_70")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
