from faker import Faker
from pages.base_page import BasePage
from pages.locators import ClothesCategoryLocators


class CLOTHES(BasePage):
    PATH = "3-clothes"

    def subscribe_newsletter(self):
        email = Faker().email()
        self.find(ClothesCategoryLocators.NEWSLETTER_EMAIL).send_keys(email)
        self.click(ClothesCategoryLocators.NEWSLETTER_SUBMIT)
        return self.wait_visible(ClothesCategoryLocators.NEWSLETTER_MODAL).text

    def subscribe_again(self):
        self.click(ClothesCategoryLocators.NEWSLETTER_SUBMIT)
        return self.wait_visible(ClothesCategoryLocators.NEWSLETTER_MODAL).text

    def footer(self):
        return self.find(ClothesCategoryLocators.FOOTER)

    def subcategories_title(self):
        return self.find(ClothesCategoryLocators.SUBCATEGORIES_TITLE)

    def brands_text(self):
        return self.find(ClothesCategoryLocators.BRANDS_SECTION).text

    def filter_by_black(self):
        self.click(ClothesCategoryLocators.FILTER_BLACK)
        return self.wait_visible(ClothesCategoryLocators.ACTIVE_FILTER).text
