import logging

from selenium.webdriver.common.by import By
from helpers.selenium_helper import Selenium_helper

logger = logging.getLogger()


class Dashboard(Selenium_helper):
    ele_dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")

    def __init__(self, driver):
        super().__init__(driver)

    def dash_title(self):
        return self.get_text(self.ele_dashboard_header)