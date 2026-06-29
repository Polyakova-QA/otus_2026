import requests
from const import BASE_URL


def test_get_placeholder():
    r = requests.request("GET", BASE_URL)
    assert r.status_code == 200
    assert len(r.json()) > 0
