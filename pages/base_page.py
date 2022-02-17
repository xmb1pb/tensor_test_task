import math
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage:
    # конструктор
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self) -> None:
        # открывает ссылку в браузере
        self.browser.get(self.url)

    def is_element_present(self, by_method, elem_locator) -> bool:
        # проверяет наличие элемента
        try:
            self.browser.find_element(by_method, elem_locator)
        except NoSuchElementException:
            return False
        return True

    def is_element_visible(self, by_method, elem_locator) -> bool:
        try:
            WebDriverWait(self.browser, timeout=4).until(EC.visibility_of_element_located((by_method, elem_locator)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, by_method, elem_locator, timeout=4) -> bool:
        # проверяет отсутствие элемента
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by_method, elem_locator)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, by_method, elem_locator, timeout=4) -> bool:
        # проверяет что элемент исчезает когда надо
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((by_method, elem_locator)))
        except TimeoutException:
            return False
        return True




