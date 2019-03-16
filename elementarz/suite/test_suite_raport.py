# -*- coding: utf-8" -*

import unittest
from search_text import SearchText
from home_page_test import HomePageTest
import HTMLTestRunner
import os

# Pobierz z systemu katalog, w którym pracujemy
# (będziemy zapisywali wyniki testów)
dir = os.getcwd()

# Pobierz wszystkie testy z SearchText i HomePageTest
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# Stwórz Test Suita łączac testy
test_suite = unittest.TestSuite([home_page_test, search_text])

# Stwórz plik z wynikami
outfile = open(dir + "/TestResults.html", "w")

# Skonfiguruj HTMLRunner
runner = HTMLTestRunner.HTMLTestRunner(
    verbosity=2, stream=outfile, title='Test report',
    description='Smoke Tests')

# Uruchom suite
runner.run(test_suite)
