import time

from pages.product_page import ProductPage
link1 = "http://selenium1py.pythonanywhere.com/"                                                        # Main page link
link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"  # 209 book link
link3 = "http://selenium1py.pythonanywhere.com/accounts/login/"                                         # Login page
link4 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"   # 209 book link + new year promo
link5 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
# pytest -s --tb=line --language=en test_product_page.py для пазла
# pytest -v --tb=line --language=en test_product_page.py


def test_user_can_solve_quiz_and_get_code(browser):
    page = ProductPage(browser, link4)
    page.open()
    page.adding_to_basket_from_product_page()
    page.solve_quiz_and_get_code()



def test_user_should_see_correct_message_about_adding_product_to_basket(browser):
    page = ProductPage(browser, link5)
    page.open()
    page.adding_to_basket_from_product_page()
    page.adding_to_basket_message_should_contain_product_name()