import pytest
from src.rectangle import Rectangle


@pytest.mark.positive
@pytest.mark.parametrize(
    ("width", "height", "area"),
    [
        pytest.param(6, 8, 48, id="integer"),
        pytest.param(7.5, 13.25, 99.375, id="float"),
    ],
)
def test_rectangle(width, height, area):
    r = Rectangle(width, height)
    assert r.area == area
