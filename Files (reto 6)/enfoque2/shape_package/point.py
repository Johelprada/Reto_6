# Clase para representar un punto en el plano
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def compute_distance(self, other):
        return ((self._x - other._x) ** 2 + (self._y - other._y) ** 2) ** 0.5

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y