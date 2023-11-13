import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def options():
    options = Options()
    options.add_argument('--window-size=2880,1800')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return options 


@pytest.fixture 
def browser(options):
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def wait(browser):
    wait = WebDriverWait(browser, timeout=10)
    return wait
