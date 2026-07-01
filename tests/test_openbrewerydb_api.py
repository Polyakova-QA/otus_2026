import requests
import pytest

BASE_URL = "https://api.openbrewerydb.org/v1/breweries"
TIMEOUT = 3
ONE_BREWERY = {
    "id": "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0",
    "name": "MadTree Brewing 2.0",
    "brewery_type": "regional",
    "address_1": "5164 Kennedy Ave",
    "address_2": None,
    "address_3": None,
    "city": "Cincinnati",
    "state_province": "Ohio",
    "postal_code": "45213",
    "country": "United States",
    "longitude": -84.4137736,
    "latitude": 39.1885752,
    "phone": "5138368733",
    "website_url": "http://www.madtreebrewing.com",
    "state": "Ohio",
    "street": "5164 Kennedy Ave",
}


def test_get_brewery():
    URI = f"{BASE_URL}/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"
    r = requests.request("GET", URI, timeout=TIMEOUT)
    assert r.status_code == 200
    assert r.json() == ONE_BREWERY
    data = r.json()
    assert data["name"] == "MadTree Brewing 2.0"
    assert data["brewery_type"] == "regional"
    assert data["address_1"] == "5164 Kennedy Ave"


@pytest.mark.parametrize(
    ("obdb_id"),
    [
        pytest.param("aa7cbe9b-3a0f-4888-9884-6186b0042b55", id="Belgium"),
        pytest.param("ae7b3174-8be8-4d53-a3a5-9b8240970eea", id="Germany"),
        pytest.param("9c5a66c8-cc13-416f-a5d9-0a769c87d318", id="United States"),
    ],
)
def test_get_brewery_param(obdb_id):
    r = requests.request("GET", f"{BASE_URL}/{obdb_id}", timeout=TIMEOUT)
    assert r.status_code == 200


@pytest.mark.parametrize(
    ("none_id"),
    [pytest.param("germany", id="World"), pytest.param("123", id="Numbers")],
)
def test_get_param_negativ(none_id):
    r = requests.request("GET", f"{BASE_URL}/{none_id}", timeout=TIMEOUT)
    assert r.status_code == 404


def test_list_brewery():
    r = requests.request("GET", f"{BASE_URL}", timeout=TIMEOUT)
    assert r.status_code == 200
    assert len(r.json()) > 3


def test_random_brewery():
    URL = f"{BASE_URL}/random"
    r = requests.request("GET", URL, timeout=TIMEOUT)
    assert r.status_code == 200
    assert r.json() is not None
    assert isinstance(r.json()[0]["name"], str)
