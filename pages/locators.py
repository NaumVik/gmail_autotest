from selenium.webdriver.common.by import By

#TODO find all locators
class LoginPageLocators():
    FRAME_LOGIN = (By.CSS_SELECTOR, 'form[method="post"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[type="email"]')
    MESSAGE_ELEMENT = (By.CSS_SELECTOR, 'div[class="o6cuMc"]')
    FORGOT_EMAIL_BUTTON = (By.XPATH, '//button[contains(text(), "Forgot email")]')
    LEARN_MORE_BUTTON = (By.XPATH, '//a[text()="Learn more"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//span[text()="Create account"]')
    CREATE_ACCOUNT_PERSONAL = (By.XPATH, '//span[text()="For my personal use"]')
    CREATE_ACCOUNT_FOR_CHILD = (By.XPATH, '//span[text()="For my child"]')
    CREATE_ACCOUNT_FOR_BUSINESS = (By.XPATH, '//span[text()="For work or my business"]')
    NEXT_BUTTON = (By.XPATH, '//span[text()="Next"]')
    HELP_BUTTON = (By.XPATH, '//a[text()="Help"]')
    PRIVACY_BUTTON = (By.XPATH, '//a[text()="Privacy"]')
    TERMS_BUTTON = (By.XPATH, '//a[text()="Terms"]')
    LANGUAGE_PAGE_BUTTON = (By.CSS_SELECTOR, 'div[role="combobox"]')
    LANGUAGE_TO_CHANGE_BUTTON = (By.CSS_SELECTOR, 'li[data-value="be"]')
    ANOTHER_LANGUAGE_BUTTON = (By.XPATH, '//a[text()="Даведацца больш"]')



class PasswordPageLocators():
    pass


class KeyWordsForRightURL():
    LEARN_MORE_PAGE = "answer" #support.google.com/accounts/answer/2917834
    HELP_PAGE = "accounts" #support.google.com/accounts
    PRIVACY_PAGE = "privacy"
    TERMS_PAGE = "terms"
    FORGOT_EMAIL_PAGE = "usernamerecovery"