# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

"""
Na obiektach będących instancjami klasy WebElement możemy podejmować
przeróżne akcje.

Przykłady:
clear() - czyści tekst
send_keys() - wpisuje zadany tekst
click() - klika w element
submit() - wysyła formularz
"""


class WsbPlSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(20)

    def test_click_on_link(self):
        self.driver.get("http://www.wsb.pl/wroclaw")
        podyplomowe_link = self.driver.find_element_by_link_text(
            "Studia podyplomowe")
        podyplomowe_link.click()
        sleep(2)

    def test_search_tester_in_wsb_pl(self):
        self.driver.get("http://www.wsb.pl")
        magnifier = self.driver.find_element_by_link_text("Szukaj")
        magnifier.click()
        search_field = self.driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys("tester")
        search_field.submit()

        results = self.driver.find_elements_by_xpath('//div[@class="direction-title-wrap with-label"]')
        # Czekamy na wyniki (nieładny sposób, lepiej tutaj explixcit wait)
        sleep(2)
        print("Znalazłem " + str(len(results)) + " wyniki:\n")
        for result in results:
            # Nic nie stoi na przeszkodzie, by odnaleźć element h3
            # zawarty w elemencie [@id='block-system-main']/div/ol/li
            result_title = result.find_element_by_xpath("./div/span")
            print(result_title.text)
        # Sprawdzam, czy liczba znalezionych elementów jest równa 3
        self.assertEqual(3, len(results))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=0)
