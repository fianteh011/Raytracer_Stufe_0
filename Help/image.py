from PIL import Image
import numpy as np


class MyImage:
    """Initialisiert ein numpy-array zur Aufnahme der Pixelkoordinaten und Farbe"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = np.zeros((height, width, 3), dtype=np.uint8)
        # _ because variables are not going to be utilise

    def set_pixel(self, x, y, col):
        def to_byte(col):
            return round(max(min(col * 255, 255), 0))

        self.pixels[y][x] = [to_byte(col.x), to_byte(col.y), to_byte(col.z)]

    """ Wandelt das numpy-array in ein image-file RGB, speichert das Bild bzw. zeigt das Bild an"""

    def write_image(self, img_file):
        img = Image.fromarray(self.pixels, 'RGB')
        img.save(img_file)

    def show_image(self):
        img = Image.fromarray(self.pixels, 'RGB')
        img.show()
