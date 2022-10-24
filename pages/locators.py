from selenium.webdriver.common.by import By

#TODO find all locators
class LoginPageLocators():
    FRAME_LOGIN = (By.CSS_SELECTOR, 'form[method="post"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[type="email"]')
    BUTTON_FORGOT_EMAIL = (By.XPATH, '//button[contains(text(), "Forgot email")]')
    BUTTON_LEARN_MORE = (By.XPATH, '//a[text()="Learn more"]')
    NEXT_BUTTON = (By.XPATH, '//span[text()="Next"]')
    HELP_BUTTON = (By.XPATH, '//a[text()="Help"]')
    PERSONAL_SECURITY_BUTTON = (By.XPATH, '//a[text()="Privacy"]')
    CONDITIONS_BUTTON = (By.XPATH, '//a[text()="Terms"]')


class PasswordPageLocators():
    pass