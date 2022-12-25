import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru/'

        super().__init__(web_driver, url)

    #ссылка зарегистрироваться
    register = WebElement(id='kc-register')

    #кнопка войти
    submit = WebElement(id='kc-login')

    #поле логин
    field_login = WebElement(id='username')

    #поле пароль
    field_pass = WebElement(id='password')

    #таб телефон
    tab_phone = WebElement(id='t-btn-tab-phone')

    #таб почта
    tab_mail = WebElement(id='t-btn-tab-mail')

    #ссылка забыл пароль
    forgot_pass = WebElement(id='forgot-password')

    #кнопка продолжить
    register_btn = WebElement(XPath='//*[@id="page-right"]/div/div/div/form/button')

    # кнопка далее
    forgot_pass_btn = WebElement(id='reset')

    # кнопка вернуться
    back_btn = WebElement(id='reset-back')

    # кнопка выход из личного кабинета
    exit_btn = WebElement(id='logout-btn')





    screenshot = ManyWebElements()
