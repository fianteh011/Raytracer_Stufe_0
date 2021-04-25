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

        #Schnittpunkt-Rechnung CG_1 Folie 20
        bruchOben = n.dot_product(self.pointA - a)
        bruchUnten = n.dot_product(u)
        schnittpunkt = a + (bruchOben / bruchUnten) * u

        if self.pointintriangle(schnittpunkt):
            abstand = schnittpunkt - ray.origin
            return abstand.magnitude()
        return None

    def pointintriangle(self, punkt):
        """zum Test, ob ein gegebener Punkt im gegebenen Dreieck liegt"""
        #U ausrechnen Formel aus CG_1 - Folie 22
        uo = (punkt.dot_product(self.pointB) * (self.pointC.magnitude() ** 2)) - (self.pointC.dot_product(self.pointB) * punkt.dot_product(self.pointC))
        uu = ((self.pointB.magnitude() ** 2) * (self.pointC.magnitude() ** 2)) - (self.pointC.dot_product(self.pointB) ** 2)
        u = uo / uu

        #v ausrechnen Formel aus CG_1 - Folie 22
        vo = (punkt.dot_product(self.pointC) * (self.pointB.magnitude() ** 2)) - (self.pointC.dot_product(self.pointB) * punkt.dot_product(self.pointB))
        vu = uu
        v = vo / vu

        #liegt der Punkt im Dreieck?
        if 0 <= u <= 1 and 0 <= v <= 1 and 0 <= u+v <= 1:
            return True
        else:
            return False
