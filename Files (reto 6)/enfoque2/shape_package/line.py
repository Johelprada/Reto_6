from .point import Point

# Clase para representar una línea entre dos puntos
class Line:
    def __init__(self, start_point, end_point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self._start_point.compute_distance(self._end_point)

    def get_start_point(self):
        return self._start_point

    def get_end_point(self):
        return self._end_point

    def get_length(self):
        return self._length

    def set_start_point(self, p):
        self._start_point = p
        self._length = self._start_point.compute_distance(self._end_point)

    def set_end_point(self, p):
        self._end_point = p
        self._length = self._start_point.compute_distance(self._end_point)