# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
import time

class AlertTest(unittest.TestCase):

    # Instrukcje, które zostaną automatycznie wykonane przed każdym testem
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("file:///home/gralu/Dokumenty/nowe%20selenium/alert.html")

    # Metody rozpoczynające się od słowa "test" - czyli moje testy
    def test_simple_alert(self):
        driver = self.driver
        driver.find_element_by_id("zwykly").click()
	#driver.switch_to_alert() <-DEPRECATED
        moj_alert = driver.switch_to.alert
        time.sleep(2)
        moj_alert.accept()
        print("zaakceptowano alert")

    def test_prompt(self):
        driver = self.driver
        driver.find_element_by_id("prompt").click()
	#driver.switch_to_alert() <-DEPRECATED
        prompt_alert = driver.switch_to.alert
        prompt_alert.send_keys("Radoslaw Patlewicz")
        prompt_alert.accept()
        print(driver.find_element_by_id("name").text)
        time.sleep(2)

    def test_confirm(self):
        driver = self.driver
        driver.find_element_by_id("conf").click()
	#driver.switch_to_alert() <-DEPRECATED
        conf_alert = driver.switch_to.alert
        conf_alert.accept()
        print(driver.find_element_by_id("tinder").text)
        time.sleep(2)

    # Instrukcje, które zostaną automatycznie wykonane po każdym teście
    def tearDown(self):
        self.driver.quit()

# Początek mojego programu
# wywołuję funkcję main() z modułu unittest,
# która w automatyczny sposób będzie już wiedziała
# co dalej robić z utworzoną wyżej klasą
if __name__ == "__main__":
    unittest.main(verbosity=2)
