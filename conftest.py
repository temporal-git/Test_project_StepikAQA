import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action="store", default='en',
                     help='Choose language: en/ru/fr...(etc)')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options_firefox)
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
