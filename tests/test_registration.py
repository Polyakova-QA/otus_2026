import allure
from faker import Faker

from pages.registration_page import Registration


@allure.feature("Регистрация")
@allure.title("Валидация формы регистрации")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("regression", "registration", "positive")
def test_registration(browser):
    page = Registration(browser)
    page.open()
    with allure.step("Проверка: заголовок страницы отображается"):
        assert page.title().is_displayed()
    page.input_password("123")
    with allure.step("Проверка: значение поля пароля"):
        assert page.password_value() == "123"
    with allure.step("Проверка: подсказки о требованиях к паролю"):
        assert (
            "Enter a password between 8 and 72 characters"
            in page.password_length_hint()
        )
        assert "The minimum score must be: Strong" in page.password_score_hint()
    page.click_save()
    with allure.step("Проверка: сообщение валидации обязательного поля"):
        assert (
            page.firstname_field().get_attribute("validationMessage")
            == "Заполните это поле."
        )
    page.send_first_name(Faker().first_name())
    page.send_last_name(Faker().last_name())
    page.input_password(Faker().password())
    page.send_email(Faker().email())
    page.click_check_agree()
    page.click_check_privacy()
    page.click_save()
    with allure.step("Проверка: кнопка выхода отображается"):
        assert page.logout_button().is_displayed()
