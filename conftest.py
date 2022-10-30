import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=en-US')
    # options.add_argument("--headless")
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    browser.quit()
