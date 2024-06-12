import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

from Tests.BaseTest import BaseTest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class TestLogin(BaseTest):
    def test_login_with_valid_credentials(self):
        homepage = HomePage(self.driver)
        login_page=homepage.navigate_to_login_page()
        account_page=login_page.login_to_application("vrindamb1@gmail.com","123456")
        assert account_page.display_status_of_edit_you_account_information_option()

    def test_login_with_invalid_email_and_valid_password(self):
        homepage = HomePage(self.driver)
        login_page=homepage.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(),"123456")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__eq__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        homepage = HomePage(self.driver)
        login_page=homepage.navigate_to_login_page()
        login_page.login_to_application("vrindamb1@gmail.com","1234567")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__eq__(expected_warning_message)

    def test_login_without_entering_credentials(self):
        homepage = HomePage(self.driver)
        login_page = homepage.navigate_to_login_page()
        login_page.login_to_application("","")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__eq__(expected_warning_message)


