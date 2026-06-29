import pytest
import requests
from const import BASE_URL


@pytest.mark.parametrize(
    ("obdb_id"),
    [
        pytest.param("aa7cbe9b-3a0f-4888-9884-6186b0042b55", id="Belgium"),
        pytest.param("ae7b3174-8be8-4d53-a3a5-9b8240970eea", id="Germany"),
        pytest.param("9c5a66c8-cc13-416f-a5d9-0a769c87d318", id="United States"),
    ],
)
def test_get_brewery_param(obdb_id):
    r = requests.request("GET", f"{BASE_URL}/{obdb_id}")
    assert r.status_code == 200


@pytest.mark.parametrize(
    ("none_id"),
    [pytest.param("germany", id="World"), pytest.param("123", id="Numbers")],
)
def test_get_param_negativ(none_id):
    r = requests.request("GET", f"{BASE_URL}/{none_id}")
    assert r.status_code == 404
