# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

"""
Selenium zawiera szereg metod wyszukiwania elementów zawartych na stronie.
Wszystkie zaczynają się od "find_element_by..." i zwracają obiekt klasy
WebElement. W przypadku, gdy chcemy wyszukać wiele elementów, korzystamy
z metod "find_elements_by_..." - otrzymujemy wówczas listę złożoną
z obiektów klasy WebElement
"""


class WsbPlSelectors(unittest.TestCase):
    """
    Lokalizatory na stronie wsp.pl/wroclaw
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_find_element(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        # Wyszukuję ciało strony (to co widać) - cała strona
        driver.find_element_by_tag_name("body")
        # Wyszukuję: Pole wybiry miasta
        driver.find_element_by_id("edit-city")
        # Wyszukuję: Lupa
        driver.find_elements_by_class_name("search-icon")
        # Wyszukuję: Link do studiów podyplomowych
        driver.find_element_by_link_text("Studia podyplomowe")
        driver.find_element_by_partial_link_text("podyplom")

    def test_find_element_by_css_selector(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        # Wyszukuję: Pole wyszukiwania
        driver.find_element_by_css_selector("li[class=search-icon]")

    def test_find_element_by_xpath(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        # Wyszukuję: Lupa
        driver.find_element_by_xpath('//li[@class="search-icon"]')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
