from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage

class MainPage(BasePage):
    # Возвращет кнопку корзины (объект вебдрайвера)
    def get_basket_from_main_button(self):
        busket_button = self.browser.find_element(*MainPageLocators.BASKET_FROM_MAIN)
        return busket_button

    # Возвращает текст с кнопки карзины
    def get_basket_from_main_button_text(self):
        busket_button = self.browser.find_element(*MainPageLocators.BASKET_FROM_MAIN).text
        return busket_button

    # Открывает карзину с главной вкладки
    def open_basket_from_main(self):
        self.should_be_basket_button()
        button = self.get_busket_from_main_button()
        button.click()


