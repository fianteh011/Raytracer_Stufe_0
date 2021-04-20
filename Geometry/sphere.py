from math import sqrt


class Sphere:
    """ Klasse zur Repräsentation von Sphären (Kugelflächen) in 3d"""

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material
        self.name = "Kugel"

    def intersects(self, ray):
        """Prüft Schnittpunkt Ray-Kugelfläche. Return: Abstand origin Schnittpunkt oder None, wenn kein Schnittpunkt
        vorliegt """
        """Hier fehlt Ihre Implementierung"""
        # a = 1
        # discriminat = b**2 - 4ac
        # if discriminant > 0: intersects at 2 Points
        # if disciminatn = 0: intersects at 1 Point
        # if discriminant < 0 := no intersection
        # distance to point from intersection from ray_ori := (-b +- sqrt(disc))/2a
        # camera is always in negative  z (0, 0, -1)

        sphere_to_ray = ray.origin - self.center
        # a = 1
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        discriminant = (b * b - 4 * c)

        if discriminant >= 0:
            abstand = (-b - sqrt(discriminant))/2
            if abstand > 0:
                return abstand
        return None

    """Alternative Ansatz zur Berechnung der Schnittpunkte"""
    # Schnittpunkt bestimmen
    # def intersects(self, ray):
    #     """Prüft Schnittpunkt Ray-Kugelfläche. Return: Abstand origin Schnittpunkt oder None, wenn kein Schnittpunkt vorliegt"""
    #
    #     # Gegeben: Mittelpunkt M und Radius r
    #     M = self.center
    #     r = self.radius
    #
    #     # 1 L = Abstand zwischen Origin und Mittelpunkt
    #     L = M - ray.origin
    #
    #     # 2 Skalarprodukt verwenden um Länge von tc zu bestimmen
    #     tc = L.dot_product(ray.direction)
    #     # Wenn tc kleiner als 0 ist dann liegt kein Schnittpunkt vor
    #     if tc < 0:
    #         return None
    #
    #     # 3 d berechnen mit Satz d. Pythagoras
    #     qD = (tc * tc) - (L.magnitude() * L.magnitude())
    #     qDLength = sqrt(qD * qD)
    #     d = sqrt(qDLength)
    #
    #     # Wenn d größer ist als der radius muss Strahl außerhalb liegen!
    #     if d > r:
    #         return None
    #
    #     # 4 t1c berechnen: Abstand zwischen Punkt und Mittelpunkt
    #     t1c = sqrt((r * r) - (d * d))
    #
    #     # 5 Abstand von Origin zum Punkt:
    #     t1 = tc - t1c  #erste Punkt
    #     # t2 = tc + t1c #zweite Punkt
    #
    #     # 6 Schnittpunkt bestimmen
    #     schnittpunkt = ray.origin + (ray.direction * t1)
    #
    #     # 7 Abstand zw Origin & Schnittpunkt
    #     abstand = schnittpunkt - ray.origin
    #     return abstand.magnitude()

    def normal(self, surface_point):
        """Return: Normale auf der Fläche bezogen auf den Flächenpunkt"""
        """Hier fehlt Ihre Implementierung"""
        # berechne die Differenz zwischen dem Flächenpunkt und dem Mittelpunkt
        return (surface_point - self.center).normalize()
