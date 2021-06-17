from pages.main_page import MainPage
link1 = "http://selenium1py.pythonanywhere.com/"                                                        # MainPageLink
link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"  # 209 book link


# pytest -v --tb=line --language=en test_main_page.py
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link1)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу
    page.go_to_login_page()         # выполняем метод страницы — переходим на страницу логина


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link1)
    page.open()
    page.should_be_login_link()
