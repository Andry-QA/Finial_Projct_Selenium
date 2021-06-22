from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_FROM_MAIN = (By.CSS_SELECTOR, "span a.btn")
    ITEMS_IN_BUSKET = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_BUSKET_MESSAGE = (By.CSS_SELECTOR, "div #content_inner  >p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON_PODUCT_PAGE = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESSFUL_ADDING_PRODUCT_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR,"div.alertinner p")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    CHANGED_PRICE_BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "div.alertinner p strong")