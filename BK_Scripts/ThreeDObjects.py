from manimlib.imports import *

class ThreeDObjects(SpecialThreeDScene):
    def construct(self):
        sphere = self.get_sphere()
        cube = Cube()
        prism = Prism()
        self.play(ShowCreation(sphere))
        self.wait(1)
        self.play(ReplacementTransform(sphere, cube))
        self.wait(1)
        self.play(ReplacementTransform(cube, prism))
        self.wait(2)