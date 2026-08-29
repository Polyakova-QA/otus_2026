import allure
import pytest


@allure.feature("Валюта")
@allure.title("Смена валюты в каталоге")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("regression", "currency")
@pytest.mark.parametrize("currency", ["9-art"], indirect=True)
def test_currency_catalog(browser, currency):
    with allure.step("Проверка: цена в USD отличается от цены в EUR"):
        assert currency["usd"] != currency["euro"]
