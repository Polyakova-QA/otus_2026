import requests
import pytest


BASE_URL = "https://dog.ceo/api"
TIMEOUT = 5

def test_random_image():
    URL = f"{BASE_URL}/breeds/image/random"
    r = requests.get(URL, timeout=TIMEOUT)
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "success"
    assert data["message"] is not None


def test_get_all_breeds():
    URL = f"{BASE_URL}/breeds/list/all"
    r = requests.get(URL, timeout=TIMEOUT)
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "success"
    assert "akita" in data["message"]


def test_get_sub_breeds():
    URL = f"{BASE_URL}/breed/hound/list"
    r = requests.get(URL, timeout=TIMEOUT)
    assert r.status_code == 200


@pytest.mark.parametrize(
    ("name_breed"),
    [
        pytest.param("akita", id="Akita"),
        pytest.param("borzoi", id="Borzoi"),
        pytest.param("boxer", id="Boxer"),
    ],
)
def test_image_random(name_breed):
    URL = f"{BASE_URL}/breed"
    r = requests.get(f"{URL}/{name_breed}/images/random", timeout=TIMEOUT)
    assert r.status_code == 200


@pytest.mark.parametrize(
    ("name_breed_negative"),
    [
        pytest.param("123", id="Numbers"),
        pytest.param("злой", id="Russian"),
        pytest.param("Chov", id="Error"),
    ],
)
def test_image_random_negative(name_breed_negative):
    URL = f"{BASE_URL}/breed"
    r = requests.get(f"{URL}/{name_breed_negative}/images/random", timeout=TIMEOUT)
    assert r.status_code == 404
    assert r.json()["status"] == "error"
    assert r.json()["message"] == "Breed not found (main breed does not exist)"

