from Help.color import Color


class Material:
    """Material hat zunächst nur eine Farbe, es gibt noch keine Interaktion mit Licht
     und Eigenschaften, die sich mit Licht interargieren wird"""
    # beginnend mit diesen Werten
    # ambient = 0.05
    # diffuse = 1.0

    def __init__(self, color=Color.from_hex("#FFFFFF"), ambient=0.05, diffuse=1.0, specular=1.0):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular

    # wo trifft
    def color_at(self, position):
        return self.color
