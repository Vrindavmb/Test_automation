import pytest

from Tests.BaseTest import BaseTest
from pages.HomePage import HomePage


class TestSearch(BaseTest):
    def test_search_for_a_valid_product(self):
        homepage = HomePage(self.driver)
        search_page=homepage.search_for_a_product("samsung")
        assert search_page.display_status_of_valid_product()

    def test_search_for_an_invalid_product(self):
        homepage = HomePage(self.driver)
        search_page=homepage.search_for_a_product("Redmi")
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrieve_no_product_message().__eq__(expected_text)

    def test_searh_without_entering_any_product(self):
        homepage = HomePage(self.driver)
        search_page = homepage.search_for_a_product("")
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrieve_no_product_message().__eq__(expected_text)