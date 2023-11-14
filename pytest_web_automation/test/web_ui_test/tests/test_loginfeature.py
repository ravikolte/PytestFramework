import logging
import pytest

from helpers.constants_helper import *
from pages.Dashboard import Dashboard
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest

logger = logging.getLogger()


class Test_Login(BaseTest):

    @pytest.mark.login
    def test_valid_login(self):
        LoginPage(self.driver).login(user_name, user_password)
        title = Dashboard(self.driver).dash_title()
        assert "Dashboard" == title, "Not on Dashboard"


    @pytest.mark.login
    def test_invalid_login(self):
        LoginPage(self.driver).login(invalid_user_name, invalid_user_password)
        invalid_credentials_message = LoginPage(self.driver).get_invalid_credential_message()
        assert "Invalid credentials" == invalid_credentials_message, "Invalid credentials are accepted"

    def test_example(self):
        print("in test function")
        logger.info("Test example function executed correctly")

