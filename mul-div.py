from manimlib.imports import *

# class final(Scene):
#     def construct(self):

class intro(Scene):
    def construct(self):

        intro_text1 = TextMobject("The following is a sample module made entirely")
        intro_text2 = TextMobject("with")
        intro_text3 = TextMobject("Python and Manim", color=GOLD).scale(2)
        intro_text1.next_to(intro_text2, UP)
        intro_text3.next_to(intro_text2, DOWN)

        self.play(Write(intro_text1))
        self.play(Write(intro_text2))
        self.play(Write(intro_text3))
        self.wait(2)
        self.play(Uncreate(intro_text1), Uncreate(intro_text2), Uncreate(intro_text3))
        self.wait(1)
        
class mod11(Scene):
    def construct(self):
        
        mod1_intro = TextMobject("Class 4: Multiplication").scale(1.5)    
    
        mod11_intro = TextMobject("First we'll try to relate Multiplication with Addition")
        mod11 = TextMobject("2 x 3 = 3 + 3 = 6")
        mod11_edge = mod11.to_edge(UP)
        face_holder11 = TextMobject("3 + 3 = 6").scale(2)
        face_holder11.move_to(UP)
        circle11 = Circle(fill_color = YELLOW, fill_opacity = 1, color = YELLOW, radius=0.5)
        circle12 = Circle(fill_color = YELLOW, fill_opacity = 1, color = YELLOW, radius=0.5)
        circle12.next_to(circle11, DOWN)
        circle13 = Circle(fill_color = YELLOW, fill_opacity = 1, color = YELLOW, radius=0.5)
        circle13.next_to(circle12, DOWN)
        circle_group11 = Mobject.add(circle11, circle12, circle13)
        circle_group11.next_to(face_holder11, DOWN)
        circle_group12 = circle_group11.copy().next_to(circle_group11, 4*LEFT)
        circle_group13 = circle_group12.copy().next_to(circle_group11, 4*RIGHT)
        circle_group14 = circle_group12.copy().next_to(circle_group13, RIGHT)
   
        self.play(Write(mod1_intro))
        self.wait(2)
        self.play(ReplacementTransform(mod1_intro, mod11_intro))
        self.wait(2)   
        self.play(ReplacementTransform(mod11_intro, mod11))
        self.wait(1)
        self.play(ReplacementTransform(mod11, mod11_edge))
        self.wait(1)
        self.play(ShowCreation(face_holder11))
        self.wait(1)
        self.play(FadeIn(circle_group11), FadeIn(circle_group12))
        self.wait(2)
        self.play(Transform(circle_group11, circle_group13), Transform(circle_group12, circle_group14), run_time=2)
        self.wait(3)
        self.play(Uncreate(circle_group11), Uncreate(circle_group12), Uncreate(face_holder11), Uncreate(mod11))
        self.wait(2)

class mod12(Scene):

    def construct(self):    

        mod12_intro = TextMobject("Another Example").scale(1.5)
        mod12 = TextMobject("3 x 6 = 6 + 6 + 6 = 18")
        mod12_edge = mod12.to_edge(UP)
        face_holder12 = TextMobject("6 + 6 + 6 = 18").scale(2)
        face_holder12.move_to(1.5*UP)
        circle21 = Circle(fill_color = ORANGE, fill_opacity = 1, color = ORANGE, radius=0.25)
        circle22 = Circle(fill_color = ORANGE, fill_opacity = 1, color = ORANGE, radius=0.25).next_to(circle21, DOWN)
        circle23 = Circle(fill_color = ORANGE, fill_opacity = 1, color = ORANGE, radius=0.25).next_to(circle22, DOWN)
        circle24 = Circle(fill_color = ORANGE, fill_opacity = 1, color = ORANGE, radius=0.25).next_to(circle23, DOWN)
        circle25 = Circle(fill_color = ORANGE, fill_opacity = 1, color = ORANGE, radius=0.25).next_to(circle24, DOWN)
        circle26 = Circle(fill_color = ORANGE, fill_opacity = 1, color = ORANGE, radius=0.25).next_to(circle25, DOWN)
        circle_group21 = Mobject.add(circle21, circle22, circle23, circle24, circle25, circle26)
        circle_group21.next_to(face_holder12, DOWN).align_to(face_holder12, LEFT)
        circle_group22 = circle_group21.copy().next_to(circle_group21, 6*RIGHT)
        circle_group23 = circle_group21.copy().next_to(circle_group21, 14*RIGHT)
        circle_group24 = circle_group21.copy().next_to(face_holder12, DOWN).align_to(face_holder12, RIGHT)
        circle_group25 = circle_group21.copy().next_to(circle_group24, RIGHT)
        circle_group26 = circle_group21.copy().next_to(circle_group25, RIGHT)
        
        self.play(Write(mod12_intro))
        self.wait(2)
        self.play(Uncreate(mod12_intro))
        self.play(Write(mod12_edge)) 
        self.wait(2)
        self.play(ShowCreation(face_holder12))
        self.wait(2)
        self.play(ShowCreation(circle_group21), ShowCreation(circle_group22), ShowCreation(circle_group23))
        self.wait(2)
        self.play(Transform(circle_group23, circle_group24), Transform(circle_group22, circle_group25), Transform(circle_group21, circle_group26))
        self.wait(2)
        self.play(Uncreate(circle_group23), Uncreate(circle_group22), Uncreate(circle_group21), FadeOut(face_holder12), FadeOut(mod12_edge))
        self.wait(2)

class mod21(Scene):

    def construct(self):        

        mod21_intro1 = TextMobject("Let us try to visualize the associative property of")
        mod21_intro2 = TextMobject("Multiplication")
        mod21_intro1.next_to(mod21_intro2, UP)

        self.play(Write(mod21_intro1), run_time=1)
        self.play(Write(mod21_intro2))
        self.wait(2)