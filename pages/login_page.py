from selenium import webdriver
from .base_page import BasePage
from .locators import LoginPageLocators, KeyWordsForRightURL
from selenium.webdriver.support.ui import Select
from random import choice
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.INPUT_EMAIL), "Form for enter login is not present"


    def enter_valid_value(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "Shemyakin11", *LoginPageLocators.NEXT_BUTTON)


    def leave_empty_form(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "", *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Enter an email or phone number', f'Message is not present or false, current message: {message}'


    def enter_cyrillic_symbols(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "Виктория", *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Enter a valid email or phone number', f'Message is not present or false, current message: {message}'


    def enter_five_symbols(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "Vikon", *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Enter a valid email or phone number', f'Message is not present or false, current message: {message}'

    def enter_six_symbols(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "Naumen",
                                    *LoginPageLocators.NEXT_BUTTON)
        #go to password page
    def enter_twenty_nine_symbols(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "Testinggoggleservicesisveryfun",
                                    *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Couldn’t find your Google Account', f'Message is not present or false, current message: {message}'


    def enter_thirty_symbols(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "Testinggoggleservicesisveryhard", *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Enter a valid email or phone number', f'Message is not present or false, current message: {message}'

    def enter_html_tag(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "<h1>", *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Enter a valid email or phone number', f'Message is not present or false, current message: {message}'

    def enter_email_from_another_mail_service(self):
        self.enter_value_and_submit(*LoginPageLocators.INPUT_EMAIL, "umbrella_92_0502@mail.ru", *LoginPageLocators.NEXT_BUTTON)
        message_element = self.browser.find_element(*LoginPageLocators.MESSAGE_ELEMENT)
        message = message_element.text
        assert message == 'Couldn’t find your Google Account', f'Message is not present or false, current message: {message}'


    def learn_more_button(self):
        self.should_be_learn_more_button()
        self.should_be_learn_more_page()

    def should_be_learn_more_button(self):
        assert self.is_element_present(*LoginPageLocators.LEARN_MORE_BUTTON), "learn_more button is not present"

    def should_be_learn_more_page(self):
        assert self.go_to_right_page_in_new_window(*LoginPageLocators.LEARN_MORE_BUTTON, KeyWordsForRightURL.LEARN_MORE_PAGE), "Not learn more page URL"

    def help_button(self):
        self.should_be_help_button()
        self.should_be_help_page()

    def should_be_help_button(self):
        assert self.is_element_present(*LoginPageLocators.HELP_BUTTON), "Help button is not present"

    def should_be_help_page(self):
        assert self.go_to_right_page_in_new_window(*LoginPageLocators.HELP_BUTTON, KeyWordsForRightURL.HELP_PAGE), "Not Help_page URL"

    def privacy_button(self):
        self.should_be_privacy_button()
        self.should_be_privacy_page()

    def should_be_privacy_button(self):
        assert self.is_element_present(*LoginPageLocators.PRIVACY_BUTTON), "Privacy button is not present"

    def should_be_privacy_page(self):
        assert self.go_to_right_page_in_new_window(*LoginPageLocators.PRIVACY_BUTTON,
                                                   KeyWordsForRightURL.PRIVACY_PAGE), "Not privacy_page URL"

    def terms_button(self):
        self.should_be_terms_button()
        self.should_be_terms_page()

    def should_be_terms_button(self):
        assert self.is_element_present(*LoginPageLocators.TERMS_BUTTON), "Terms button is not present"

    def should_be_terms_page(self):
        assert self.go_to_right_page_in_new_window(*LoginPageLocators.TERMS_BUTTON,
                                                   KeyWordsForRightURL.TERMS_PAGE), "Not terms_page URL"

    def forgot_email_button(self):
        self.should_be_forgot_email_button()
        self.should_be_forgot_email_page()

    def should_be_forgot_email_button(self):
        assert self.is_element_present(*LoginPageLocators.FORGOT_EMAIL_BUTTON), "Forgot_email button is not present"

    def should_be_forgot_email_page(self):
        forgot_email_button = self.browser.find_element(*LoginPageLocators.FORGOT_EMAIL_BUTTON)
        forgot_email_button.click()
        assert "usernamerecovery" in self.get_url_of_page(), "Not forgot_email page URL"

    # def create_account_button(self):
    #     self.should_be_create_account_button()
    #     self.should_be_create_personal_account_page()
    #     self.should_be_create_child_account_page()

    def should_be_create_account_button(self):
        assert self.is_element_present(*LoginPageLocators.CREATE_ACCOUNT_BUTTON), "Create_account button is not present"


    def should_be_create_personal_account_page(self):
        create_account_button = self.browser.find_element(*LoginPageLocators.CREATE_ACCOUNT_BUTTON)
        create_account_button.click()
        assert self.go_to_right_page_in_the_same_window(*LoginPageLocators.CREATE_ACCOUNT_PERSONAL,"webcreateaccount"), \
            "Not create_personal_account page URL"

    def should_be_create_child_account_page(self):
        # sign_in_button = self.browser.find_element(By.XPATH, '//span[text()="Sign in instead"]')
        # sign_in_button.click()
        create_account_button = self.browser.find_element(*LoginPageLocators.CREATE_ACCOUNT_BUTTON)
        create_account_button.click()
        assert self.go_to_right_page_in_the_same_window(*LoginPageLocators.CREATE_ACCOUNT_FOR_CHILD,"kidaccountinfo"), \
            "Not create_child_account page URL"

    def should_be_create_for_business_account_page(self):
        create_account_button = self.browser.find_element(*LoginPageLocators.CREATE_ACCOUNT_BUTTON)
        create_account_button.click()
        assert self.go_to_right_page_in_the_same_window(*LoginPageLocators.CREATE_ACCOUNT_FOR_BUSINESS, "webcreateaccount"), \
            "Not create_personal_account page URL"

    def could_change_language(self):
        self.should_be_change_language_box()
        self.should_page_in_diff_language()

    def should_be_change_language_box(self):
        assert self.is_element_present(*LoginPageLocators.LANGUAGE_PAGE_BUTTON), "Language button is not present"


#TODO not interaction button language
    def should_page_in_diff_language(self):
        language_box = self.browser.find_element(*LoginPageLocators.LANGUAGE_PAGE_BUTTON)
        language_box.click()
        another_language = self.browser.find_element(*LoginPageLocators.LANGUAGE_TO_CHANGE_BUTTON)
        another_language.click()
        assert self.is_element_present(*LoginPageLocators.ANOTHER_LANGUAGE_BUTTON), "Language is not change"
