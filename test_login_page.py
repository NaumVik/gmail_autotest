from .pages.login_page import LoginPage

def test_user_can_go_to_password_page(browser):
    link = 'https://accounts.google.com/AccountChooser/identifier?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_enter_password()
