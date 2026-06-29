import pytest
import requests
from const import BASE_URL


@pytest.mark.parametrize(
    ("id_user"),
    [
        pytest.param("1", id="1"),
        pytest.param("10", id="10"),
    ],
)
def test_delete_positive(id_user):
    r = requests.get(f"{BASE_URL}/{id_user}")
    assert r.status_code == 200
