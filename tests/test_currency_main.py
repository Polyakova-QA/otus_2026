import allure
import pytest


@allure.feature("Валюта")
@allure.title("Смена валюты на главной странице")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("regression", "currency")
@pytest.mark.parametrize("currency", [""], indirect=True)
def test_currency_main(browser, currency):
    with allure.step("Проверка: цена в USD отличается от цены в EUR"):
        assert currency["usd"] != currency["euro"]
