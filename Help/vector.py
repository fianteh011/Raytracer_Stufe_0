import math
import numpy


class Vector:
    """Vektorklasse für 3d-Vektoren"""

    # n ist anzahl der Koeffizienten

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """Ausgabe des Vektors als string"""
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __add__(self, other):
        """addition"""
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Subtraktion"""
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """Vektor mal Zahl"""
        # if other is a vector, this assert fails
        # other must be a number
        assert not isinstance(other, Vector)
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        """Zahl mal Vektor"""
        return self.__mul__(other)

    def __truediv__(self, other):
        assert not isinstance(other, Vector)
        # ensure "other" ist not a Vector
        # divison is not kommutativ as mulitplicaiton
        return Vector(self.x / other, self.y / other, self.z / other)

    def dot_product(self, other):
        """Hier fehlt Ihre Implementierung für das Skalarprodukt"""
        # result = numpy.dot(numpy.array(self)[:, 0], other) ## Ansatz mit numpy
        # eigene ImplementationA
        # for i in range(0, 3):
        #     result = result + self[i] * other[i]
        # return result
        assert isinstance(other, Vector)
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        """Hier fehlt Ihre Implementierung für das Vektorprodukt/Kreuzprodukt"""
        #  x   y   z
        #  i   j   k
        # |a1  a2  a3|
        # |b1  b2  b3|
        # ((a2 * b3) - (a3 * b2))i
        i = (self.y * other.z) - (self.z * other.y)

        # (a3 * b1) - (a1 * b3)
        j = (self.z * other.x) - (self.x * other.z)

        # (a1 * b2) - (a2 * b1)
        k = (self.x * other.y) - (self.y * other.x)

        result = Vector(i, j, k)
        return result

    def magnitude(self):
        """Hier fehlt Ihre Implementierung für die Vektorlänge"""
        # result = 0
        # result = result + abs(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2))
        #
        # return result
        return abs(math.sqrt(self.dot_product(self)))

    def normalize(self):
        """Hier fehlt Ihre Implementierung für einen auf Länge 1 normalisierten
           Vektor"""
        # length = self.magnitude()
        # self.x = self.x / length
        # self.y = self.y / length
        # self.z = self.z / length
        return self.__mul__(1/self.magnitude())

    # Formel = (1 / Vektorlänge) * Vektor
