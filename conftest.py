import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    # options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_UK'})
    options.add_argument('--lang=en_US')
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    # print("\nquit browser..")
    browser.quit()
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @pytest.fixture(scope="function")
# def browser():
#     browser_service = Service(ChromeDriverManager().install())
#     browser = webdriver.Chrome(service=browser_service)
#     # browser.maximize_window()
#     yield browser
#     browser.quit()

