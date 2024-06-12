from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class Account_Success_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    account_creation_message_xpath="//div[@id='content']/h1"

    def retrieve_account_creation_message(self):
        return self.retreive_element_text("account_creation_message_xpath",self.account_creation_message_xpath)
