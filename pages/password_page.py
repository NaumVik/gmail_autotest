from .locators import PasswordPageLocators
from .base_page import BasePage
from .locators import PasswordPageLocators



class PasswordPage(BasePage):
    # def should_be_login_page(self):
    #     self.should_be_password_page_url()
    #     self.should_be_password_form()
    #
    # def should_be_password_page_url(self):
    #     assert "pwd" in self.get_url_of_page(), 'Not password_page URL'

    def should_be_password_form(self):
        assert self.is_element_present(*PasswordPageLocators.INPUT_PASSWORD), 'Password form is not present'

    def leave_empty_form(self):
        self.enter_value_and_submit(*PasswordPageLocators.INPUT_PASSWORD, "", *PasswordPageLocators.NEXT_BUTTON)
        message = self.read_the_message(*PasswordPageLocators.MESSAGE_ELEMENT)
        assert message == 'Enter a password', f'Should be message: "Enter a password", current message: {message}'

    def enter_cyrillic_symbols(self):
        self.enter_value_and_submit(*PasswordPageLocators.INPUT_PASSWORD, "Виктория12345", *PasswordPageLocators.NEXT_BUTTON)
        message = self.read_the_message(*PasswordPageLocators.MESSAGE_ELEMENT)
        assert message == 'Wrong password. Try again or click Forgot password to reset it.', f'Should be message: "Wrong password. Try again or click Forgot password to reset it.", current message: {message}'

    def enter_seven_symbols(self):
        self.enter_value_and_submit(*PasswordPageLocators.INPUT_PASSWORD, "1234567", *PasswordPageLocators.NEXT_BUTTON)
        message = self.read_the_message(*PasswordPageLocators.MESSAGE_ELEMENT)
        assert message == 'Wrong password. Try again or click Forgot password to reset it.', f'Should be message: "Wrong password. Try again or click Forgot password to reset it., current message: {message}'

    def enter_eight_symbols(self):
        self.enter_value_and_submit(*PasswordPageLocators.INPUT_PASSWORD, "09876543", *PasswordPageLocators.NEXT_BUTTON)
        message = self.read_the_message(*PasswordPageLocators.MESSAGE_ELEMENT)
        assert message == 'Wrong password. Try again or click Forgot password to reset it.', f'Should be message: "Wrong password. Try again or click Forgot password to reset it., current message: {message}'

    def could_change_account(self):
        self.should_be_change_account_button()
        self.should_go_to_login_page()

    def should_be_change_account_button(self):
        assert self.is_element_present(*PasswordPageLocators.ACCOUNT_NAME)

    def should_go_to_login_page(self):
        assert self.go_to_right_page_in_the_same_window(*PasswordPageLocators.ACCOUNT_NAME, "identifier"), "Not login_page URL"

    def show_password_button(self):
        self.should_be_show_password_button()
        self.password_can_be_shown()

    def should_be_show_password_button(self):
        assert self.is_element_present(*PasswordPageLocators.SHOW_PASSWORD)

    def password_can_be_shown(self):
        password_form = self.browser.find_element(*PasswordPageLocators.INPUT_PASSWORD)
        element = self.browser.find_element(*PasswordPageLocators.SHOW_PASSWORD)
        element.click()
        view_password = password_form.get_attribute("autocomplete")
        assert view_password == "off", 'Password can not shown to user'

    def forgot_password_button(self):
        self.should_be_forgot_password_button()
        self.should_be_forgot_password_url()

    def should_be_forgot_password_button(self):
        assert self.is_element_present(*PasswordPageLocators.FORGOT_PASSWORD)

    def should_be_forgot_password_url(self):
        forgot_password_button = self.browser.find_element(*PasswordPageLocators.FORGOT_PASSWORD)
        forgot_password_button.click()
        assert "ipe" in self.get_url_of_page(), "Not forgot_password page URL"