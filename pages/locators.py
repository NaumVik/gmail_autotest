from selenium.webdriver.common.by import By


class LoginPageLocators():
    FRAME_LOGIN = (By.CSS_SELECTOR, 'form[method="post"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[type="email"]')
    BUTTON_FORGOT_EMAIL = (By.XPATH, '//button[contains(text(), "Забыли")]')
    BUTTON_MORE_DETAILS = (By.XPATH, '//a[text()="Подробнее"]')
    SUBMIT_BUTTON = (By.XPATH, '//span[text()="Далее"]')
    HELP_BUTTON = (By.XPATH, '//a[text()="Справка"]')
    PERSONAL_SECURITY_BUTTON = (By.XPATH, '//a[text()="Конфиденциальность"]')
    CONDITIONS_BUTTON = (By.XPATH, '//a[text()="Условия"]')