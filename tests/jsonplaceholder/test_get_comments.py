import pytest
import requests

URL = "https://jsonplaceholder.typicode.com/comments"


@pytest.mark.parametrize(
    ("post_id"),
    [
        pytest.param("1", id="1"),
        pytest.param("10", id="10"),
    ],
)
def test_get_comments(post_id):
    params = {"postId": post_id}
    r = requests.get(f"{URL}", params=params)
    assert r.status_code == 200
