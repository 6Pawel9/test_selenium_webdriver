# -*- coding: utf-8" -*
import unittest
from selenium import webdriver

"""
Get „http://wp.pl” startpage
Check if there is a specific word
Check if more that one
"""

search_word = "Trump"


class WpPlSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_word(self):
        self.driver.get("http://www.wp.pl")
        # Szukam elementów w kontenerze //div na stronie, które
        # zawierają poszukiwane słowo search_word
        # Przypisuję znalezione elementy do listy results
        results = self.driver.find_elements_by_xpath(
            '//div[contains(text(), "' + search_word + '")]')
        # Sprawdzam, czy odnalazłem choć jedno poszukiwane słowo
        self.assertGreaterEqual(len(results), 1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
