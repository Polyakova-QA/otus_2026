import random

import allure

from pages.base_page import BasePage
from pages.locators import HeaderLocators, MainPageLocators
from pages.product_page import ProductPage


class MainPage(BasePage):
    @allure.step("Получить логотип")
    def logo(self):
        return self.find(HeaderLocators.LOGO)

    @allure.step("Получить заголовок вкладки")
    def title(self):
        return self.browser.title

    @allure.step("Получить карточки товаров")
    def cards(self):
        return self.find_all(MainPageLocators.PRODUCT_MINIATURES)

    @allure.step("Кликнуть по кнопке «нравится» у первого товара")
    def click_like(self):
        self.find(MainPageLocators.FIRST_PRODUCT_LIKE).click()

    @allure.step("Получить текст модального окна")
    def modal_text(self):
        return self.wait_visible(MainPageLocators.MODAL_TEXT).text

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.wait_visible(MainPageLocators.MODAL_CLOSE).click()

    @allure.step("Получить товары со скидкой")
    def cards_on_sale(self):
        return self.find_all(MainPageLocators.PRODUCTS_ON_SALE)

    @allure.step("Перейти к списку всех товаров")
    def click_all_new_products(self):
        current_url = self.browser.current_url
        self.find(MainPageLocators.ALL_NEW_PRODUCTS_LINK).click()
        self.wait_url_changes(current_url)
        return self

    @allure.step("Открыть случайный товар")
    def open_random_product(self):
        products = self.find_all(MainPageLocators.PRODUCT_MINIATURES)
        random.choice(products).click()
        return ProductPage(self.browser)
