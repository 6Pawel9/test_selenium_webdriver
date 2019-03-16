# -*- coding: utf-8" -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
Open page  wp.pl
Go to „poczta”
Login to user „testerwsb_t1”
Password „adam1234”
Check if there is a word „Odebrane”
Do the same with wrong password
Do the same with the wrong user
Do the same with wrong password and user
"""

valid_username = "testerwsb_t1"
valid_password = "adam1234"
wrong_username = "tetserwsb_t1"
wrong_password = "adam4321"


class WpPlPoczta(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.wp.pl")
        acc=self.driver.find_element_by_xpath("//button[contains(text(),'PRZECHODZĘ')]")
        self.driver.execute_script("arguments[0].click()", acc)

    def test_mail_odebrane(self):
        poczta_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'POCZTA')))
        self.driver.execute_script("arguments[0].click()", poczta_btn)
        login_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login")))
        # login_field = self.driver.find_element_by_id("login")
        login_field.clear()
        login_field.send_keys(valid_username)
        password_field = self.driver.find_element_by_id("password")
        password_field.clear()
        password_field.send_keys(valid_password)
        self.driver.find_element_by_id("btnSubmit").click()
        handles = self.driver.window_handles
        # Jeśli wyskoczyła upierdliwa rekalama, to ją zamknij
        if len(handles) > 1:
            time.sleep(2)
            self.driver.switch_to_window(handles[0])
            self.driver.find_element_by_id("btnSubmit").click()
            self.driver.switch_to_window(handles[1])
            self.driver.close()
            self.driver.switch_to_window(handles[0])

        odebrane = WebDriverWait(self.driver, 8).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@title="Odebrane"]')))

    def test_wrong_password(self):
        poczta_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'POCZTA')))
        self.driver.execute_script("arguments[0].click()", poczta_btn)
        login_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login")))
        # login_field = self.driver.find_element_by_id("login")
        login_field.clear()
        login_field.send_keys(valid_username)
        password_field = self.driver.find_element_by_id("password")
        password_field.clear()
        password_field.send_keys(wrong_password)
        self.driver.find_element_by_id("btnSubmit").click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='szary error']")))

    def test_wrong_user(self):
        poczta_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'POCZTA')))
        self.driver.execute_script("arguments[0].click()", poczta_btn)
        login_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login")))
        # login_field = self.driver.find_element_by_id("login")
        login_field.clear()
        login_field.send_keys(wrong_username)
        password_field = self.driver.find_element_by_id("password")
        password_field.clear()
        password_field.send_keys(valid_password)
        self.driver.find_element_by_id("btnSubmit").click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='szary error']")))

    def test_wrong_user_and_password(self):
        poczta_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'POCZTA')))
        self.driver.execute_script("arguments[0].click()", poczta_btn)
        login_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login")))
        # login_field = self.driver.find_element_by_id("login")
        login_field.clear()
        login_field.send_keys(wrong_username)
        password_field = self.driver.find_element_by_id("password")
        password_field.clear()
        password_field.send_keys(wrong_password)
        self.driver.find_element_by_id("btnSubmit").click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='szary error']")))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
