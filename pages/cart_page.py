import allure

from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    @allure.step("Получить строку товара в корзине")
    def product_row(self):
        return self.wait_visible(CartPageLocators.PRODUCT_ROW)
