# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
import time
import test_data.customer_data as td


class WizzairRegistration(unittest.TestCase):

    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("geo.enabled", False);
        self.driver = webdriver.Firefox(firefox_profile=profile)
        self.driver.get("https://wizzair.com/pl-pl#/")
        self.driver.maximize_window()

    def test_correct_registration(self):


        home_page = HomePage(self.driver)
        #Checks if the word "Python" is in title
        home_page._verify_page()
        home_page.click_zaloguj_button()
        login_page = LoginPage(self.driver)
        login_page.click_rejestracja_button()
        register_page = RegisterPage(self.driver)
        register_page.fill_name_field(td.valid_name)
        register_page.fill_surname_field(td.valid_surname)
        register_page.choose_gender(td.gender)
        register_page.fill_telephone_field(td.valid_telephone)
        register_page.fill_email_field(td.valid_email)
        register_page.fill_password_field(td.valid_password)
        register_page.fill_country_field(td.valid_country)
        register_page.accept_privacy_policy()
        register_page.check_if_register_button_is_enabled()
        register_page.check_if_no_error_notice_is_presented()
        time.sleep(2)
        #register_page.check_displayed_error_notice()

    def test_incorrect_email(self):
        home_page = HomePage(self.driver)
        #Checks if the word "Python" is in title
        home_page._verify_page()
        home_page.click_zaloguj_button()
        login_page = LoginPage(self.driver)
        login_page.click_rejestracja_button()
        register_page = RegisterPage(self.driver)
        register_page.fill_name_field(td.valid_name)
        register_page.fill_surname_field(td.valid_surname)
        register_page.choose_gender(td.gender)
        register_page.fill_telephone_field(td.valid_telephone)
        register_page.fill_email_field("sasda.pl")
        register_page.fill_password_field(td.valid_password)
        register_page.fill_country_field(td.valid_country)
        register_page.accept_privacy_policy()
        errors = register_page.return_displayed_error_notices()
        assert len(errors) == 1
        error_text = errors[0].get_attribute("innerText")
        assert error_text == u"Nieprawidłowy adres e-mail"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
