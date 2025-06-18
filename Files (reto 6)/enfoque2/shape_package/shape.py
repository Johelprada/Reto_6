from .line import Line

# Clase base para cualquier figura
class Shape:
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = self._compute_edges()
        self._inner_angles = []
        self._is_regular = False

    def _compute_edges(self):
        print("\nlíneas que forman la figura:")
        edges = []
        for i in range(len(self._vertices)):
            start = self._vertices[i]
            end = self._vertices[(i + 1) % len(self._vertices)]
            line = Line(start, end)
            print(f"  Lado {i+1} de longitud {line.get_length():.2f}")
            edges.append(line)
        return edges

    def compute_perimeter(self):
        perimeter = sum(edge.get_length() for edge in self._edges)
        print(f"  Perímetro total: {perimeter:.2f}")
        return perimeter

    def compute_area(self):
        raise NotImplementedError("Área no implementada para figura genérica")

    def compute_inner_angles(self):
        raise NotImplementedError("Ángulos internos no implementados")

    def get_edges(self):
        return self._edges

    def get_vertices(self):
        return self._vertices

    def get_is_regular(self):
        return self._is_regular