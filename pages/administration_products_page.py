from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import AdministrationPageLocatorsProducts


class AdministrationProductPage(BasePage):
    PATH = "administration"

    def new_product(self):
        self.click(AdministrationPageLocatorsProducts.NEW_PRODUCT)
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe"))
        )
        return self

    def new_standart_product(self):
        self.wait_visible(AdministrationPageLocatorsProducts.STANDART_PRODUCT).click()
        return self

    def add_new_product(self):
        self.wait_visible(AdministrationPageLocatorsProducts.ADD_PRODUCT).click()
        return self

    def fill_product(self, name):
        self.browser.switch_to.default_content()
        wait = WebDriverWait(self.browser, 15)
        wait.until(
            EC.visibility_of_element_located(AdministrationPageLocatorsProducts.PRODUCT_NAME)
        ).send_keys(name)
        wait.until(
            EC.element_to_be_clickable(AdministrationPageLocatorsProducts.SAVE)
        ).click()
        return self

    def success_message(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located(
                AdministrationPageLocatorsProducts.SUCCESS_MESSAGE
            )
        ).text

    def open_delete_modal(self):
        # JS-клик напрямую по кнопке удаления — в обход выпадающего меню и
        # панели отладки Symfony, которая перехватывает обычный клик
        self.js_click(AdministrationPageLocatorsProducts.DELETE_PRODUCT)
        return self

    def confirm_delete(self):
        self.wait_visible(AdministrationPageLocatorsProducts.CONFIRM_DELETE).click()
        return self
