# from pages.base_page import BasePage
from pages.base_page import BasePage
from pages.locators import HeaderLocators, MainPageLocators
import random
from pages.product_page import ProductPage


class MainPage(BasePage):
    def logo(self):
        return self.find(HeaderLocators.LOGO)

    def title(self):
        return self.browser.title

    def cards(self):
        return self.find_all(MainPageLocators.PRODUCT_MINIATURES)

    def click_like(self):
        self.find(MainPageLocators.FIRST_PRODUCT_LIKE).click()

    def modal_text(self):
        return self.wait_visible(MainPageLocators.MODAL_TEXT).text

    def close_modal(self):
        self.wait_visible(MainPageLocators.MODAL_CLOSE).click()

    def cards_on_sale(self):
        return self.find_all(MainPageLocators.PRODUCTS_ON_SALE)

    def click_all_new_products(self):
        current_url = self.browser.current_url
        self.find(MainPageLocators.ALL_NEW_PRODUCTS_LINK).click()
        self.wait_url_changes(current_url)
        return self

    def open_random_product(self):
        products = self.find_all(MainPageLocators.PRODUCT_MINIATURES)
        random.choice(products).click()
        return ProductPage(self.browser, self.base_url)
