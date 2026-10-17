import allure
import pytest
import requests

URLS = [
    pytest.param(
        "https://dog.ceo/api/breeds/image/random",
        id="dog_api",
    ),
    pytest.param(
        "https://jsonplaceholder.typicode.com/posts",
        id="jsonplaceholder",
    ),
    pytest.param(
        "https://api.openbrewerydb.org/v1/breweries",
        id="openbrewerydb",
    ),
]


@allure.feature("API")
@allure.title("Проверка статус-кода публичных API")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("api", "regression")
@pytest.mark.parametrize("url", URLS)
def test_url_status_code(url):
    r = requests.get(url)
    with allure.step("Проверка: статус-код равен 200"):
        assert r.status_code == 200
