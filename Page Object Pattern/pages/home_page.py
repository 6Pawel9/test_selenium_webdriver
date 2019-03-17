from locators import HomePageLocators
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def _verify_page(self):
        assert "Oficjalna strona Wizz Air" in self.driver.title

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(HomePageLocators.ZALOGUJ_BTN))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.ZALOGUJ_BTN))

    def click_zaloguj_button(self):
        """Triggers the search"""
        el = self.driver.find_element(*HomePageLocators.ZALOGUJ_BTN)
        el.click()
