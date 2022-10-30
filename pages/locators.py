from selenium.webdriver.common.by import By


class LoginPageLocators:
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


class PasswordPageLocators:
    ACCOUNT_NAME = (By.CSS_SELECTOR, 'div[class="KTeGk"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input[type="password"]')
    SHOW_PASSWORD = (By.XPATH, '//span[text()="Show password"]')
    FORGOT_PASSWORD = (By.XPATH, '//span[text()="Forgot password?"]')
    NEXT_BUTTON = (By.XPATH, '//span[text()="Next"]')
    MESSAGE_ELEMENT = (By.CSS_SELECTOR, 'div[jsname="B34EJ"] > span')


class KeyWordsForRightURL:
    LEARN_MORE_PAGE = "answer"
    HELP_PAGE = "accounts"
    PRIVACY_PAGE = "privacy"
    TERMS_PAGE = "terms"
    FORGOT_EMAIL_PAGE = "usernamerecovery"
    PASSWORD_PAGE = 'pwd'
    CREATE_PERSONAL_ACCOUNT_PAGE = "webcreateaccount"
    CREATE_CHILD_ACCOUNT_PAGE = "kidaccountinfo"
    CREATE_BUSINESS_ACCOUNT_PAGE = "webcreateaccount"
