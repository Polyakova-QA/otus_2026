import pytest
from src.triangle import Triangle


def test_triangle(start_bd):
    t = Triangle(4, 4, 4)
    assert round(t.area, 3) == 6.928, f"Площадь квадрата не верна ({round(t.area, 3)})"
