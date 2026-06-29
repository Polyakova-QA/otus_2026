import requests
from const import BASE_URL

URL = f"{BASE_URL}/breeds/image/random"


def test_random_image():
    r = requests.get(URL)
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "success"
    assert data["message"] is not None
