import requests
from const import BASE_URL

URL = f"{BASE_URL}/breeds/list/all"


def test_get():
    r = requests.get(URL)
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "success"
    assert "akita" in data["message"]
