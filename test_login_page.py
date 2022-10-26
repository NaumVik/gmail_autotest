from .pages.login_page import LoginPage
import pytest

# def test_user_can_go_to_password_page(browser):
#     link = 'https://accounts.google.com/v3/signin/identifier?dsh=S-435494590%3A1666185865878993&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWqpKF8YtfEQOlQB4FlAcQ-aXHwkPh_7RKfM_wy1fksvCMnFVgwIhSc0NQlSg-7TU3EiYPf3ow'
#     page = LoginPage(browser, link)
#     page.open()

# def test_right_page(browser):
#     #link = 'https://stackoverflow.com/questions/67240842/selenium-expected-browser-binary-location-but-unable-to-find-binary-in-defaul'
#     link = 'https://accounts.google.com/v3/signin/identifier?dsh=S-435494590%3A1666185865878993&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWqpKF8YtfEQOlQB4FlAcQ-aXHwkPh_7RKfM_wy1fksvCMnFVgwIhSc0NQlSg-7TU3EiYPf3ow'
#     page = LoginPage(browser, link)
#     page.open()
#     page.learn_more_button()
link = 'https://accounts.google.com/v3/signin/identifier?dsh=S-435494590%3A1666185865878993&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWqpKF8YtfEQOlQB4FlAcQ-aXHwkPh_7RKfM_wy1fksvCMnFVgwIhSc0NQlSg-7TU3EiYPf3ow'
class TestEnterValuesInLoginForm():
    def test_enter_right_value(self, browser):
        # link = 'https://accounts.google.com/v3/signin/identifier?dsh=S-435494590%3A1666185865878993&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWqpKF8YtfEQOlQB4FlAcQ-aXHwkPh_7RKfM_wy1fksvCMnFVgwIhSc0NQlSg-7TU3EiYPf3ow'
        page = LoginPage(browser, link)
        page.open()
        page.enter_right_value()

    def test_leave_empty_form(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.leave_empty_form()

    def test_enter_thirty_symbols(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.enter_thirty_symbols()

# class TestActiveButtonsRightURL():
#     @pytest.mark.learn_more
#     def test_learn_more_button(self, browser):
#         link = 'https://accounts.google.com/v3/signin/identifier?dsh=S-435494590%3A1666185865878993&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWqpKF8YtfEQOlQB4FlAcQ-aXHwkPh_7RKfM_wy1fksvCMnFVgwIhSc0NQlSg-7TU3EiYPf3ow'
#         page = LoginPage(browser, link)
#         page.open()
#         page.learn_more_button()
#
#     def test_help_button(self, browser):
#         link = 'https://accounts.google.com/v3/signin/identifier?dsh=S-435494590%3A1666185865878993&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWqpKF8YtfEQOlQB4FlAcQ-aXHwkPh_7RKfM_wy1fksvCMnFVgwIhSc0NQlSg-7TU3EiYPf3ow'
#         page = LoginPage(browser, link)
#         page.open()
#         page.help_button()