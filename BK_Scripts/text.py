from manimlib.imports import *

class makeText(Scene):
    def construct(self):
        first_line = TextMobject("I think we can use this for i-Help Projects")
        second_line = TextMobject("This is a very useful python library - Manim")
        third_line = TextMobject("We'll try exploring this!")
        final_line = TextMobject("Mayira Pochu?", color=BLUE)
        color_final_line = TextMobject("Mayira Pochu?")

        color_final_line.set_color_by_gradient(BLUE, PURPLE)

        second_line.next_to(first_line, DOWN)
        third_line.next_to(second_line, DOWN)

        self.wait(1)
        self.play(Write(first_line))
        self.wait(1)
        self.play(Write(second_line))
        self.wait(1)
        self.play(Write(third_line))
        self.wait(2)
        self.play(FadeOut(first_line), FadeOut(third_line), ReplacementTransform(second_line, final_line))
        self.wait(1)
        self.play(Transform(final_line, color_final_line))
        self.wait(2)