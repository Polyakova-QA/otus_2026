import requests
from const import BASE_URL


URI = f"{BASE_URL}/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"
one_brewery = {
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
    r = requests.request("GET", URI)
    assert r.status_code == 200
    assert r.json() == one_brewery
    data = r.json()
    assert data["name"] == "MadTree Brewing 2.0"
    assert data["brewery_type"] == "regional"
    assert data["address_1"] == "5164 Kennedy Ave"
