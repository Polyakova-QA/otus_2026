import pytest
import requests
from const import BASE_URL

URL = f"{BASE_URL}/breed"


@pytest.mark.parametrize(
    ("name_breed"),
    [
        pytest.param("akita", id="Akita"),
        pytest.param("borzoi", id="Borzoi"),
        pytest.param("boxer", id="Boxer"),
    ],
)
def test_image_random(name_breed):
    r = requests.get(f"{URL}/{name_breed}/images/random")
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
    r = requests.get(f"{URL}/{name_breed_negative}/images/random")
    assert r.status_code == 404
    assert r.json()["status"] == "error"
    assert r.json()["message"] == "Breed not found (main breed does not exist)"
