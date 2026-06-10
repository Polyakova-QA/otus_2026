from src.figure import Figure


class Triangle(Figure):
    def __init__(self, a: int | float, b: int | float, c: int | float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError(f'Не верные данные, "a": {a},"b": {b},"c": {c}')
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError(f"Стороны {a}, {b}, {c} не образуют треугольник")
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter

    @property
    def area(self):
        p = self.perimeter / 2
        area = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return area
