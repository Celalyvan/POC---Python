#ABC = Abstract Base Class
from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    def __int__(self, width, height):
        if self._validate_value(height):
            self.width = width
            self.height = height
        else:
            self.width = 0
            self.height = 0


    def _validate_value(self, value):
        return True if 0 < value < 10 else False

    @abstractmethod
    def calculate_area(self):
        pass   # indica que no tiene implementacion