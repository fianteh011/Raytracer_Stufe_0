from Help.vector import Vector


class Ray:
    """Ray (Strahl) ausgehend von origin (Aufpunkt) in
       Richtung direction (Richtungsvektor normalisiert)"""

    # constructor for ray
    def __init__(self, origin, direction):
        """ Hier fehlt Ihre Implementierung"""
        self.origin = origin
        # normalize contrustor in array itself
        self.direction = direction.normalize()
