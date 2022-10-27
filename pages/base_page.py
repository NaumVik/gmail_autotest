from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)


    def get_url_of_page(self):
        need_url = self.browser.current_url
        return need_url

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def enter_value_and_submit(self, how, what, value, how2, what2):
        form = self.browser.find_element(how, what)
        form.send_keys(value)
        submit_button = self.browser.find_element(how2, what2)
        submit_button.click()

    def go_to_right_page_in_new_window(self, how, what, search_word):
        button = self.browser.find_element(how, what)
        button.click()
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        if search_word in self.get_url_of_page():
            return True
        else:
            return False





    # def go_to_another_page(self):
    #     sign_in_button = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     sign_in_button.click()
