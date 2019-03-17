from locators import RegisterPageLocators
from base_page import BasePage
import time


class RegisterPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def _verify_page(self):
        time.sleep(2)

    def fill_name_field(self, name):
        field = self.driver.find_element(*RegisterPageLocators.NAME_FIELD)
        field.send_keys(name)

    def fill_surname_field(self, surname):
        field = self.driver.find_element(*RegisterPageLocators.SURNAME_FIELD)
        field.send_keys(surname)

    def fill_email_field(self, email):
        field = self.driver.find_element(*RegisterPageLocators.EMAIL_FIELD)
        field.send_keys(email)

    def fill_country_field(self, country):
        field = self.driver.find_element(*RegisterPageLocators.COUNTRY_FIELD)
        field.send_keys(country)

    def fill_telephone_field(self, telephone):
        field = self.driver.find_element(*RegisterPageLocators.TELEPHONE_FIELD)
        field.send_keys(telephone)

    def fill_password_field(self, password):
        field = self.driver.find_element(*RegisterPageLocators.PASSWORD_FIELD)
        field.send_keys(password)

    def accept_privacy_policy(self):
        checkbox = self.driver.find_element(*RegisterPageLocators.PRIVACY_POLICY_CHECKBOX)
        checkbox.click()

    def check_if_register_button_is_enabled(self):
        btn = self.driver.find_element(*RegisterPageLocators.REGISTER_BTN)
        assert btn.is_enabled(), "Register button cannot be clicked"

    def check_if_no_error_notice_is_presented(self):
        error_notices = self.driver.find_elements(*RegisterPageLocators.ERROR_NOTICES)
        for error in error_notices:
            assert not error.is_displayed(), "Notice displayed: "+ error.get_attribute("innerText")

    def return_displayed_error_notices(self):
        visible_error_notices=[]
        error_notices = self.driver.find_elements(*RegisterPageLocators.ERROR_NOTICES)
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        return visible_error_notices


    def choose_gender(self, gender):
        if gender == 'male':
            gender_switch = self.driver.find_element(*RegisterPageLocators.GENDER_MALE)
            self.driver.execute_script("arguments[0].click()", gender_switch)
        else:
            gender_switch = self.driver.find_element(*RegisterPageLocators.GENDER_FEMALE)
            self.driver.execute_script("arguments[0].click()", gender_switch)
