from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):          # Проверка, что текущая Url - Url страницы логина
        assert "login" in self.browser.current_url, f"Current url {self.browser.current_url} doesnt contains 'login' in it!"

    def should_be_login_form(self):         # Проверка на присутствии на странице формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form on page not found!"

    def should_be_register_form(self):      # Проверка на присутствии на странице формы регистрациии
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form on page not found!"