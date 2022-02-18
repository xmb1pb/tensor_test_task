"""
Это модуль с тестами.
"""

import pytest
from .pages.main_page import MainPage
from .pages.pictures_page import PicturesPage

"""
Заметка по первому тесту: не смотря на то, что все первые 5 результатов 
поисковой выдачи так и или иначе связаны с Тензор
ссылка на tensor.ru подержится не более, чем в двух
Тест вполне закономерно падает
"""

@pytest.mark.search_test()
class TestSearchOnMainPage:
    # поиск в яндексе
    def test_search_main_page(self, browser):
        # открываем главную страницу яндекса
        link = "https://yandex.ru/"
        # присваиваем запрос переменной
        search_query = 'тензор'
        search_link = 'tensor.ru'
        # создаем экземпляр класса
        page = MainPage(browser, link)
        # вызываем метод open и открываем страницу
        page.open()
        # убеждаемся, что поле поиска присутствует на странице
        page.should_be_search_field()
        # вводим поисковый запрос в строку поиска, но не отправляем
        page.enter_query_to_search_field(search_query)
        # ожидаем появления списка подсказок поиска и убеждаемся что он появился
        page.should_be_search_suggests_frame()
        page.should_be_shown_search_suggests_frame()
        # отправляем поисковый запрос
        page.search_query_submit()
        # проверяем, что фрейм с результатами поиска присутствует на странице
        page.should_be_search_result_frame()
        # проверяем, что в первых пяти результатах поиска есть ссылка на tensor.ru
        page.query_results_should_contain_link(search_link, 5)


@pytest.mark.pictures_test()
class TestPicturesPage:
    def test_pictures_page(self, browser):
        link = "https://yandex.ru/"
        pictures_link = "https://yandex.ru/images/"
        page = MainPage(browser, link)
        # открываем главную яндекса
        page.open()
        # проверяем наличие ссылки "Картинки"
        page.should_be_pictures_link()
        # нажимаем на "картинки" и переходим
        page.go_to_pictures_page()
        # тест падает, возможно виновато новое окно
        pictures_page = PicturesPage(browser, browser.current_url)
        # проверяем, что url верный
        pictures_page.should_be_correct_url(pictures_link)
        # выбор категории по индексу - для 1 категории индекс 0
        pictures_page.open_pictures_category(0)
        # проверяем, что категория открылась
        pictures_page.should_be_picture_category_opened()
        # проверяем, что название открытой категории картинок отображается в строке поиска
        pictures_page.pictures_category_name_displayed_in_search_field()
        # открываем картинку №1 (индекс 0) и проверяем, что открылась
        pictures_page.open_picture_category_result(0)
        # нажимаем кнопку "вперед" и проверяем что картинка изменилась
        pictures_page.open_picture_category_result_next()
        # нажимаем кнопку "вперед" и проверяем что картинка прежняя
        # дополнительно скачиваем картинки и сравниваем хэш
        pictures_page.open_picture_category_result_previous()
        pictures_page.should_be_exactly_same_pictures()


if __name__ == '__main__':
    pytest.main()
