from selenium import webdriver

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        # self.should_be_register_form()

    def should_be_login_url(self):
        actual_url = str(self.get_url_of_page())
        assert 'signin' in actual_url, 'Not login url address'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FRAME_LOGIN), "Login form is not presented"


    def learn_more_button(self):
        self.should_be_learn_more_button()
        self.should_be_learn_more_page()


    def should_be_learn_more_button(self):
        assert self.is_element_present(*LoginPageLocators.BUTTON_LEARN_MORE), "learn more button is not present"



    def should_be_learn_more_page(self):
        assert self.go_to_right_page(*LoginPageLocators.BUTTON_LEARN_MORE, "answer"), "Not right page"


    # def should_be_register_form(self):
    #     # реализуйте проверку, что есть форма регистрации на странице
    #     assert True