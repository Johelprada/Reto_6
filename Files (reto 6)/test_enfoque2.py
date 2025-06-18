print("PROBANDO ENFOQUE 2")
from enfoque2.shape_package import Point, Square, Rectangle, Scalene

try:
    # Rectángulo 3x2
    p1 = Point(0, 0)
    p2 = Point(0, 3)
    p3 = Point(2, 3)
    p4 = Point(2, 0)
    rectangulo = Rectangle([p1, p2, p3, p4])

    print("RECTÁNGULO:")
    rectangulo.compute_perimeter()
    rectangulo.compute_area()
    print(f"¿Es regular? {'Sí' if rectangulo.get_is_regular() else 'No'}")

except (ValueError, TypeError) as e:
    print(f"Error creando el rectángulo: {e}")

try:
    # Cuadrado
    p1 = Point(0, 0)
    p2 = Point(0, 2)
    p3 = Point(2, 2)
    p4 = Point(2, 0)
    cuadrado = Square([p1, p2, p3, p4])

    print("CUADRADO:")
    cuadrado.compute_perimeter()
    cuadrado.compute_area()
    print(f"¿Es regular? {'Sí' if cuadrado.get_is_regular() else 'No'}")

except (ValueError, TypeError) as e:
    print(f"Error creando el cuadrado: {e}")