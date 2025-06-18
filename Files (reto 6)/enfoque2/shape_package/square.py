from .rectangle import Rectangle

# Clase cuadrado que hereda de rectángulo
class Square(Rectangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._is_regular = True