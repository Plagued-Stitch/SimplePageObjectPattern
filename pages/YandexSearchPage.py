
from selenium.webdriver.common.by import By


# класс инциализирует ya.ru/search и задаёт эмуляцию интерфейса страницы
class YandexSearchPage:
    def __init__(self, web_browser):

        self.web_browser = web_browser


# функция проверяет текст первой ссылки на страницы результатов поиска
    def check_exists_first_link(self):

        return self.web_browser.find_element(By.XPATH, '//*[@id="search-result"]/li[1]/div/div[2]/div[1]/a/b').text