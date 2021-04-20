from Help.color import Color


class Light:
    """Punktlicht mit vorgegebener Position und Farbe"""

    def __init__(self, position, color=Color.from_hex("#FFFFFF")):
        self.position = position
        self.color = color
