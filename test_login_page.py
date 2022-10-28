from .pages.login_page import LoginPage
import pytest

link = 'https://accounts.google.com/v3/signin/identifier?dsh=S-435494590%3A1666185865878993&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWqpKF8YtfEQOlQB4FlAcQ-aXHwkPh_7RKfM_wy1fksvCMnFVgwIhSc0NQlSg-7TU3EiYPf3ow'

class TestEnterValuesInLoginForm():
    def test_login_form_is_present(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_form()

    def test_enter_valid_value(self, browser):
        # link = 'https://accounts.google.com/v3/signin/identifier?dsh=S-435494590%3A1666185865878993&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWqpKF8YtfEQOlQB4FlAcQ-aXHwkPh_7RKfM_wy1fksvCMnFVgwIhSc0NQlSg-7TU3EiYPf3ow'
        page = LoginPage(browser, link)
        page.open()
        page.enter_valid_value()

    def test_leave_empty_form(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.leave_empty_form()

    def test_enter_cyrillic_symbols(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.enter_cyrillic_symbols()

    def test_enter_five_symbols(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.enter_five_symbols()

    def test_enter_six_symbols(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.enter_six_symbols()

    def test_enter_twenty_nine_symbols(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.enter_twenty_nine_symbols()

    def test_enter_thirty_symbols(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.enter_thirty_symbols()

    def test_enter_html_tag(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.enter_html_tag()

    def test_enter_email_from_another_mail_service(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.enter_email_from_another_mail_service()

class TestActiveButtons():
    # @pytest.mark.learn_more
    def test_learn_more_button(self, browser):
        #link = 'https://accounts.google.com/v3/signin/identifier?dsh=S-435494590%3A1666185865878993&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWqpKF8YtfEQOlQB4FlAcQ-aXHwkPh_7RKfM_wy1fksvCMnFVgwIhSc0NQlSg-7TU3EiYPf3ow'
        page = LoginPage(browser, link)
        page.open()
        page.learn_more_button()

    def test_help_button(self, browser):
        #link = 'https://accounts.google.com/v3/signin/identifier?dsh=S-435494590%3A1666185865878993&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWqpKF8YtfEQOlQB4FlAcQ-aXHwkPh_7RKfM_wy1fksvCMnFVgwIhSc0NQlSg-7TU3EiYPf3ow'
        page = LoginPage(browser, link)
        page.open()
        page.help_button()

    def test_privacy_button(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.privacy_button()

    def test_terms_button(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.terms_button()

    def test_forgot_email_button(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.forgot_email_button()

    # @pytest.mark.create_account
    # def test_create_account_button(self, browser):
    #     page = LoginPage(browser, link)
    #     page.open()
    #     page.create_account_button()

class TestCreateAccountButton():
    def test_presence_of_create_account_button(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_create_account_button()

    def test_creation_button_for_person(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_create_personal_account_page()

    def test_creation_button_for_child(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_create_child_account_page()

    def test_creation_button_for_business(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_create_for_business_account_page()