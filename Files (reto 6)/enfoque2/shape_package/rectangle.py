from .shape import Shape

# Clase para representar un rectángulo
class Rectangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._is_regular = False

    def compute_area(self):
        l1 = self._edges[0].get_length()
        l2 = self._edges[1].get_length()
        area = l1 * l2
        print(f"  Área = {l1:.2f} x {l2:.2f} = {area:.2f}")
        return area
    