import pytest
from src.circle import Circle


@pytest.mark.positive
def test_circle_perimeter():
    c = Circle(5)
    assert round(c.perimeter, 3) == 31.416, f"Периметр круга не верен ({round(c.perimeter, 3)})"
