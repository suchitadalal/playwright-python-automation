from playwright.sync_api import Page


class TextBoxPage:
    """Page Object Model for DemoQA Text Box page"""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://demoqa.com/text-box"

    # Locators
    fullname_input = "//input[@id='userName']"
    email_input = "//input[@id='userEmail']"
    current_address_textarea = "//textarea[@id='currentAddress']"
    permanent_address_textarea = "//textarea[@id='permanentAddress']"
    submit_button = "//button[@id='submit']"
    output_name = "//p[@id='name']"
    output_email = "//p[@id='email']"
    output_current_address = "//p[@id='currentAddress']"
    output_permanent_address = "//p[@id='permanentAddress']"

    def navigate(self):
        """Navigate to Text Box page"""
        self.page.goto(self.url)

    def enter_fullname(self, fullname: str):
        """Enter full name in the text box"""
        self.page.fill(self.fullname_input, fullname)

    def enter_email(self, email: str):
        """Enter email in the text box"""
        self.page.fill(self.email_input, email)

    def enter_current_address(self, address: str):
        """Enter current address in the textarea"""
        self.page.fill(self.current_address_textarea, address)

    def enter_permanent_address(self, address: str):
        """Enter permanent address in the textarea"""
        self.page.fill(self.permanent_address_textarea, address)

    def click_submit(self):
        """Click the submit button"""
        self.page.click(self.submit_button)

    def get_output_name(self) -> str:
        """Get the output name from the result"""
        return self.page.text_content(self.output_name)

    def get_output_email(self) -> str:
        """Get the output email from the result"""
        return self.page.text_content(self.output_email)

    def get_output_current_address(self) -> str:
        """Get the output current address from the result"""
        return self.page.text_content(self.output_current_address)

    def get_output_permanent_address(self) -> str:
        """Get the output permanent address from the result"""
        return self.page.text_content(self.output_permanent_address)

    def fill_and_submit(self, fullname: str, email: str, current_address: str, permanent_address: str):
        """Fill all fields and submit the form"""
        self.enter_fullname(fullname)
        self.enter_email(email)
        self.enter_current_address(current_address)
        self.enter_permanent_address(permanent_address)
        self.click_submit()

    def fill_full_name(self, fullname: str):
        """Alias method for filling full name."""
        self.enter_fullname(fullname)

    def fill_email(self, email: str):
        """Alias method for filling email."""
        self.enter_email(email)

    def fill_current_address(self, address: str):
        """Alias method for filling current address."""
        self.enter_current_address(address)

    def fill_permanent_address(self, address: str):
        """Alias method for filling permanent address."""
        self.enter_permanent_address(address)

    def clear_full_name(self):
        """Clear the full name field."""
        self.page.fill(self.fullname_input, "")

    def clear_email(self):
        """Clear the email field."""
        self.page.fill(self.email_input, "")

    def get_full_name_value(self) -> str:
        """Return the current full name field value."""
        return self.page.input_value(self.fullname_input)

    def get_email_value(self) -> str:
        """Return the current email field value."""
        return self.page.input_value(self.email_input)

    def is_result_displayed(self) -> bool:
        """Return True if the name output is visible after submission."""
        return self.page.is_visible(self.output_name)

    def get_result_text(self) -> str:
        """Return the submitted full name text output without the label prefix."""
        output = self.get_output_name()
        if output and output.startswith("Name:"):
            return output.replace("Name:", "", 1).strip()
        return output or ""

    def is_error_displayed(self) -> bool:
        """Return True if the entered email is invalid."""
        return self.page.eval_on_selector(self.email_input, "el => !el.checkValidity()")
