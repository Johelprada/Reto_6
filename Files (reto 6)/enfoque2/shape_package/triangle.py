from .shape import Shape

# Clase base para triángulos
class Triangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)

    def compute_area(self):
        a, b, c = [edge.get_length() for edge in self._edges]
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f"  Lados: {a:.2f}, {b:.2f}, {c:.2f}")
        print(f"  Semiperímetro: {s:.2f}")
        print(f"  Área: {area:.2f}")
        return area


class Equilateral(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._is_regular = True


class Isosceles(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)


class Scalene(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)


class TriRectangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)