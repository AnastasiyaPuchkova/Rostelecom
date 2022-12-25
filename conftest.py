#!/usr/bin/python3
# -*- encoding=utf8 -*-

# Этот пример показывает, как мы можем управлять неудачными тестами
# и делать скриншоты после любого неудачного тестового примера.

import pytest
import uuid


@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')  #чтобы браузер не блокировался
    chrome_options.add_argument('--log-level=DEBUG') #задаём уровень логов

    return chrome_options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    #Эта функция помогает обнаружить, что какой-то тест не прошел успешно,
    # и передать эту информацию в teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    browser.set_window_size(1400, 1000)

    # Return browser instance to test case:
    yield browser

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Делаем скриншот если тест падает:
        try:
            browser.execute_script("document.body.bgColor = 'white';")#подкладываем белый фон и делаем скриншот

            # Скриншот для локальной отладки (debug):
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # Приложение скриншота к отчету:
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG) #если подключен алюр

            # For happy debugging:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass # just ignore any errors here


def get_test_case_docstring(item):
    """ Эта функция получает строку документа из тестового примера и форматирует ее,
        чтобы показывать эту строку документа вместо имени тестового примера в отчетах.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ Эта функция изменяет названия тестовых примеров "на лету".
        во время выполнения тестовых случаев.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ Эта функция изменяет имена тестовых примеров "на лету",
        когда мы используем параметр --collect-only для pytest
        (чтобы получить полный список всех существующих тестовых примеров).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to
            # it's doc string to show human-readable reports and to
            # automatically import test cases to test management system.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')
