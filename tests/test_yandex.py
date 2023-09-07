
import pytest

from pages.YandexPage import YandexMainPage
from pages.YandexSearchPage import YandexSearchPage


# Тест поисковой системы ya.ru, кол-во assert эквивалентно шагам в задании с действием "проверить"
def test_yandex_search(web_browser):
    '''Test Yandex search'''

    yandexpage = YandexMainPage(web_browser)

    assert yandexpage.check_exists_search_bar() == True, 'Search bar isnt exists'

    yandexpage.enter_text_in_search_bar('Тензор')

    assert yandexpage.check_exists_suggestion_container() == True, 'Suggestions isnt exists'

    yandexpage.emulate_enter_key_in_search_bar()

    assert 'ya.ru/search/' in web_browser.current_url, 'The result page isnt loaded'

    yandexsearchpage = YandexSearchPage(web_browser)

    assert yandexsearchpage.check_exists_first_link() == 'tensor.ru', f'The first link is: {yandexsearchpage.check_exists_first_link()}'


# Тест не может быть физически продолжен если следовать тех.заданию
@pytest.mark.xfail(reason='Task step cant be passed due new ya.ru page frontend design')
def test_yandex_pictures(web_browser):
    '''Test Yandex Pictures
    
        NOTE: Because of updated ya.ru page design Pictures button is hidden by default now - test cant be followed 'step by step' as it said in the task'''

    yandexpage = YandexMainPage(web_browser)

    assert yandexpage.check_exists_yandex_menu_button() == True, 'Yandex menu button isnt displayed'