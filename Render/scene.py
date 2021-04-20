class Scene:
    """Scene-Klasse bündelt/sammelt alle Informationen für die ray tracing engine"""

    def __init__(self, camera, objects, lights, width, height):
        self.camera = camera
        self.objects = objects
        self.lights = lights
        self.width = width
        self.height = height
