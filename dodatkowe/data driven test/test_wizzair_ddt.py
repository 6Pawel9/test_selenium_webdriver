# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
from ddt import ddt, data, unpack
import csv

"""
Rejestracja nowego użytkownika na stronie wizzair.com

Przypadki testowe:
I Rejestracja nowego użytkownika używając adresu email
dane niepoprawne (niekompletny email)
Kroki:
"1. Wejdz na https://wizzair.com/pl-pl/main-page#/
2. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
3. Wybierz rejestracja
4. Wprowadź imię
5. Wprowadź nazwisko
6. Wybierz płeć
7. Wprowadź nr tel
8. Wprowadź błędny adres email - brak znaku @
9. Wprowadź hasło
10. Wybierz kraj
11. Akceptuj politykę prywatności
12. Kliknij przycisk ZAREJESTRUJ SIĘ"

Oczekiwany rezultat:
Przycisk "zarejestruj się" jest nieaktywny
Uzytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny

"""


def get_data(file_name):
    # Stwórz pustą listę
    rows = []
    # Otwórz plik CSV
    data_file = open(file_name, "rb")
    # Stwórz CSV Reader z pliku CSV
    reader = csv.reader(data_file)
    # Pomiń nagłówek
    next(reader, None)
    # Dodaj wiersze do listy
    for row in reader:
        rows.append(row)
    return rows


@ddt
class WizzairRegistrationDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    @data(*get_data("valid_credentials.csv"))
    @unpack
    def test_registration_valid(
            self, valid_name, valid_surname, valid_telephone,
            valid_email, valid_password, valid_country, valid_gender):
        driver = self.driver
        driver.get("https://wizzair.com/pl-pl/main-page#/")
        zaloguj_btn = driver.find_element_by_css_selector(
            "#app > header > div > nav > ul > li:nth-child(3) > button")
        zaloguj_btn.click()
        rejestracja_btn = driver.find_element_by_xpath(
            '//*[@id="login-modal"]/form/div/p/button')
        rejestracja_btn.click()
        imie_field = driver.find_element_by_xpath(
            "//input[@placeholder='Imię']")
        imie_field.send_keys(valid_name)
        nazwisko_field = driver.find_element_by_xpath(
            "//input[@placeholder='Nazwisko']")
        nazwisko_field.send_keys(valid_surname)

        if(valid_gender == "M"):
            gender_switch = driver.find_element_by_id("register-gender-male")
        elif(valid_gender == "K"):
            gender_switch = driver.find_element_by_id("register-gender-female")
        driver.execute_script("arguments[0].click()", gender_switch)
        telefon_field = driver.find_element_by_css_selector("input[type=tel]")
        telefon_field.send_keys(valid_telephone)
        email_field = driver.find_element_by_css_selector(
            "input[data-test=booking-register-email]")
        email_field.send_keys(valid_email)
        password_field = driver.find_element_by_css_selector(
            "input[data-test=booking-register-password]")
        password_field.send_keys(valid_password)
        country_field = driver.find_element_by_css_selector(
            "input[data-test=booking-register-country]")
        country_field.send_keys(valid_country)
        privacy_policy = driver.find_element_by_xpath(
            '//*[@data-test="booking-register-privacy-policy"]')
        privacy_policy.click()
        zarejestruj_btn = driver.find_element_by_css_selector(
            ".button[type=submit][data-test=booking-register-submit]")
        self.assertTrue(zarejestruj_btn.is_enabled(), "Szlag rafił!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
