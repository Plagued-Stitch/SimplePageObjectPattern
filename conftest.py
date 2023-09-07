
import pytest


# фикстура конфигурации pytest задаёт аргументы браузера chromedriver.exe (Chrome)
@pytest.fixture
def chrome_options(chrome_options):

    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')
    chrome_options.add_argument('--start-maximized')

    return chrome_options


# функция выводит более подробный репорт кода при test_case FAILED
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    return rep


# функция задаёт пресет driver
@pytest.fixture
def web_browser(selenium):

    browser = selenium
    yield browser


# функция предоставляет кастомный функционал для имплементации doc string комментария
def get_test_case_docstring(item):

    full_name = ''

    if item._obj.__doc__:

        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])

            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]

            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


# функция имплементирует doc string комментарий в консоль
def pytest_itemcollected(item):

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


# функция имплементирует doc string комментарий в консоль с параметром --collect-only
def pytest_collection_finish(session):

    if session.config.option.collectonly is True:

        for item in session.items:
            
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')