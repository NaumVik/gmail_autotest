from .pages.login_page import LoginPage
import pytest

# def test_user_can_go_to_password_page(browser):
#     link = 'https://accounts.google.com/v3/signin/identifier?dsh=S-435494590%3A1666185865878993&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWqpKF8YtfEQOlQB4FlAcQ-aXHwkPh_7RKfM_wy1fksvCMnFVgwIhSc0NQlSg-7TU3EiYPf3ow'
#     page = LoginPage(browser, link)
#     page.open()

def test_right_page(browser):
    #link = 'https://stackoverflow.com/questions/67240842/selenium-expected-browser-binary-location-but-unable-to-find-binary-in-defaul'
    link = 'https://accounts.google.com/v3/signin/identifier?dsh=S-435494590%3A1666185865878993&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWqpKF8YtfEQOlQB4FlAcQ-aXHwkPh_7RKfM_wy1fksvCMnFVgwIhSc0NQlSg-7TU3EiYPf3ow'
    page = LoginPage(browser, link)
    page.open()
    page.learn_more_button()

# class TestActiveButtonsRightURL():
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self, browser):
#         pass
#         yield
#         browser.get(self, 'https://accounts.google.com/v3/signin/identifier?dsh=S-435494590%3A1666185865878993&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowEntry=ServiceLogin&flowName=GlifWebSignIn&ifkv=AQDHYWrw3jPWmsyyW0_qKjmH2eUNsEkRGwDwozbASvvWWzMmidt2jpaeYFeOtk2P_y-MuYCQtMNwrA&rip=1&service=mail')
