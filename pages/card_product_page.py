from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class CardPage(BasePage):
    PATH = "women/2-9-brown-bear-printed-sweater.html#/1-size-s"

    def have_description(self):
        return self.wait_visible(ProductPageLocators.DESCRIPTION).text

    def product_details(self):
        self.find(ProductPageLocators.PRODUCT_DETAILS).click()
        return self.wait_visible(ProductPageLocators.DATA_SHEET).text

    def click_picture(self):
        self.find(ProductPageLocators.PRODUCT_PICTURE).click()
        return self.wait_visible(ProductPageLocators.PRODUCT_MODAL_IMG)
