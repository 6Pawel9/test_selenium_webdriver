# -*- coding: utf-8" -*

import unittest
from selenium import webdriver


#Klasa WsbPlCheck dziedzicząca po klasie TestCase z modułu unittest
class WsbPlCheck(unittest.TestCase):

    # Instrukcje, które zostaną automatycznie wykonane przed każdym testem
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Metody rozpoczynające się od słowa "test" - czyli moje testy
    def test_wsb_pl(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        # Sprawdzam, czy "Wyższe Szkoły Bankowe" znajdują się w tytule strony
        self.assertIn("Wyższe Szkoły Bankowe".decode("utf-8"), driver.title)

    def test_wsb_pl_wroclaw(self):
        driver = self.driver
        driver.get("https://www.wsb.pl/wroclaw/")
        # Sprawdzam, czy "Wyższe Szkoły Bankowe" znajdują się w tytule strony
        self.assertIn(u"Wrocław", driver.title)

    def test_wsb_pl_chorzow(self):
        driver = self.driver
        driver.get("https://www.wsb.pl/chorzow/")
        # Sprawdzam, czy "Wyższe Szkoły Bankowe" znajdują się w tytule strony
        self.assertIn("Chorzowie", driver.title)

    def test_wsb_pl_bydgoszcz(self):
        driver = self.driver
        driver.get("https://www.wsb.pl/bydgoszcz/")
        # Sprawdzam, czy "Wyższe Szkoły Bankowe" znajdują się w tytule strony
        self.assertIn("Bydgoszcz", driver.title)

    # Instrukcje, które zostaną automatycznie wykonane po każdym teście
    def tearDown(self):
        self.driver.quit()

# Początek mojego programu
# wywołuję funkcję main() z modułu unittest,
# która w automatyczny sposób będzie już wiedziała
# co dalej robić z utworzoną wyżej klasą
# Bez poniższego warunku można ouruchomić test
# Przy pomocy komendy: python -m unittest hello_unittest.py
if __name__ == "__main__":
    unittest.main()
