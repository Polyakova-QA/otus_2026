from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("figure должна быть фигурой из класса Figure")
        sum_area = self.area + figure.area
        return sum_area
