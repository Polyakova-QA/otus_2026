import allure

from pages.base_page import BasePage
from pages.locators import ProductPageLocators, HeaderLocators
from pages.cart_page import CartPage


class ProductPage(BasePage):
    @allure.step("Добавить товар в корзину")
    def add_to_cart(self):
        self.click(ProductPageLocators.ADD_TO_CART)
        return self.wait_visible(ProductPageLocators.ADDED_MODAL_LABEL).text

    @allure.step("Закрыть модальное окно добавления")
    def close_modal(self):
        self.click(ProductPageLocators.ADDED_MODAL_CLOSE)
        return self

    @allure.step("Открыть корзину")
    def open_cart(self):
        self.click(HeaderLocators.CART_LINK)
        return CartPage(self.browser)
