import allure

from pages.base_page import BasePage
from pages.locators import LoginLocators


class LoginPage(BasePage):
    PATH = "login"

    @allure.step("Авторизоваться")
    def login(self, email, password):
        self.find(LoginLocators.EMAIL).send_keys(email)
        self.find(LoginLocators.PASSWORD).send_keys(password)
        self.click(LoginLocators.SUBMIT)
        return self
