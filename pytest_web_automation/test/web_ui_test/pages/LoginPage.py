import logging

from selenium.webdriver.common.by import By
from helpers.selenium_helper import Selenium_helper

logger = logging.getLogger()


class LoginPage(Selenium_helper):
    ele_login_btn = (By.CSS_SELECTOR, "button[type='submit']")
    ele_email_textfield = (By.CSS_SELECTOR, "input[placeholder='Username']")
    ele_password_textfield = (By.CSS_SELECTOR, "input[placeholder='Password']")
    ele_invalid_credential_message = (By.XPATH, "//p[text()='Invalid credentials']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.clear_text(self.ele_email_textfield)
        self.enter(self.ele_email_textfield, username)
        self.clear_text(self.ele_password_textfield)
        self.enter(self.ele_password_textfield, password)
        self.click(self.ele_login_btn)

    def get_invalid_credential_message(self):
        return self.get_text(self.ele_invalid_credential_message)


