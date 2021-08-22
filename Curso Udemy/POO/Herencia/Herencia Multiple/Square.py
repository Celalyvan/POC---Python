from GeometricFigure import GeometricFigure  # from <file> import <class> as <New class name>
from Color import Color


class Square(GeometricFigure, Color):
    def __init__(self, side, color):
        GeometricFigure.__int__(self, side, side)
        Color.__init__(self, color)

    def calculate_area(self):
        return self.height * self.width


