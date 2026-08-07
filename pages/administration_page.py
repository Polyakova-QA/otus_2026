from pages.administration_products_page import AdministrationProductPage
from pages.base_page import BasePage
from pages.locators import AdministrationLocators


class Administration(BasePage):
    PATH = "administration"

    def email(self):
        return self.find(AdministrationLocators.EMAIL_LABEL).text

    def password(self):
        return self.find(AdministrationLocators.PASSWORD_LABEL).text

    def submit(self):
        self.click(AdministrationLocators.SUBMIT)
        return self

    def required_error(self):
        return self.find(AdministrationLocators.EMAIL_ERROR)

    def check_stay_logged_in(self):
        checkbox = self.find(AdministrationLocators.STAY_LOGGED_IN)
        checkbox.click()
        return checkbox.is_selected()

    def open_forgot_password(self):
        self.click(AdministrationLocators.FORGOT_PASSWORD_LINK)
        self.wait_visible(AdministrationLocators.RESET_PASSWORD_BTN)
        return self

    def reset_password(self, email):
        self.find(AdministrationLocators.EMAIL_FORGOT).send_keys(email)
        self.click(AdministrationLocators.RESET_PASSWORD_BTN)
        return self.wait_visible(AdministrationLocators.RESET_ERROR).text


    def email_send(self, email):
        self.find(AdministrationLocators.EMAIL_INPUT).send_keys(email)
        return self


    def password_send(self, password):
        self.find(AdministrationLocators.PASSWORD_INPUT).send_keys(password)
        return self

    def dashboard_header(self):
        return self.wait_visible(AdministrationLocators.DASHBOARD_HEADER)

    def open_products(self):
        self.click(AdministrationLocators.OPEN_DASHBOARD)
        self.click(AdministrationLocators.CATALOG)
        self.wait_visible(AdministrationLocators.PRODUCTS).click()
        return AdministrationProductPage(self.browser)
