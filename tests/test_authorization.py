import os

import allure

from pages.login_page import LoginPage


@allure.feature("Авторизация")
@allure.title("Вход и выход из аккаунта")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "authorization", "positive")
def test_authorization(browser):
    page = LoginPage(browser).open()
    page.login("mail@mail.com", os.getenv("TEST_PASSWORD"))
    with allure.step("Проверка: имя пользователя в шапке"):
        assert page.account_name() == "Nadezhda P."
    with allure.step("Проверка: после выхода отображается «Sign in»"):
        assert page.logout() == "Sign in"
