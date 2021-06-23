from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage

class MainPage(BasePage):
    def should_be_basket_button(self):
        assert self.is_element_present(*MainPageLocators.BASKET_FROM_MAIN), \
            f"Busket button not found at {self.browser.current_url} url!"

    def get_basket_from_main_button(self):
        busket_button = self.browser.find_element(*MainPageLocators.BASKET_FROM_MAIN)
        return busket_button

    def get_basket_from_main_button_text(self):
        busket_button = self.browser.find_element(*MainPageLocators.BASKET_FROM_MAIN).text
        return busket_button

    def open_basket_from_main(self):
        self.should_be_basket_button()
        button = self.get_busket_from_main_button()
        button.click()


