import pytest
from pages.login_page import LoginPage

link1 = "http://selenium1py.pythonanywhere.com/"  # Main page link
link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"  # 209 book link
link3 = "http://selenium1py.pythonanywhere.com/accounts/login/"  # Login page


# pytest -v --tb=line -m login_guest --language=en test_login_page.py
# pytest -v --tb=line --language=en test_login_page.py

@pytest.mark.skip
def test_guest_should_be_at_login_page(browser):
    page = LoginPage(browser, link3)
    page.open()
    page.should_be_login_page()


@pytest.mark.skip
def test_guest_should_see_login_in_current_url(browser):
    page = LoginPage(browser, link3)
    page.open()
    page.should_be_login_url()


@pytest.mark.skip
def test_guest_should_see_register_form(browser):
    page = LoginPage(browser, link3)
    page.open()
    page.should_be_register_form()


@pytest.mark.skip
def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, link3)
    page.open()
    page.should_be_login_form()


@pytest.mark.skip
@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        page = LoginPage(browser, link1)
        page.open()
        page.go_to_login_page()
        page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = LoginPage(browser, link1)
        page.open()
        page.should_be_login_link()


# @pytest.mark.skip
def test_guest_can_register_account(browser):
    page = LoginPage(browser, link3)
    page.open()
    page.register_new_user('shakokkuk25@gmail.com', "zcsqweds1SEWE32")
