# -*- coding: utf-8 -*
# Zaimportowanie niezbędnych bibliotek
from selenium import webdriver
import time

# Stwórz nowy sterownik do Chrome
driver = webdriver.Chrome()
# Maksymalizuj okno
driver.maximize_window()
# Przejdź do strony www.wsb.pl
driver.get("http://www.wsb.pl")
# Poczekaj 5 sekund, by nacieszyć oczy
# Bardzo zła metoda w prawdziwych testach
# są specjalne funkcje explicit i implicit wait
time.sleep(5)
# Zamknij sterownik
driver.quit()
