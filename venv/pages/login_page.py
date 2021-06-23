import time

from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    # Проверка, что текущая страница действительно является страницей логина
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверка, что текущая Url - Url страницы логина
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            f"Current url {self.browser.current_url} doesnt contains 'login' in it!"

    # Проверка на присутствии на странице формы логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            f"Login form on {self.browser.current_url} not found!"

    # Проверка на присутствии на странице формы регистрациии
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            f"Register form on {self.browser.current_url} not found!"

    # Проверка, что на странице есть поле ввода регистрации э-мейла
    def should_be_email_register_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_FIELD), \
            f"E-mail reigstration field on {self.browser.current_url} not found!"

    # Заполняем данными э-мейл поле регистрации
    def send_data_to_email_register_field(self,email):
        email_register_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        email_register_field.send_keys(email)

    # Проверка, что на странице есть поле ввода пароля1
    def should_be_password1_register_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1_FIELD),\
            f"Password1 field on {self.browser.current_url} not found!"

    # Заполняем поле ввода пароля1 информацией, передаваемой в password
    def send_data_to_password1_register_field(self,password):
        password1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1_FIELD)
        password1_field.send_keys(password)

    # Проверка, что на странице есть поле ввода пароля2
    def should_be_password2_register_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2_FIELD), \
                f"Password2 field on {self.browser.current_url} not found!"

    # Заполняем поле ввода пароля2 информацией, передаваемой в password
    def send_data_to_password2_register_field(self, password):
        password1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2_FIELD)
        password1_field.send_keys(password)

    # Проверка, что на странице есть кнопка регистрации
    def should_be_registration_button(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), \
                f"Registration button on {self.browser.current_url} not found!"

    # Нажатие кнопки регистрации
    def register_button_click(self):
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        register_button.click()

    # Регистрация нового пользователя с имейлом email и паролем password
    def register_new_user(self,email,password):
        self.should_be_email_register_field()
        self.should_be_password1_register_field()
        self.should_be_password2_register_field()
        self.should_be_registration_button()
        self.send_data_to_email_register_field(email)
        self.send_data_to_password1_register_field(password)
        self.send_data_to_password2_register_field(password)
        self.register_button_click()
