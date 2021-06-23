import time

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage

link1 = "http://selenium1py.pythonanywhere.com/"  # Main page link
link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"  # 209 book link
link3 = "http://selenium1py.pythonanywhere.com/accounts/login/"  # Login page
link4 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"  # 209 book link + new year promo


# pytest -v --tb=line --language=en test_main_page.py


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link1)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link1)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_maim_page(browser):
    page = MainPage(browser, link1)
    page.open()
    page.open_basket()
    page.basket_should_be_empty()
    page.should_be_empty_basket_text()
