from selenium.webdriver.common.by import By


class BasePageLocators():
    pass


class MainPageLocators():
    # поле ввода для поиска. текст в поле поиска get_property('value')
    SEARCH_FIELD = (By.XPATH, '//input[@class="input__control input__input mini-suggest__input"]')
    # кнопка "Найти"
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    # таблица с подсказками поиска
    SEARCH_SUGGESTS_FRAME = (By.XPATH, '//ul[@class="mini-suggest__popup-content"]')
    # элементы выпадающего списка подсказок поиска
    SEARCH_SUGGESTS_FRAME_ELEMENTS = (By.XPATH, '//ul[@class="mini-suggest__popup-content"]/li')
    # таблица с результатами поиска
    SEARCH_RESULT_FRAME = (By.XPATH, '//ul[@id="search-result"]')
    # результат поиска
    SEARCH_RESULT_LINK = (By.XPATH, '//ul[@id="search-result"]//a[contains(@class,"organic__url")]')
    # ссылка на "Картинки"
    PICTURES_PAGE_LINK = (By.XPATH, '//a[@data-id="images"]')


class PicturesPageLocators():
    # поле поиска на странице картинок. текст в поле поиска get_property('value')
    PICTURES_SEARCH_FIELD = (By.XPATH, '//input[@class="input__control mini-suggest__input"]')
    # категория картинок, название категории аттрибут data-grid-text=""
    PICTURES_CATEGORY = (By.XPATH, '//div[contains(@class, "PopularRequestList-Item")]')
    # картинка в категории
    IMAGE_GRID = (By.XPATH, '//a[@class="serp-item__link"]')
    # увеличенная картинка
    IMAGE_SHOWN = (By.XPATH, '//img[@class="MMImage-Origin"]')
    # кнопка "следующая картинка"
    IMAGE_NEXT = (By.XPATH, '//div[contains(@class, "CircleButton_type_next")]')
    # кнопка "предыдущая картинка"
    IMAGE_PREVIOUS = (By.XPATH, '//div[contains(@class, "CircleButton_type_prev")]')
