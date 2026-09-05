import allure

from pages.administration_products_page import AdministrationProductPage
from pages.base_page import BasePage
from pages.locators import AdministrationLocators


class Administration(BasePage):
    PATH = "administration"

    @allure.step("Получить подпись поля email")
    def email(self):
        return self.find(AdministrationLocators.EMAIL_LABEL).text

    @allure.step("Получить подпись поля пароля")
    def password(self):
        return self.find(AdministrationLocators.PASSWORD_LABEL).text

    @allure.step("Нажать «Войти»")
    def submit(self):
        self.click(AdministrationLocators.SUBMIT)
        return self

    @allure.step("Получить ошибку обязательного поля")
    def required_error(self):
        return self.find(AdministrationLocators.EMAIL_ERROR)

    @allure.step("Отметить «оставаться в системе»")
    def check_stay_logged_in(self):
        checkbox = self.find(AdministrationLocators.STAY_LOGGED_IN)
        checkbox.click()
        return checkbox.is_selected()

    @allure.step("Открыть восстановление пароля")
    def open_forgot_password(self):
        self.click(AdministrationLocators.FORGOT_PASSWORD_LINK)
        self.wait_visible(AdministrationLocators.RESET_PASSWORD_BTN)
        return self

    @allure.step("Восстановить пароль по email")
    def reset_password(self, email):
        self.find(AdministrationLocators.EMAIL_FORGOT).send_keys(email)
        self.click(AdministrationLocators.RESET_PASSWORD_BTN)
        return self.wait_visible(AdministrationLocators.RESET_ERROR).text

    @allure.step("Ввести email администратора")
    def email_send(self, email):
        self.find(AdministrationLocators.EMAIL_INPUT).send_keys(email)
        return self

    @allure.step("Ввести пароль администратора")
    def password_send(self, password):
        self.find(AdministrationLocators.PASSWORD_INPUT).send_keys(password)
        return self

    @allure.step("Получить заголовок дашборда")
    def dashboard_header(self):
        return self.wait_visible(AdministrationLocators.DASHBOARD_HEADER)

    @allure.step("Перейти в раздел товаров")
    def open_products(self):
        self.click(AdministrationLocators.OPEN_DASHBOARD)
        self.click(AdministrationLocators.CATALOG)
        self.wait_visible(AdministrationLocators.PRODUCTS).click()
        return AdministrationProductPage(self.browser)
