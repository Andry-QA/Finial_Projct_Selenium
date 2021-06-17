from selenium.common.exceptions import NoSuchElementException


class BasePage():
    # Конструктор
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Метлод открывает нужную страницу в браузере
    def open(self):
        self.browser.get(self.url)

    # Метод перехвата исключения существования элемента
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True