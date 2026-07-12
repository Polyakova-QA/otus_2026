import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"
TIMEOUT = 0.1

@pytest.mark.parametrize(
    ("id_user"),
    [
        pytest.param("1", id="1"),
        pytest.param("10", id="10"),
    ],
)
def test_delete_positive(id_user):
    r = requests.delete(f"{BASE_URL}/{id_user}", timeout=TIMEOUT)
    assert r.status_code == 200


@pytest.mark.parametrize(
    ("post_id"),
    [
        pytest.param("1", id="1"),
        pytest.param("10", id="10"),
    ],
)
def test_get_comments(post_id):
    URL = "https://jsonplaceholder.typicode.com/comments"
    params = {"postId": post_id}
    r = requests.get(f"{URL}", params=params, timeout=TIMEOUT)
    assert r.status_code == 200

def test_get_placeholder():
    r = requests.request("GET", BASE_URL, timeout=TIMEOUT)
    assert r.status_code == 200
    assert len(r.json()) > 0

@pytest.mark.parametrize(
    ("number_id"),
    [
        pytest.param("1", id="1"),
        pytest.param("10", id="10"),
    ],
)
def test_param_positive(number_id):
    r = requests.get(f"{BASE_URL}/{number_id}", timeout=TIMEOUT)
    assert r.status_code == 200


@pytest.mark.parametrize(
    ("number_id"),
    [
        pytest.param("hello", id="world"),
        pytest.param("&&^&(", id="symbols"),
    ],
)
def test_param_negative(number_id):
    r = requests.get(f"{BASE_URL}/{number_id}", timeout=TIMEOUT)
    assert r.status_code == 404




