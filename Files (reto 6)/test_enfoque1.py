print("PROBANDO ENFOQUE 1: Módulo único")
from enfoque1.shape_package import Point, Square, Rectangle, Scalene , Line

try:
    # Cuadrado de lado 2
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


try:
    # Triángulo escaleno
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(2, 3)
    triangulo = Scalene([p1, p2, p3])

    print("TRIÁNGULO ESCALENO:")
    triangulo.compute_perimeter()
    triangulo.compute_area()
    print(f"¿Es regular? {'Sí' if triangulo.get_is_regular() else 'No'}")

except (ValueError, TypeError) as e:
    print(f"Error creando el triángulo: {e}")


# Ejemplo de manejo de errores
print("EJEMPLOS DE MANEJO DE ERRORES:")

try:
    # Intentar crear un punto con datos inválidos
    punto_malo = Point("hola", 5)
except ValueError as e:
    print(f"Error: {e}")

try:
    # Intentar crear una figura con pocos vértices
    figura_mala = Square([Point(0, 0), Point(1, 1)])
except ValueError as e:
    print(f"Error: {e}")

try:
    # Intentar crear una línea con algo que no es un punto
    linea_mala = Line("no soy punto", Point(1, 1))
except TypeError as e:
    print(f"Error: {e}")





