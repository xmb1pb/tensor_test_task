from selenium.webdriver.common.by import By


class BasePageLocators():
    pass


class MainPageLocators():
    # поле ввода для поиска
    SEARCH_FIELD = (By.XPATH, '//input[@class="input__control input__input mini-suggest__input"]')
    # кнопка "Найти"
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    # таблица с подсказками поиска
    SEARCH_SUGGESTS_FRAME = ((By.XPATH, '//ul[@class="mini-suggest__popup-content"]'))
    # элементы выпадающего списка подсказок поиска
    SEARCH_SUGGESTS_FRAME_ELEMENTS = (By.XPATH, '//ul[@class="mini-suggest__popup-content"]/li')
    # таблица с результатами поиска
    SEARCH_RESULT_FRAME = (By.XPATH, '//ul[@id="search-result"]')
    # результат поиска
    SEARCH_RESULT_LINK = (By.XPATH, '//ul[@id="search-result"]//a[contains(@class,"organic__url")]')
    # ссылка на "Картинки"
    PICTURES_PAGE_LINK = (By.XPATH, '//a[@data-id="images"]')

class PicturesPageLocators():
    # форма ввода логина
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    # форма регистрации
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    # поле ввода мейла при регистрации
    REGISTER_EMAIL = (By.XPATH, '//input[@name="registration-email"]')
    # поле ввода пароля при регистрации
    REGISTER_PASS = (By.XPATH, '//input[@name="registration-password1"]')
    # поле подтверждения пароля
    REGISTER_PASS_CONFIRM = (By.XPATH, '//input[@name="registration-password2"]')
    # кнопка завершения регистрации
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')

