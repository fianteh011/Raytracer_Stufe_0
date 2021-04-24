from Help.color import Color
from Help.image import MyImage
from Help.point import Point
from Render.ray import Ray


class RenderEngine:
    """Rendert 3D Objekte in 2D Pixelbilder mittels ray tracing"""
    """Erzeugt Pixel als array"""

    def rendertask(self, scene, zaehler):
        # Anpassung Bildausgabe (Pixelformat) an "virtuellen Screen [-1,1]x[-1,1]"
        width = scene.width
        height = scene.height
        # aspect_ratio1 = float(width) / height
        aspect_ratio = float(width - 1) / (height - 1)
        # leftmost extreme for x --> x0
        # rightmost extreme for x--> x1
        x0 = -1.0
        x1 = +1.0
        # berechne wie viel Schritte um jeweils x-Schritte, --> delta
        x_step = (x1 - x0) / (width - 1)
        y0 = -1.0 / aspect_ratio
        y1 = +1.0 / aspect_ratio
        y_step = (y1 - y0) / (height - 1)
        # Bildausgabe (Pixelformat) initialisieren (Instanz)
        pixels = MyImage(width, height)

        # Kameraposition (Augpunkt) setzen
        camera = scene.camera

        # Bild berechnen (geschachtelte Schleifen über alle Pixel)
        for j in range(height):
            y = y0 + j * y_step  # Umrechnung "virtueller Screen" hoeh
            for i in range(width):
                x = x0 + i * x_step  # Umrechnung "virtueller Screen" breite
                ray = Ray(camera, Point(x, y, 0.0) - camera)
                pixels.set_pixel(i, j, self.ray_trace(ray, scene))
                # eine Symmetrie des Algorithmuses soll in CG vorhanden sein
                # sodass es richtig implementiert ist


            ###################################################################################
            # Fortschrittszähler ausgeben, falls zaehler=True
            if zaehler:
                print("{:3.0f}%".format(float(j) / float(height) * 100), end="\r")
        return pixels

    # def rendertask(self, scene,zaehler):
    #     # Anpassung Bildausgabe (Pixelformat) an "virtuellen Screen [-1,1]x[-1,1]"
    #     width = scene.width
    #     height = scene.height
    #     aspect_ratio = float(width-1)/(height-1)
    #     x0 = -1.0
    #     x1 = +1.0
    #     xstep = (x1 - x0) / (width - 1)
    #     y0 = -1.0 / aspect_ratio
    #     y1 = +1.0 / aspect_ratio
    #     ystep = (y1 - y0) / (height - 1)
    #     # Bildausgabe (Pixelformat) initialisieren (Instanz)
    #     pixels = MyImage(width, height)
    #
    #     # Kameraposition (Augpunkt) setzen
    #     camera = scene.camera
    #
    #     # Bild berechnen (geschachtelte Schleifen über alle Pixel)
    #     for j in range(height):
    #         y = y0 + j * ystep # Umrechnung "virtueller Screen"
    #         for i in range(width):
    #             x = x0 + i * xstep # Umrechnung "virtueller Screen"
    #             ray = Ray(camera, Point(x, y) - camera)
    #             pixels.set_pixel(i, j, self.ray_trace(ray, scene))
    #     ######### Hier fehlt Ihre Implementierung#########################################
    #             ##### raytrace-Algorithmus starten
    #             ##### ray erzeugen
    #             ##### pixel (Farbe) mit ray_trace berechnen
    #     ###################################################################################
    #         # Fortschrittszähler ausgeben, falls zaehler=True
    #         if zaehler:
    #             print("{:3.0f}%".format(float(j) / float(height) * 100), end="\r")
    #     return pixels

    def ray_trace(self, ray, scene, depth=0):
        # Berechnet den vom ray getroffenen nächstgelegenen Objektpunkt jnd gibt die
        # Farbinformation dazu aus. Kein Treffer: Farbe schwarz

        # Farbe initialisieren (schwarz)
        color = Color(0, 0, 0)
        ######### Hier fehlt Ihre Implementierung#########################################
        # nächstgelegenen Schnittpunkt zwischen ray und einem Objekt der
        # Szene auswählen
        dist_hit, obj_hit = self.find_nearest_hit(ray, scene)
        if obj_hit is None:
            return color
        # Schnittpunkt vorhanden: Punkt berechnen, Normale berechnen, gesamte Farbinformation
        # berechnen
        # Kollisionspunkt mit dem Objekt
        hit_pos = ray.origin + ray.direction * dist_hit # gerade Gleichung: y = mx +c
        # berechne diffuse und spekular--> wie die Normale auf getroffenen Punkt lautet
        hit_normal = obj_hit.normal(hit_pos)
        color += self.color_at_hit(obj_hit, hit_pos, hit_normal, scene)
        return color

    def find_nearest_hit(self, ray, scene):
        # Berechnung des nächstgelegenen Schnittpunkt zwischen ray und einem Objekt der
        # Szene. Rückgabe: Objekt und Abstand Augpunkt-Schnittpunkt

        # Initialisierung (noch keine Rückgabedaten: None)
        dist_min = None  # Abstand zum nächstgelegenen Objekt
        obj_hit = None  # nächstgelegenes Objekt
        # Schleife über alle Objekte der Szene
        # theoretisch kann ein Objekt verdeckt
        for obj in scene.objects:
            # Hier wird der Schnittpunkt zwischen Objekt und Strahl berechnet
            # zunächst nur für Kugelflächen (sphere)
            distance = obj.intersects(ray)
            # comparison with is None or is not None
            # ausrufezeichen sind nicht so übersichtlich
            if distance is not None and (obj_hit is None or distance < dist_min):
                dist_min = distance # neu füllen
                obj_hit = obj
        return dist_min, obj_hit

    def color_at_hit(self, obj_hit, hit_pos, normal, scene):
        # Farbinformation des getroffenen Objekts im Schnittpunkt ermitteln
        material = obj_hit.material

        # Nur Objektfarbe anzeigen
        obj_color = material.color_at(hit_pos)

        # Ambientes Licht = Grundhelligkeit der Szene
        color = material.ambient * Color.from_hex("#000000")
        # specular potenz:
        spekular_k = 50.00 # wird später im Praktikum 2

        # gehe in jedem Licht duch und berechne schatten
        for light in scene.lights:
            # Abstand zwischen Lichtquelle und Kollisionspunkt
            # to_lights = Ray(hit_pos, light.position - hit_pos)
            augpunkt = hit_pos
            direction = light.position - hit_pos

            # erzeuge einen Ray
            new_ray_l = Ray(augpunkt, direction)
            """Lambert-Shading für diffuses Licht"""
            # eintreffendes Licht streut in alle Richtungnen (matte Oberflaeche)
            # cos (phi) = <normal, new_ray_l.direction>
            cos = normal.dot_product(new_ray_l.direction)

            color += (obj_color
                      * material.diffuse
                      * max(cos, 0))
            # max: um negative Werten zu vermeiden
            # z.B. wenn das Licht nur die vordere Oberfläche aufleuchtet

            # Blinn Phong-Beleuchtungsmodell fasst die drei Beiträgt zusammen (ambient, diffuse und speuklar)-->wird
            # später im Praktikum 2
            half_vector = (new_ray_l.direction + augpunkt).normalize()
            color += ((light.color * material.specular) * max(normal.dot_product(half_vector), 0))
        return color

