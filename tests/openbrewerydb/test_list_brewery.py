import requests
from const import BASE_URL


def test_list_brewery():
    r = requests.request("GET", f"{BASE_URL}")
    assert r.status_code == 200
    assert len(r.json()) > 3
