import pytest  # type: ignore[import]
import os
import sys
import json  # Add this import
from playwright.sync_api import Page
from code.pom.textboxpage import TextBoxPage
from utility.Logger import LogGen

logger = LogGen.loggen()

class TestTextBox:
    """Test cases for TextBox functionality"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup test - initialize page and navigate to textbox"""
        logger.info("Setting up test")
        self.page = page
        self.textbox_page = TextBoxPage(page)
        self.textbox_page.navigate()

    def test_fill_textbox_with_valid_data(self):
        logger.info("Test started")
        # Load data from JSON file
        """with open('data/text_box.xlsx/csv', 'r') as f:
            data = xls/csv.load(f)"""

        with open('data/text_box.json', 'r') as f:
            data = json.load(f)

        record = data[0]
        full_name = record['fullName']
        email = record['email']
        current_address = record['currentAddress']
        permanent_address = record['permanentAddress']

        self.textbox_page.fill_full_name(full_name)
        self.textbox_page.fill_email(email)
        self.textbox_page.fill_current_address(current_address)
        self.textbox_page.fill_permanent_address(permanent_address)
        self.textbox_page.click_submit()

        assert self.textbox_page.is_result_displayed()
        assert self.textbox_page.get_result_text() == full_name

    def test_fill_textbox_with_empty_fields(self):
        """Test textbox with empty required fields"""
        self.textbox_page.click_submit()
        assert not self.textbox_page.is_result_displayed()

    def test_fill_textbox_email_validation(self):
        """Test textbox with invalid email"""
        self.textbox_page.fill_full_name("Test User")
        self.textbox_page.fill_email("invalid-email")
        self.textbox_page.fill_current_address("Test Address")
        self.textbox_page.click_submit()

        assert self.textbox_page.is_error_displayed()

    def test_clear_textbox_fields(self):
        """Test clearing textbox fields"""
        self.textbox_page.fill_full_name("Jane Doe")
        self.textbox_page.fill_email("jane@example.com")

        self.textbox_page.clear_full_name()
        self.textbox_page.clear_email()

        assert self.textbox_page.get_full_name_value() == ""
        assert self.textbox_page.get_email_value() == ""

logger.info("Test cases for TextBox functionality executed successfully.")

