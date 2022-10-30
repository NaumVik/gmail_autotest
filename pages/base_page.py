from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
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
        WebDriverWait(self.browser, 5).until(EC.new_window_is_opened([1]))
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        if search_word in self.get_url_of_page():
            return True
        else:
            return False

    def go_to_right_page_in_the_same_window(self, how, what, search_word):
        button = self.browser.find_element(how, what)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        if search_word in self.get_url_of_page():
            return True
        else:
            return False

    def read_the_message(self, how, what):
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((how, what)))
            message_element = self.browser.find_element(how, what)
            message = message_element.text
        except NoSuchElementException and TimeoutException:
            return False
        return message
