# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    ZALOGUJ_BTN = (By.XPATH, "//button[@data-test='navigation-menu-signin']")

class LoginPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    REJESTRACJA_BTN = (By.XPATH, "//button[text()='Rejestracja']")

class RegisterPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    NAME_FIELD = (By.XPATH, '//input[@placeholder="Imię"]')
    SURNAME_FIELD = (By.XPATH, '//input[@placeholder="Nazwisko"]')
    GENDER_MALE = (By.XPATH, "//label[@for='register-gender-male']")
    GENDER_FEMALE = (By.XPATH, "//label[@for='register-gender-female']")
    TELEPHONE_FIELD = (By.NAME, "mobilePhone")
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[placeholder="E-mail"][data-test="booking-register-email"]')
    COUNTRY_FIELD = (By.XPATH, "//input[@data-test='booking-register-country']")
    PASSWORD_FIELD = (By.XPATH, "//input[@data-test='booking-register-password']")
    PRIVACY_POLICY_CHECKBOX = (By.XPATH, "//label[@for='registration-privacy-policy-checkbox']")
    REGISTER_BTN = (By.XPATH, "//button[@data-test='booking-register-submit']")

    ERROR_NOTICES = (By.XPATH, "//*[@class='rf-input__error__message']/span")
