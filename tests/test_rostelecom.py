
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  Удаленно можно запустить: pytest -v --driver Remote --capability browserName chrome tests/*

import time

from pages.rostelecom import MainPage

def test_auth_valid_data_phone(web_browser):
    """Make sure auth with valid number and password """
    page = MainPage(web_browser)

    page.tab_phone.click()
    page.field_login.click()
    page.field_login.clear()
    page.field_login.send_keys('89131071785')

    time.sleep(5)

    page.field_pass.click()
    page.field_pass.clear()
    page.field_pass.send_keys('1234567Qww')
    page.submit.click()

    time.sleep(5)

    assert page.get_relative_link() == '/account_b2c/page?state='

def test_auth_invalid_data(web_browser):
    """Make sure auth with invalid number and password """
    page = MainPage(web_browser)

    page.tab_phone.click()
    page.field_login.click()
    page.field_login.clear()
    page.field_login.send_keys('89999999999')

    time.sleep(5)

    page.field_pass.click()
    page.field_pass.clear()
    page.field_pass.send_keys('QWERTY')
    page.submit.click()

    time.sleep(5)

    assert page.get_relative_link() != '/account_b2c/page?state='

def test_auth_invalid_phone(web_browser):
    """Make sure auth with invalid number """
    page = MainPage(web_browser)

    page.tab_phone.click()
    page.field_login.click()
    page.field_login.clear()
    page.field_login.send_keys('89999999999')

    time.sleep(5)

    page.field_pass.click()
    page.field_pass.clear()
    page.field_pass.send_keys('1234567Qww')
    page.submit.click()

    time.sleep(5)

    assert page.get_relative_link() != '/account_b2c/page?state='

def test_auth_invalid_pass(web_browser):
    """Make sure auth with invalid password """
    page = MainPage(web_browser)

    page.tab_phone.click()
    page.field_login.click()
    page.field_login.clear()
    page.field_login.send_keys('89131071785')

    time.sleep(5)

    page.field_pass.click()
    page.field_pass.clear()
    page.field_pass.send_keys('QWERTY')
    page.submit.click()

    time.sleep(5)

    assert page.get_relative_link() != '/account_b2c/page?state='

def test_auth_valid_data_email(web_browser):
    """Make sure auth with valid email and password """
    page = MainPage(web_browser)

    page.tab_mail.click()
    page.field_login.click()
    page.field_login.clear()
    page.field_login.send_keys('puchkoova@yandex.ru')

    time.sleep(5)

    page.field_pass.click()
    page.field_pass.clear()
    page.field_pass.send_keys('1234567Qww')
    page.submit.click()

    time.sleep(5)

    assert page.get_relative_link() == '/account_b2c/page?state='

def test_auth_invalid_data_tab_email(web_browser):
    """Make sure auth with invalid email and password """
    page = MainPage(web_browser)

    page.tab_mail.click()
    page.field_login.click()
    page.field_login.clear()
    page.field_login.send_keys('example@google.ru')

    time.sleep(5)

    page.field_pass.click()
    page.field_pass.clear()
    page.field_pass.send_keys('QWERTY')
    page.submit.click()

    time.sleep(5)

    assert page.get_relative_link() != '/account_b2c/page?state='

def test_auth_invalid_email(web_browser):
    """Make sure auth with invalid email """
    page = MainPage(web_browser)

    page.tab_mail.click()
    page.field_login.click()
    page.field_login.clear()
    page.field_login.send_keys('example@google.ru')

    time.sleep(5)

    page.field_pass.click()
    page.field_pass.clear()
    page.field_pass.send_keys('1234567Qww')
    page.submit.click()

    time.sleep(5)

    assert page.get_relative_link() != '/account_b2c/page?state='

def test_auth_invalid_pass_to_tab_mail(web_browser):
    """Make sure auth with invalid password """
    page = MainPage(web_browser)

    page.tab_mail.click()
    page.field_login.click()
    page.field_login.clear()
    page.field_login.send_keys('puchkoova@yandex.ru')

    time.sleep(5)

    page.field_pass.click()
    page.field_pass.clear()
    page.field_pass.send_keys('QWERTY')
    page.submit.click()

    time.sleep(5)

    assert page.get_relative_link() != '/account_b2c/page?state='

def test_check_register(web_browser):
    """Make sure register button visible"""

    page = MainPage(web_browser)

    page.scroll_down()
    page.register.click()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration?'
    page._web_driver.save_screenshot('rostelecom.png')

def test_check_forgot_pass(web_browser):
    """Make sure forgot password working"""

    page = MainPage(web_browser)

    page.forgot_pass.click()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/reset-credentials?'

def test_check_register_button(web_browser):
    """Make sure register button text"""

    page = MainPage(web_browser)

    page.scroll_down()
    page.register.click()

    assert page.register_btn.get_text() == 'Продолжить'

def test_check_forgot_pass_button(web_browser):
    """Make sure forgot password button text"""

    page = MainPage(web_browser)

    page.forgot_pass.click()

    assert page.forgot_pass_btn.get_text() == 'Далее'

def test_check_back_button(web_browser):
    """Make sure back button text to forgot pass"""

    page = MainPage(web_browser)

    page.forgot_pass.click()

    assert page.back_btn.get_text() == 'Вернуться'

def test_check_submit_button(web_browser):
    """Make sure submit button text"""

    page = MainPage(web_browser)

    assert page.submit.get_text() == 'Войти'

def test_cabinet_exit(web_browser):
    """Make sure user cabinet contains exit button"""
    page = MainPage(web_browser)

    page.tab_mail.click()
    page.field_login.click()
    page.field_login.clear()
    page.field_login.send_keys('puchkoova@yandex.ru')

    time.sleep(5)

    page.field_pass.click()
    page.field_pass.clear()
    page.field_pass.send_keys('1234567Qww')
    page.submit.click()

    time.sleep(5)

    page.exit_btn.click()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/authenticate?'
