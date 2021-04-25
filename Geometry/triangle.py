class Triangle:

    def __init__(self, pointA, pointB, pointC, material ):
        self.pointA = pointA
        self.pointB = pointB
        self.pointC = pointC
        self.material = material
        self.name = "Dreieck"

    def normal(self, surface_point):
        """normal zur Berechnung der Flächennormalen"""
        #Jeder Punkt im Dreieck hat den selben Normaleneinheitsvektor!
        v = surface_point - self.pointA
        w = self.pointC - self.pointA
        n = v.cross_product(w).normalize()
        return n

    def intersect_t(self, ray):
        """Zur Überprüfung eines Schnitts des Strahls mit einer Fläche mit gegebenener Flächennormalen"""
        n = self.normal(self.pointB)
        a = ray.origin
        u = ray.direction

        o = n.dot_product(self.pointA - a)
        bruch = (o / n.dot_product(u))
        ts = a + bruch * u

        if self.pointintriangle(ts):
            abstand = ts - ray.origin
            return abstand.magnitude()
        return None

    def pointintriangle(self, punkt):
        """zum Test, ob ein gegebener Punkt im gegebenen Dreieck liegt"""
        xs = punkt
        b = self.pointB - self.pointA
        c = self.pointC - self.pointA
        p = xs - self.pointA

        quadC = (c.magnitude() ** 2)
        quadB = (b.magnitude() ** 2)
        u = (p.dot_product(b) * quadC - c.dot_product(b) * p.dot_product(c)) / quadB * quadC - (c.dot_product(b) ** 2)
        v = (p.dot_product(c) * quadB - c.dot_product(b) * p.dot_product(b)) / quadB * quadC - (c.dot_product(b) ** 2)

        if 0 <= u and u <= 1 or 0 <= v and v <= 1 or 0 <= u+v and u+v <= 1:
            return True
        else:
            return False

