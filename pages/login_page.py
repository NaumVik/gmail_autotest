from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def go_to_enter_password(self):
        user_name = self.browser.find_element(By.CSS_SELECTOR, 'input[type="email"]')
        user_name.send_keys("Shemyakin11")
        submit_button = self.browser.find_element(By.XPATH, '//span[text()="Next"]')
        submit_button.click()
