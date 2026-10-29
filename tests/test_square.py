import pytest
from src.square import Square


@pytest.mark.positive
def test_square_area_positive():
    s = Square(5)
    assert s.area == 25, f"Некорректная площадь квадрата"


@pytest.mark.negative
def test_square_area_negative():
    with pytest.raises(ValueError):
        s = Square(-5)
