from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, width: int | float, height: int | float):
        if width <= 0 or height <= 0:
            raise ValueError(f'Не верные данные, "width": {width},"height": {height}')
            raise ValueError("width and height must be positive")
        self.width = width
        self.height = height

    @property
    def perimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter

    @property
    def area(self):
        area = self.width * self.height
        return area
