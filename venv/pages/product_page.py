from pages.base_page import BasePage
from pages.locators import ProductPageLocators

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

    # Проверка наличия названия товара в сообщении о успешном добавлении
    def adding_to_basket_message_should_contain_product_name(self):
        self.should_be_product_name()
        self.should_be_adding_to_basket_message()
        adding_message = self.browser.find_element(*ProductPageLocators.SUCCESSFUL_ADDING_PRODUCT_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name in adding_message, \
            f"Message about adding product({self.browser.current_url}) to basket doesn't contains '{product_name}' in it!"

    # Проверка наличия сообщения об изменении цены корзины
    def should_be_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), \
            f"Message about changing price of basket at {self.browser.current_url} not found!"

    # Проверка наличия новой общей стоимости карзины в сообщении об изменении цены корзины
    def should_be_basket_changed_price(self):
        assert self.is_element_present(*ProductPageLocators.CHANGED_PRICE_BASKET_PRICE_MESSAGE), \
            f"Changed total price of basket at message on {self.browser.current_url} not found!"

    # Проверка, что новая общая цена корзины, после добавления товара, соответствует его цене (только если до этого в корзине не было товаров)
    def changing_basket_total_price_after_adding_product(self):
        self.should_be_basket_price_message()
        self.should_be_basket_changed_price()
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        total_basket = self.browser.find_element(*ProductPageLocators.CHANGED_PRICE_BASKET_PRICE_MESSAGE).text
        assert total_basket == product_price, \
            f"Total basket price --{total_basket}-- doesn't equals price of added product --{product_price}-- !"
