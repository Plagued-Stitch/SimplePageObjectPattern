
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


# класс инциализирует ya.ru и задаёт эмуляцию интерфейса страницы
class YandexMainPage:
    def __init__(self, web_browser, url='https:/ya.ru'):

        self.web_browser = web_browser
        web_browser.get(url)


# записываются только статичные элементы
    SEARCHBAR = (By.ID, 'text')
    SUGGESTCONTAINER = (By.CLASS_NAME, 'mini-suggest__popup-content')

# функция проверяет существует ли поле поиска на странице
    def check_exists_search_bar(self):

        try:
            self.web_browser.find_element(*self.SEARCHBAR)
        except NoSuchElementException:
            return False
        finally:
            return True


# функция позволяет вводить текст в поле поиска
    def enter_text_in_search_bar(self, textsearch = ''):

        search_bar = self.web_browser.find_element(*self.SEARCHBAR)
        search_bar.send_keys(textsearch)


# функция проверяет видит ли пользователь контейнер с подсказками
    def check_exists_suggestion_container(self):

        if self.web_browser.find_element(*self.SUGGESTCONTAINER).is_displayed():
            return True
        else:
            return False


# функция позволяет эмулировать клавишу Enter
    def emulate_enter_key_in_search_bar(self):

        time.sleep(1)
        
        search_bar = self.web_browser.find_element(*self.SEARCHBAR)
        search_bar.send_keys(Keys.ENTER)


# фукнция проверяет видит ли пользователь кнопку меню
    def check_exists_yandex_menu_button(self):

        try:
            self.web_browser.find_element(By.LINK_TEXT, 'https://yandex.ru/all')
        except NoSuchElementException:
            return False
        finally:
            for i in self.web_browser.find_elements(By.TAG_NAME, 'a'):
                if i.get_attribute('title') == 'Все сервисы':
                    if i.is_displayed():
                        return True
                    else:
                        return False