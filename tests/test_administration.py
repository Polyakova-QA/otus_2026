import allure

from pages.administration_page import Administration


@allure.feature("Админка")
@allure.title("Валидация формы входа в админку")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("regression", "admin", "negative")
def test_administration(browser):
    page: Administration = Administration(browser).open()
    with allure.step("Проверка: подписи полей email и пароль"):
        assert "Email address" in page.email()
        assert "Password" in page.password()

    page.submit()
    error = page.required_error()
    with allure.step("Проверка: ошибка обязательного поля"):
        assert error.get_attribute("class") == "help-block"
        assert "This field is required." in error.text

    with allure.step("Проверка: чекбокс «оставаться в системе» включается"):
        assert page.check_stay_logged_in()

    page.open_forgot_password()
    text_error = (
        "You can reset your password every 360 minute(s) only. Please try again later."
    )
    with allure.step("Проверка: сообщение о лимите восстановления пароля"):
        assert text_error in page.reset_password("mail@mail.com")
