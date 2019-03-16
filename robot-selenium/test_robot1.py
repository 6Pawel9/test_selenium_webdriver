# -*- coding: utf-8" -*
import unittest
from selenium import webdriver

"""
Get „http://wp.pl” startpage
Check if there is a specific word
Check if more that one
"""

search_word = u"Paryż"


class WpPlSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.wp.pl")
        acc=self.driver.find_element_by_xpath("//button[contains(text(),'PRZECHODZĘ')]")
        self.driver.execute_script("arguments[0].click()", acc)

    def test_search_word(self):

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
