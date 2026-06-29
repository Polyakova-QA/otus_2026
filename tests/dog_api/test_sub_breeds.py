import requests
from const import BASE_URL

URL = f"{BASE_URL}/breed/hound/list"


def test_get():
    r = requests.get(URL)
    assert r.status_code == 200
