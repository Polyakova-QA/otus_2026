from pages.base_page import BasePage
from pages.locators import ProductPageLocators, HeaderLocators
from pages.cart_page import CartPage


class ProductPage(BasePage):
    def add_to_cart(self):
        self.click(ProductPageLocators.ADD_TO_CART)
        return self.wait_visible(ProductPageLocators.ADDED_MODAL_LABEL).text

    def close_modal(self):
        self.click(ProductPageLocators.ADDED_MODAL_CLOSE)
        return self

    def open_cart(self):
        self.click(HeaderLocators.CART_LINK)
        return CartPage(self.browser, self.base_url)
