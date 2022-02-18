from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators
import urllib.request
import hashlib


def download_image(src, name):
    # скачивает картинки
    urllib.request.urlretrieve(src, f'./images/{name}.jpg')
    # возвращает имя картинки так как вызывается из hasher()
    return name


def hasher(name):
    # считает хеш для предварительно скачанной картинки
    # в качестве аргумента передается функция download_image()
    with open(f'./images/{name}.jpg', 'rb') as f:
        img_hash = hashlib.md5()
        img_hash.update(f.read())
        return img_hash.hexdigest()


class BasePage:
    # конструктор
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self) -> None:
        # открывает ссылку в браузере
        self.browser.get(self.url)

    def wait(self, by_method, elem_locator):
        WebDriverWait(self.browser, timeout=2).until(EC.presence_of_element_located((by_method, elem_locator)))

    def is_element_present(self, by_method, elem_locator) -> bool:
        # проверяет наличие элемента
        try:
            self.browser.find_element(by_method, elem_locator)
        except NoSuchElementException:
            return False
        return True

    def is_element_visible(self, by_method, elem_locator) -> bool:
        # проверяет видимость элемента
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
