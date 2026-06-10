from src.figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius: int | float):
        if radius <= 0:
            raise ValueError(f'Не верные данные, "radius": {radius}')
        self.radius = radius

    @property
    def perimeter(self):
        perimeter = 2 * pi * self.radius
        return perimeter

    @property
    def area(self):
        area = pi * self.radius**2
        return area
