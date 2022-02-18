'''
Класс для главной страницы
'''

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def should_be_search_field(self):
        # проверяет есть ли поле описка на странице
        assert self.is_element_present(*MainPageLocators.SEARCH_FIELD), \
            "Search field not found on page"

    def should_be_search_suggests_frame(self):
        # проверяет что список подсказок поиска присутствует на странице
        assert self.is_element_present(*MainPageLocators.SEARCH_SUGGESTS_FRAME), \
            "Search suggests frame not found on page"

    def should_be_shown_search_suggests_frame(self):
        # проверяет что список подсказок для поиска visible
        assert self.is_element_visible(*MainPageLocators.SEARCH_SUGGESTS_FRAME), \
            "Search suggests frame should be shown, but it's not"

    def should_be_search_result_frame(self):
        # проверяет присутствие таблицы с результатами поиска
        assert self.is_element_present(*MainPageLocators.SEARCH_RESULT_FRAME), \
            "Search results frame not found on page"

    def enter_query_to_search_field(self, text):
        # вводит text в поле поиска
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.send_keys(text)
        # search_field.submit()

    def search_query_submit(self):
        # отправляет поисковый запрос
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.submit()

    def query_results_should_contain_link(self, link, n):
        # проверяет наличие нужной ссылки в n результатах поиска
        search_result_links = self.browser.find_elements(*MainPageLocators.SEARCH_RESULT_LINK)
        for ind, i in enumerate(search_result_links[:n]):
            got_link = i.get_attribute('href')
            assert link in got_link, f'Expected \"{link}\" in search result #{ind}, got \"{got_link}\"'

    def should_be_pictures_link(self):
        # проверяет наличие ссылки на "картинки"
        assert self.is_element_present(*MainPageLocators.PICTURES_PAGE_LINK), \
            "Link to pictures page not found on main"

    def go_to_pictures_page(self):
        # кликает на ссылку "Картинки"
        pictures_link = self.browser.find_element(*MainPageLocators.PICTURES_PAGE_LINK)
        pictures_link.click()
        self.browser.switch_to.window(window_name=self.browser.window_handles[-1])
