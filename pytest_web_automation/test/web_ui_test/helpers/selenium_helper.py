import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.constants_helper import ExplicitWait

logger = logging.getLogger()


class Selenium_helper:

    def __init__(self, driver):
        self.driver = driver

    def enter(self, locator, text):
        logger.debug("Entering value for the webelement")
        WebDriverWait(self.driver, ExplicitWait).until(EC.element_to_be_clickable(locator)).send_keys(text)

    def click(self, locator):
        logger.debug("Click on the element")
        WebDriverWait(self.driver, ExplicitWait).until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator):
        logger.debug("Getting text of the element")
        return WebDriverWait(self.driver, ExplicitWait).until(EC.visibility_of_element_located(locator)).text

    def _get_list(self, locator):
        logger.debug("Getting a list of Webelements")
        try:
            elements = WebDriverWait(self.driver, ExplicitWait).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            elements = []  # Return an empty list if elements are not found

        return elements

    def clear_text(self, locator):
        logger.debug("Clearing the text field")
        WebDriverWait(self.driver, ExplicitWait).until(EC.element_to_be_clickable(locator)).clear()

    """  def find(self, *locator):
          return self.driver.find_element(*locator)

      def enter(self, locator, text):
          self.find(*locator).send_keys(text)

      def get_text(self, locator):
          return self.find(*locator).text

      def click(self, locator):
          self.find(*locator).click()

      def clear(self, locator):
          self.find(*locator).clear()
    """