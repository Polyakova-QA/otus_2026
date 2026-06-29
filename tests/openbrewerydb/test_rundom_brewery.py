import requests
from const import BASE_URL

URL = f"{BASE_URL}/random"


def test_rundom_brewery():
    r = requests.request("GET", URL)
    assert r.status_code == 200
    assert r.json() is not None
    assert isinstance(r.json()[0]["name"], str)
