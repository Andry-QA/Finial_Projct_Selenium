import time
import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage


link1 = "http://selenium1py.pythonanywhere.com/"  # Main page link
link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"  # 209 book link
link3 = "http://selenium1py.pythonanywhere.com/accounts/login/"  # Login page
link4 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"  # 209 book link + new year promo
link5 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
link6 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link7 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
link8 = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


# pytest -s -v --tb=line --language=en test_product_page.py для пазла
# pytest -v --tb=line --language=en test_product_page.py


@pytest.mark.skip
def test_user_can_solve_quiz_and_get_code(browser):
    page = ProductPage(browser, link4)
    page.open()
    page.adding_to_basket_from_product_page()
    page.solve_quiz_and_get_code()


@pytest.mark.skip
def test_user_should_see_correct_message_about_adding_product_to_basket(browser):
    page = ProductPage(browser, link5)
    page.open()
    page.adding_to_basket_from_product_page()
    page.changing_basket_total_price_after_adding_product()


@pytest.mark.skip
def test_user_can_solve_quiz_get_got_and_see_message(browser):
    page = ProductPage(browser, link7)
    page.open()
    page.adding_to_basket_from_product_page()
    page.solve_quiz_and_get_code()
    page.changing_basket_total_price_after_adding_product()


@pytest.mark.skip
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket_from_product_page()
    page.solve_quiz_and_get_code()
    page.changing_basket_total_price_after_adding_product()


@pytest.mark.skip
def test_success_message_disappears(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.adding_to_basket_from_product_page()
    page.success_message_should_disapeare(7)


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product(browser):
    page = ProductPage(browser, link8)
    page.open()
    page.adding_to_basket_from_product_page()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link8)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link8)
    page.open()
    page.adding_to_basket_from_product_page()
    page.success_message_should_disapeare(4)


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link8)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    templink = page.browser.current_url
    lpage = LoginPage(browser, templink)
    lpage.should_be_login_page()


@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link8)
    page.open()
    page.open_basket()
    page.basket_should_be_empty()
    page.should_be_empty_basket_text()


class TestUserAddToBasketFromProductPage:

    def test_user_cant_see_success_message(self):
        page = ProductPage(self, link8)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self):
        page = ProductPage(self, link8)
        page.open()
        page.adding_to_basket_from_product_page()
        page.changing_basket_total_price_after_adding_product()