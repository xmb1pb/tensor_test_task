import pytest
from selenium import webdriver


def pytest_addoption(parser):
    # реализована поддержка браузеров Chrome и Firefox
    parser.addoption('--browser_name', action='store', default='Chrome',
                     help="Choose browser: chrome or firefox")
    # реализован выбор языка
    parser.addoption('--language', action='store', default='ru', help='select language i.e. ru/en/es/ etc')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    firefox_options=webdriver.FirefoxOptions()
    firefox_options.add_argument("--start-maximized")
    firefox_options.set_preference("intl.accept_languages", user_language)
    browser = None
    if browser_name in ('Chrome', 'chrome'):
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name in ('Firefox', 'firefox'):
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
