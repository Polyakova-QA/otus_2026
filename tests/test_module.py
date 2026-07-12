import requests


def test_get_addoption(url, status_code):
    r = requests.get(url)
    assert r.status_code == status_code
