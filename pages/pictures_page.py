'''
Здесь описан класс для страницы Картинки
'''

from selenium.webdriver import ActionChains
from .base_page import BasePage, hasher, download_image
from .locators import PicturesPageLocators
import urllib.parse


class PicturesPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.pictures_category_name = None
        self.initial_img_src = None
        self.next_img_src = None
        self.revisited_img_src = None

    def open_pictures_category(self, index):
        # открывает n категорию картинок
        pictures_category = self.browser.find_elements(*PicturesPageLocators.PICTURES_CATEGORY)
        self.pictures_category_name = pictures_category[index].get_attribute('data-grid-text')
        pictures_category[index].click()

    def open_picture_category_result(self, index):
        # открывает n картинку в категории
        image_grid_result = self.browser.find_elements(*PicturesPageLocators.IMAGE_GRID)
        image_grid_result[index].click()
        # проверяет что картинка отрылась
        self.wait(*PicturesPageLocators.IMAGE_SHOWN)
        assert self.is_element_present(*PicturesPageLocators.IMAGE_SHOWN), "Seems that picture is not opened"
        self.initial_img_src = self.browser.find_element(*PicturesPageLocators.IMAGE_SHOWN).get_attribute('src')

    def open_picture_category_result_next(self):
        hover = ActionChains(self.browser).move_to_element(self.browser.find_element(*PicturesPageLocators.IMAGE_SHOWN))
        hover.perform()
        img_forward = self.browser.find_element(*PicturesPageLocators.IMAGE_NEXT)
        img_forward.click()
        self.next_img_src = self.browser.find_element(*PicturesPageLocators.IMAGE_SHOWN).get_attribute('src')
        assert self.initial_img_src != self.next_img_src, "Seems that picture had not changed"

    def open_picture_category_result_previous(self):
        hover = ActionChains(self.browser).move_to_element(self.browser.find_element(*PicturesPageLocators.IMAGE_SHOWN))
        hover.perform()
        img_backward = self.browser.find_element(*PicturesPageLocators.IMAGE_PREVIOUS)
        img_backward.click()
        self.revisited_img_src = self.browser.find_element(*PicturesPageLocators.IMAGE_SHOWN).get_attribute('src')

    def should_be_exactly_same_pictures(self):
        hash_a = hasher(download_image(self.initial_img_src, 'initial'))
        hash_b = hasher(download_image(self.revisited_img_src, 'revisited'))
        assert hash_a == hash_b, f"Initial and revisited pictures arent same: {hash_a} vs {hash_b}"

    def should_be_picture_category_opened(self):
        # проверяет что категория картинок открылась
        self.should_be_pictures_category_name_in_url()
        self.should_be_result_pictures_grid()

    def should_be_pictures_category_name_in_url(self):
        # проверяет наличие названия категории в URL страницы
        assert urllib.parse.quote(self.pictures_category_name) in self.browser.current_url, \
            f"\"{self.pictures_category_name}\" is not present in page URL {self.browser.current_url}"

    def should_be_result_pictures_grid(self):
        # проверяет наличие картинок в открытой категории
        result_pictures_grid = self.browser.find_elements(*PicturesPageLocators.IMAGE_GRID)
        assert len(result_pictures_grid) > 0, "Seems that no search results displayed"

    def pictures_category_name_displayed_in_search_field(self):
        # проверяет наличие названия открытой категории в строке поиска
        picture_search_field_text = self.browser.find_element(*PicturesPageLocators.PICTURES_SEARCH_FIELD).get_property(
            'value')
        assert self.pictures_category_name == picture_search_field_text, \
            f"Pictures category name differs from displayed in search field. \n" \
            f"Expected \"{self.pictures_category_name}\", got \"{picture_search_field_text}\""

    def should_be_correct_url(self, link):
        assert link in self.browser.current_url, \
            f'Seems that opened wrong URL . Expected \"{link}\", got \"{self.browser.current_url}\"'
