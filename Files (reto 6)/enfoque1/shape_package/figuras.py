# Clase para representar un punto en el plano
class Point:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Las coordenadas deben ser números")
        self._x = x
        self._y = y

    def compute_distance(self, other):
        if not isinstance(other, Point):
            raise TypeError("El parámetro debe ser un objeto Point")
        return ((self._x - other._x) ** 2 + (self._y - other._y) ** 2) ** 0.5

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError("La coordenada x debe ser un número")
        self._x = x

    def set_y(self, y):
        if not isinstance(y, (int, float)):
            raise ValueError("La coordenada y debe ser un número")
        self._y = y


# Clase para representar una línea entre dos puntos
class Line:
    def __init__(self, start_point, end_point):
        if not isinstance(start_point, Point) or not isinstance(end_point, Point):
            raise TypeError("Los puntos deben ser objetos Point")
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
        if not isinstance(p, Point):
            raise TypeError("El punto debe ser un objeto Point")
        self._start_point = p
        self._length = self._start_point.compute_distance(self._end_point)

    def set_end_point(self, p):
        if not isinstance(p, Point):
            raise TypeError("El punto debe ser un objeto Point")
        self._end_point = p
        self._length = self._start_point.compute_distance(self._end_point)


# Clase base para cualquier figura
class Shape:
    def __init__(self, vertices):
        if not isinstance(vertices, list) or len(vertices) < 3:
            raise ValueError("Debe tener al menos 3 vértices en una lista")
        for i, vertex in enumerate(vertices):
            if not isinstance(vertex, Point):
                raise TypeError(f"El vértice {i+1} debe ser un objeto Point")
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


# Clase cuadrado que hereda de rectángulo
class Square(Rectangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._is_regular = True


# Clase base para triángulos
class Triangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)

    def compute_area(self):
        try:
            a, b, c = [edge.get_length() for edge in self._edges]
            s = (a + b + c) / 2
            area_squared = s * (s - a) * (s - b) * (s - c)
            if area_squared < 0:
                raise ValueError("Los puntos no forman un triángulo válido")
            area = area_squared ** 0.5
            print(f"  Lados: {a:.2f}, {b:.2f}, {c:.2f}")
            print(f"  Semiperímetro: {s:.2f}")
            print(f"  Área: {area:.2f}")
            return area
        except ValueError as e:
            print(f"Error calculando área del triángulo: {e}")
            return 0


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