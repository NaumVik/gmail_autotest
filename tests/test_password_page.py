from pages.login_page import LoginPage

link = 'https://accounts.google.com/'


class TestPasswordFrom:
    def test_password_form_is_present(self, browser):
        page = LoginPage(browser, link)
        page.open()
        password_page = page.go_to_password_page()
        password_page.should_be_password_form()

    def test_leave_empty_password_form(self, browser):
        page = LoginPage(browser, link)
        page.open()
        password_page = page.go_to_password_page()
        password_page.leave_empty_form()

    def test_enter_cyrillic_symbols(self, browser):
        page = LoginPage(browser, link)
        page.open()
        password_page = page.go_to_password_page()
        password_page.enter_cyrillic_symbols()

    def test_enter_seven_symbols(self, browser):
        page = LoginPage(browser, link)
        page.open()
        password_page = page.go_to_password_page()
        password_page.enter_seven_symbols()

    def test_enter_eight_symbols(self, browser):
        page = LoginPage(browser, link)
        page.open()
        password_page = page.go_to_password_page()
        password_page.enter_eight_symbols()


class TestShowPasswordFunction:
    def test_show_password_function(self, browser):
        page = LoginPage(browser, link)
        page.open()
        password_page = page.go_to_password_page()
        password_page.show_password_button()


class TestActiveButtons:
    def test_change_account_button(self, browser):
        page = LoginPage(browser, link)
        page.open()
        password_page = page.go_to_password_page()
        password_page.should_be_change_account_button()

    def test_forgot_password_button(self, browser):
        page = LoginPage(browser, link)
        page.open()
        password_page = page.go_to_password_page()
        password_page.forgot_password_button()
