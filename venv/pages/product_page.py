from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage

class ProductPage(BasePage):

    # Нажатие на кнопку 'Add to basket' на странице товара
    def adding_to_basket_from_product_page(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON_PODUCT_PAGE)
        add_button.click()

    # Проверка наличия сообщения о успешном добавлении товара в корзину
    def should_be_adding_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESSFUL_ADDING_PRODUCT_MESSAGE), \
            f"Message about adding product({self.browser.current_url}) to basket not found!"

    # Проверка наличия названия товара на его странице
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            f"Product name not found at {self.browser.current_url} url!"

    # Получаем имя продукта
    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    # Получаем цену продукта
    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    # Получаем текст сообщения о добавлении товара в корзину
    def get_adding_message(self):
        adding_message = self.browser.find_element(*ProductPageLocators.SUCCESSFUL_ADDING_PRODUCT_MESSAGE).text
        return adding_message

    # Получаем общую стоимость корзины в сообщении о изменении цены корзины
    def get_changed_total_basket(self):
        total_basket = self.browser.find_element(*ProductPageLocators.CHANGED_PRICE_BASKET_PRICE_MESSAGE).text
        return total_basket

    # Проверка наличия названия товара в сообщении о успешном добавлении
    def adding_to_basket_message_should_contain_product_name(self):
        self.should_be_product_name()
        self.should_be_adding_to_basket_message()
        assert self.get_product_name() in self.get_adding_message(), \
            f"Message about adding product({self.browser.current_url}) to basket doesn't contains '{self.get_product_name()}' in it!"

    # Проверка наличия сообщения об изменении цены корзины
    def should_be_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), \
            f"Message about changing price of basket at {self.browser.current_url} not found!"

    # Проверка наличия новой общей стоимости карзины в сообщении об изменении цены корзины
    def should_be_basket_changed_price(self):
        assert self.is_element_present(*ProductPageLocators.CHANGED_PRICE_BASKET_PRICE_MESSAGE), \
            f"Changed total price of basket at message on {self.browser.current_url} not found!"

    # Проверка наличия цены продукта на его странице
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            f"Product({self.browser.current_url}) price not found!"

    # Проверка, что новая общая цена корзины, после добавления товара, соответствует его цене (только если до этого в корзине не было товаров)
    def changing_basket_total_price_after_adding_product(self):
        self.should_be_product_price()
        self.should_be_basket_price_message()
        self.should_be_basket_changed_price()
        assert self.get_changed_total_basket() == self.get_product_price(), \
            f"Total basket price --{self.get_changed_total_basket()}-- doesn't equals price of added product --{self.get_product_price()}-- !"

    # Проверка, что сообщение о успешном добавлении товара не появляется
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFUL_ADDING_PRODUCT_MESSAGE), \
            F"Success message is presented at {self.browser.current_url}, but should not be!"

    # Проверка, что сообщение о успешном добавлении товара постепенно исчезает
    def success_message_should_disapeare(self, timer):
        assert self.is_disappeared(*ProductPageLocators.SUCCESSFUL_ADDING_PRODUCT_MESSAGE, timeout=timer), \
            F"Success message at {self.browser.current_url} doesn't desapear after --{timer}-- seconds!"
