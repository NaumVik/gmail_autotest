from selenium import webdriver

from .base_page import BasePage
from .locators import LoginPageLocators, KeyWordsForRightURL


class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.INPUT_EMAIL), "Space for enter login is not present"


    def enter_right_value(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "Shemyakin11", *LoginPageLocators.NEXT_BUTTON)


    def leave_empty_form(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "", *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Enter an email or phone number', 'Message is not present or false'


    def enter_cyrillic_symbols(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "Виктория", *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Enter a valid email or phone number', 'Message is not present or false'


    def enter_five_symbols(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "Vikon", *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Enter a valid email or phone number', 'Message is not present or false'

    def enter_six_symbols(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "Naumen",
                                    *LoginPageLocators.NEXT_BUTTON)
        #go to password page
    def enter_twenty_nine_symbols(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "Testinggoggleservicesisveryfun",
                                    *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Couldn’t find your Google Account', 'Message is not present or false'


    def enter_thirty_symbols(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "Testinggoggleservicesisveryhard", *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Enter a valid email or phone number', f'Message is not present or false, current message: {message}'

    def enter_html_tag(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "<h1>", *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Enter a valid email or phone number', 'Message is not present or false'

    def enter_email_from_another_mail_service(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "umbrella_92_0502@mail.ru", *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Couldn’t find your Google Account', 'Message is not present or false'







    def learn_more_button(self):
        self.should_be_learn_more_button()
        self.should_be_learn_more_page()

    def should_be_learn_more_button(self):
        assert self.is_element_present(*LoginPageLocators.LEARN_MORE_BUTTON), "learn more button is not present"

    def should_be_learn_more_page(self):
        assert self.go_to_right_page(*LoginPageLocators.LEARN_MORE_BUTTON, KeyWordsForRightURL.LEARN_MORE_PAGE), "Not learn more page URL"

    def help_button(self):
        self.should_be_help_button()
        self.should_be_help_page()

    def should_be_help_button(self):
        assert self.is_element_present(*LoginPageLocators.HELP_BUTTON), "Help button is not present"

    def should_be_help_page(self):
        assert self.go_to_right_page(*LoginPageLocators.HELP_BUTTON, KeyWordsForRightURL.HELP_PAGE), "Not Help page URL"

    # def should_be_register_form(self):
    #     # реализуйте проверку, что есть форма регистрации на странице
    #     assert True
