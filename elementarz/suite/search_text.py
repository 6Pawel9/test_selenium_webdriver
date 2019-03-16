import unittest
from selenium import webdriver


class SearchText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://www.google.com/")

    def test_search_by_text(self):
        driver = self.driver
        search_field = driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys("Selenium")
        search_field.submit()
        lists = driver.find_elements_by_class_name("r")
        self.assertEqual(10, len(lists))

    def test_search_by_name(self):
        driver = self.driver
        search_field = driver.find_element_by_name("q")
        search_field.send_keys("Python")
        search_field.submit()
        list_new = driver.find_elements_by_class_name("r")
        self.assertEqual(9, len(list_new))

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

