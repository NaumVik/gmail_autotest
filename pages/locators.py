from selenium.webdriver.common.by import By

#TODO find all locators
class LoginPageLocators():
    FRAME_LOGIN = (By.CSS_SELECTOR, 'form[method="post"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[type="email"]')
    FORGOT_EMAIL_BUTTON = (By.XPATH, '//button[contains(text(), "Forgot email")]')
    LEARN_MORE_BUTTON = (By.XPATH, '//a[text()="Learn more"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//span[text()="Create account"]')
    NEXT_BUTTON = (By.XPATH, '//span[text()="Next"]')
    HELP_BUTTON = (By.XPATH, '//a[text()="Help"]')
    PRIVACY_BUTTON = (By.XPATH, '//a[text()="Privacy"]')
    TERMS_BUTTON = (By.XPATH, '//a[text()="Terms"]')


class PasswordPageLocators():
    pass


class KeyWordsForRightURL():
    LEARN_MORE_PAGE = "answer"
