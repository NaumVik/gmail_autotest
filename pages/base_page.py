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

#TODO modify this function to get the right url(compare)
    def get_url_of_page(self):
        need_url = self.browser.current_url
        return need_url

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

#TODO change place to setup in class of test
    def go_to_right_page(self, how, what, search_word):
        try:
            button = self.browser.find_element(how, what)
            button.click()
            actual_url = str(self.get_url_of_page())
            if search_word in actual_url:
                return True
        except:
            return False
        return True




    # def go_to_another_page(self):
    #     sign_in_button = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     sign_in_button.click()
