from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class FormPageLocators:
    input_email = (By.CSS_SELECTOR, 'input[type="email"]')
    button_forgot_email = (By.XPATH, '//button[contains(text(), "Забыли")]')
    button_more_details = (By.XPATH,  '//a[text()="Подробнее"]')
    submit_button = (By.XPATH, '//span[text()="Далее"]')
    help_button = (By.XPATH,  '//a[text()="Справка"]')
    personal_security_button = (By.XPATH,  '//a[text()="Конфиденциальность"]')
    conditions_button = (By.XPATH,  '//a[text()="Условия"]')