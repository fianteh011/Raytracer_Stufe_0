"""Einfacher raytracer
Stufe_3: Es werden nur die Objektfarben ermittelt"""
from Help.color import Color
from Help.point import Point
from Help.image import MyImage
from Help.vector import Vector
from Render.light import Light
from Render.material import Material, SchachbrettMaterial
from Render.engine import RenderEngine
from Render.scene import Scene
from Render.camera import Camera
from Geometry.sphere import Sphere
from Geometry.triangle import Triangle

##### Anzeige des Renderfortschritts (True: mit Anzeige, False: ohne Anzeige)
ZAEHLER = True

SHOW = True
##### Bildformat festlegen (für Tests kleines Ausgabeformat, um Renderzeit zu sparen)
# Grossbuchstaben sind Konstanten !
WIDTH = 320 #320 #800 #1600
HEIGHT = 200 #200 #600 #1200

##### Ausgabe am Bildschirm (True) oder in der angegebenen Datei (False)
RENDERED_IMG = "stufe3_2balls_schachbrett_" + WIDTH.__str__() + "x" + HEIGHT.__str__() + ".PNG"

def main():
    ##### Augpunkt/Camera setzen#
    CAMERA = Camera(0, 0, -1)

    ##### Objekte der Szene lokal erzeugen

    ##FARBEN
    rot = Color.from_hex("#FF0000")
    gelb = Color.from_hex("#FFFF00")

    ##Kugeln
    kugel1 = Sphere(Point(0.75, -0.1, 1.0), 0.6, Material(rot))
    kugel2 = Sphere(Point(-0.75, -0.1, 2.5), 0.6, Material(gelb))

    #Schachbrett-Ebene
    braun = Color.from_hex("#4A3601")
    beige = Color.from_hex("#e7b36e")
    schachbrettMaterial = SchachbrettMaterial(
        color1=braun,
        color2=beige,
        ambient=0.2,
        reflection=0.2
    )
    grundebene = Sphere(Point(0, 10000.5, 1), 10000.0, schachbrettMaterial)

    #Dreieck
    A = Point(-4.0, -2.0, 3.0)
    B = Point(-1.0, 0.0, 3.0)
    C = Point(1.0, -2.0, 3.0)
    blau = Color.from_hex("#0000FF")
    dreieck = Triangle(A, B, C, Material(blau))

    #TestDreieck
    A2 = Point(-0.75, -0.1, 2.5)
    B2 = Point(1.0, 1.0, 4.5)
    C2 = Point(3.0, -3.0, 4.5)

    dreieck2 = Triangle(A2, B2, C2, Material(blau))

    OBJECTS = [
        #Schachbrett-Ebene
        grundebene,
        # rote Kugel1
        kugel1,
        # gelbe kugel2
        kugel2,
        #blaues Dreieck
        dreieck
    ]
    # Punktlichter: Keine Beleuchtung nur Objektfarbe
    ##Farben
    weiss = Color.from_hex("#FFFFFF")
    grau = Color.from_hex("#F0F0F0")

    licht1 = Light(Point(1.5, -0.5, -10.0), weiss)
    licht2 = Light(Point(-0.5, -10.5, 0.0), grau)
    LIGHTS = [
        #weisses Licht
        licht1,
        #graues Licht
        licht2
    ]

    ##### Szene einrichten
    scene = Scene(CAMERA, OBJECTS, LIGHTS, WIDTH, HEIGHT)

    ##### Render-Engine instanzieren (starten)
    engine = RenderEngine()

    ##### Bild rendern (berechnen)
    image = engine.rendertask(scene, ZAEHLER)

    ##### gerendertes Bild anzeigen/speichern
    if (SHOW):
        image.show_image()
    else:
        image.write_image(RENDERED_IMG)


if __name__ == "__main__":
    main()
