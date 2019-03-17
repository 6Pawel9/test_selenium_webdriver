from locators import LoginPageLocators
from base_page import BasePage

class LoginPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def click_rejestracja_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*LoginPageLocators.REJESTRACJA_BTN)
        element.click()
