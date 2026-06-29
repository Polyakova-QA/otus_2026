import pytest
import requests
from const import BASE_URL


@pytest.mark.parametrize(
    ("number_id"),
    [
        pytest.param("1", id="1"),
        pytest.param("10", id="10"),
    ],
)
def test_param_positive(number_id):
    r = requests.get(f"{BASE_URL}/{number_id}")
    assert r.status_code == 200


@pytest.mark.parametrize(
    ("number_id"),
    [
        pytest.param("hello", id="world"),
        pytest.param("&&^&(", id="symbols"),
    ],
)
def test_param_negative(number_id):
    r = requests.get(f"{BASE_URL}/{number_id}")
    assert r.status_code == 404
