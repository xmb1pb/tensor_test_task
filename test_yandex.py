import pytest
from .pages.main_page import MainPage
from .pages.pictures_page import PicturesPage


@pytest.mark.search_test()
class TestSearchOnMainPage():
    # поиск в яндексе
    def test_should_be_search_field_on_main_page(self, browser):
        # открываем главную страницу яндекса
        link = "https://yandex.ru/"
        # присваиваем запрос переменной
        search_query='тензор'
        search_link='tensor.ru'
        # создаем экземпляр класса
        page = MainPage(browser, link)
        # вызываем метод open и открываем страницу
        page.open()
        # убеждаемся что поле поиска присутствует на странице
        page.should_be_search_field()
        # вводим поисковый запрос в строку поиска, но не отправляем
        page.enter_query_to_search_field(search_query)
        # ожидаем появления списка подсказок поиска и убеждаемся что он появился
        page.should_be_shown_search_suggests_frame()
        # отправляем поисковый запрос
        page.search_query_submit()
        # проверяем что фрейм с результатами поиска присутствует на странице
        page.should_be_search_result_frame()
        # проверяем что в первых пяти результатах поиска есть ссылка на tensor.ru
        page.query_results_should_contain_link(search_link, 5)

'''
    def test_guest_can_go_to_login_page_from_main_page(self, browser):
        # гость может перейти на страницу входа с главной страницы
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
'''

'''
@pytest.mark.pictures_test()
class TestPicturesPage():
    def test_should_be_search_field_on_main_page(self, browser):
        # гость видит ссылку "войти\регистрация" на главной странице
        link = "https://yandex.ru/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_search_field()
        page.

    def test_guest_can_go_to_login_page_from_main_page(self, browser):
        # гость может перейти на страницу входа с главной страницы
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
'''


if __name__ == '__main__':
    pytest.main()
