from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasePageLocators
import math
import time


links = []

class BasePage():
    # Конструктор
    def __init__(self, browser, url, timeout=7):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Метод открывает нужную страницу в браузере
    def open(self):
        self.browser.get(self.url)

    # Метод перехвата исключения существования элемента
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Метод проверки, что элемент не появляется на странице
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # Метод проверки что элемент исчезает со временем
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # Метод получения кода из аллерта, посчитав пример
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # Метод перехода по ссылке на страницу логина
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        """
        alert = self.browser.switch_to.alert
        alert.accept()
        return LoginPage(browser=self.browser, url=self.browser.current_url)
        """

    # Метод проверки, что есть ссылка перехода на логин страницу
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), f"Login link at {self.browser.current_url} is not presented!"

    # Получение кнопки корзины
    def get_basket_button(self):
            busket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
            return busket_button

    # Получение текста кнопки корзины
    def get_basket_button_text(self):
        busket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON).text
        return busket_button

    # Проверка что на данной странице есть кнопка корзины
    def should_be_basket_button(self):
        assert self.is_element_present(*BasePageLocators.BASKET_BUTTON), \
            f"Busket button not found at {self.browser.current_url} url!"

    # Открытие корзины
    def open_basket(self):
        self.should_be_basket_button()
        basket_button = self.get_basket_button()
        basket_button.click()

    # Проверка что корзина пуста
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasePageLocators.ITEMS_IN_BASKET), \
            f"Busket isnt empty, but it sohuld be!"

    # Проверка что есть сообещние о пустой корзине
    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BUSKET_MESSAGE), \
            f"Empty busket message not found!"

    # Проверка по иконке что пользователь зарегестрирован
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user!"

