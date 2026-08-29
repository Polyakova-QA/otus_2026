import allure

from pages.base_page import BasePage
from pages.locators import RegistrationLocators


class Registration(BasePage):
    PATH = "registration"

    @allure.step("Получить заголовок страницы")
    def title(self):
        return self.find(RegistrationLocators.TITLE)

    @allure.step("Ввести пароль и показать его")
    def input_password(self, password):
        self.find(RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        self.find(RegistrationLocators.SHOW_PASSWORD_BTN).click()
        return self

    @allure.step("Получить значение поля пароля")
    def password_value(self):
        return self.find(RegistrationLocators.PASSWORD_INPUT).get_attribute("value")

    @allure.step("Получить подсказку о длине пароля")
    def password_length_hint(self):
        return self.find(RegistrationLocators.PASSWORD_LENGTH_HINT).get_attribute(
            "textContent"
        )

    @allure.step("Получить подсказку о надёжности пароля")
    def password_score_hint(self):
        return self.find(RegistrationLocators.PASSWORD_SCORE_HINT).get_attribute(
            "textContent"
        )

    @allure.step("Нажать «Сохранить»")
    def click_save(self):
        self.find(RegistrationLocators.SUBMIT).click()
        return self

    @allure.step("Получить поле имени")
    def firstname_field(self):
        return self.find(RegistrationLocators.FIRSTNAME)

    @allure.step("Ввести имя")
    def send_first_name(self, first_name):
        self.find(RegistrationLocators.FIRSTNAME).send_keys(first_name)

    @allure.step("Ввести фамилию")
    def send_last_name(self, last_name):
        self.find(RegistrationLocators.LASTNAME).send_keys(last_name)

    @allure.step("Отметить согласие на обработку данных")
    def click_check_agree(self):
        self.find(RegistrationLocators.CHECK_AGREE).click()
        return self

    @allure.step("Отметить согласие с политикой конфиденциальности")
    def click_check_privacy(self):
        self.find(RegistrationLocators.CHECK_PRIVACY).click()
        return self

    @allure.step("Ввести email")
    def send_email(self, email):
        self.find(RegistrationLocators.EMAIL).send_keys(email)
