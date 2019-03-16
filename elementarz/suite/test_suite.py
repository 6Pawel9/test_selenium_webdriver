# -*- coding: utf-8" -*

import unittest
from search_text import SearchText
from home_page_test import HomePageTest

# Pobierz wszystkie testy z SearchText i HomePageTest
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# Stwórz Test Suita łączac testy
test_suite = unittest.TestSuite([home_page_test, search_text])

# odpal
unittest.TextTestRunner(verbosity=2).run(test_suite)
