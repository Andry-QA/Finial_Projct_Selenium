from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):

    # Нажатие на кнопку 'Add to basket' на странице товара
    def adding_to_basket_from_product_page(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON_PODUCT_PAGE)
        add_button.click()

    # Проверка наличия сообщения о успешном добавлении товара в корзину
    def should_be_message_about_adding_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESSFUL_ADDING_PRODUCT_MESSAGE), \
            f"Message about adding product({self.browser.current_url}) to basket not found!"

    # Проверка наличия названия товара на его странице
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            f"Product name not found at {self.browser.current_url} url!"

    # Проверка наличия названия товара в сообщении о успешном добавлении
    def adding_to_basket_message_should_contain_product_name(self):
        self.should_be_product_name()
        self.should_be_message_about_adding_to_basket()
        adding_message = self.browser.find_element(*ProductPageLocators.SUCCESSFUL_ADDING_PRODUCT_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name not in adding_message, \
            f"Message about adding product({self.browser.current_url}) to basket doesn't contains '{product_name}' in it!"