import allure
from faker import Faker

from pages.base_page import BasePage
from pages.locators import ClothesCategoryLocators


class CLOTHES(BasePage):
    PATH = "3-clothes"

    @allure.step("Подписаться на рассылку")
    def subscribe_newsletter(self):
        email = Faker().email()
        self.find(ClothesCategoryLocators.NEWSLETTER_EMAIL).send_keys(email)
        self.click(ClothesCategoryLocators.NEWSLETTER_SUBMIT)
        return self.wait_visible(ClothesCategoryLocators.NEWSLETTER_MODAL).text

    @allure.step("Повторно подписаться на рассылку")
    def subscribe_again(self):
        self.click(ClothesCategoryLocators.NEWSLETTER_SUBMIT)
        return self.wait_visible(ClothesCategoryLocators.NEWSLETTER_MODAL).text

    @allure.step("Получить футер")
    def footer(self):
        return self.find(ClothesCategoryLocators.FOOTER)

    @allure.step("Получить заголовок подкатегорий")
    def subcategories_title(self):
        return self.find(ClothesCategoryLocators.SUBCATEGORIES_TITLE)

    @allure.step("Получить текст блока брендов")
    def brands_text(self):
        return self.find(ClothesCategoryLocators.BRANDS_SECTION).text

    @allure.step("Отфильтровать по чёрному цвету")
    def filter_by_black(self):
        self.click(ClothesCategoryLocators.FILTER_BLACK)
        return self.wait_visible(ClothesCategoryLocators.ACTIVE_FILTER).text
