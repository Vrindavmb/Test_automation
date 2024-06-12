from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from Tests.BaseTest import BaseTest
from pages.Account_Success_Page import Account_Success_Page
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage


class TestRegister(BaseTest):
    def test_register_with_mandatory_fields(self):
        homepage=HomePage(self.driver)
        registerpage=homepage.navigate_to_register_page()
        #knowingly failing this testcase to chck the screensashot functionality
        accountsuccess=registerpage.register_an_account("Vrinda","MB",self.generate_email_with_time_stamp(),"1234567890","12345","12345","no","select")
        expected_heading_text = "Your Account Has Been Created!"
        assert accountsuccess.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_all_fields(self):
        homepage = HomePage(self.driver)
        registerpage=homepage.navigate_to_register_page()
        accountsuccess=registerpage.register_an_account("Vrinda","MB",self.generate_email_with_time_stamp(),"1234567890","12345","12345","yes","select")
        expected_heading_text = "Your Account Has Been Created!"
        assert accountsuccess.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_duplicate_email(self):
        homepage = HomePage(self.driver)
        registerpage = homepage.navigate_to_register_page()
        registerpage.register_an_account("Vrinda", "MB","vrindamb1@gmail.com","1234567890", "123456", "123456","yes", "select")
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert registerpage.retrieve_duplicate_email_warning().__contains__(expected_warning_message)

    def test_without_entering_any_fields(self):
        homepage = HomePage(self.driver)
        registerpage = homepage.navigate_to_register_page()
        registerpage.register_an_account("","","","","","","no","no")
        assert registerpage.verify_all_warnings("Warning: You must agree to the Privacy Policy!",
                                                "First Name must be between 1 and 32 characters!",
                                                "Last Name must be between 1 and 32 characters!",
                                                "E-Mail Address does not appear to be valid!",
                                                "Telephone must be between 3 and 32 characters!",
                                                "Password must be between 4 and 20 characters!")