from Help.color import Color
from Help.vector import Vector
from Render.ray import Ray
from triangle import Triangle
from Help.point import Point
from Render.material import Material

A = Point(2, 2, 3)
B = Point(2, 5, 3)
C = Point(2, 5, 5)
blau = Color.from_hex("#0000FF")
triangle = Triangle(A, B, C, Material(blau))

X = Point(2, 4, 3)

print( triangle.normal(X) )
print( triangle.intersect_t(Ray(Vector(0,0,-1), Vector(2, 7, 5))) )
print(2**8)