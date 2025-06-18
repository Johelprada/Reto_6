# Importamos desde cada módulo individual
from .point import Point
from .line import Line
from .shape import Shape
from .rectangle import Rectangle
from .square import Square
from .triangle import Triangle, Equilateral, Isosceles, Scalene, TriRectangle

__all__ = ['Point', 'Line', 'Shape', 'Rectangle', 'Square', 'Triangle', 'Equilateral', 'Isosceles', 'Scalene', 'TriRectangle']