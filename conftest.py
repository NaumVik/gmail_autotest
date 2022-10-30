import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    # options.add_argument("--headless")
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    browser.quit()
