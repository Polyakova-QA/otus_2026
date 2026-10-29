from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, width: int | float):
        if width <= 0:
            raise ValueError(f'Не верные данные, "width": {width}')
        super().__init__(width, width)
