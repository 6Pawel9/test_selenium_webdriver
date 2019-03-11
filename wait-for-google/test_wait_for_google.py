# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class GoogleCheck(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        """
        Tu mogę zastosować implicit wait
        
        Jeśli webdriver nie odnajdzie od razu elementu,
        to będzie próbował to zrobić do skutku przez
        okres 10 sekund. Od momentu wywołania, metoda będzie
        dotyczyła każdego elementu podczas działania jednej
        sesji webdrivera (do momentu driver.quit()).
        """
        # self.driver.implicitly_wait(10)

    def test_google(self):
        driver = self.driver
        driver.get("https://google.pl")
        enter = driver.find_element_by_id("lst-ib")
        enter.send_keys("tester")
        enter.submit()
        """
        Explicit wait - mechanizm, który pozwala
        czekać na zajście określonego warunku przez określony czas. 
        Dotyczy tylko miejsca w kodzie, w którym jest zastosowany.
        WebDriverWait domyślnie wywołuje ExpectedCondition (sprawdza warunek)
        co 500 milisekund, aż w końcu on wystąpi.
        
        W naszym przykładzie będzie to czekanie na to,
        aż google zwróci nam wyniki poszukiwań dla zapytania "tester"
           
        WebDriverWait <- klasa, która zawiera w sobie metody czekania
        dla webdrivera (zadajemy: sterownik, czas czekania w sekundach)
        
        until "dopóki" <- metoda przyjmuje warunek jaki ma wystąpić,
        zanim pójdziemy dalej
        
        presence_of_all_elements_located <- warunek jaki ma wystąpić
        (Czekam na pojawienie się elementów - metoda zawarta w expected_conditions
        której nazwę skróciłem podczas importu do "EC")
        
        By.CLASS_NAME,"g" <- szukam po nazwie klasy "g"
        
        Po wykonaniu się warunku, metoda zwraca elementy,
        które zapisuję do listy results. Jeśli upłynie 10 sekund zanim
        uda się znaleźć co najmniej jeden element, skrypt wyrzuci wyjątek
        TimeoutException
        
        """
        results = WebDriverWait(self.driver, 10)\
            .until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME,"g")

        ))

        # Wyświetlam atrybut text każdego znalezionego elementu
        print (str(len(results)))
        for result in results:
            print (result.text + "\n")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
