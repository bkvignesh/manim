from manimlib.imports import *

class Text(Scene):
    def construct(self):
        text = TextMobject("Don't think too much!")
        text2 = TextMobject("Things will be alright! We'll be there for you!")
        self.play(Write(text), run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(text, text2))
        self.wait(2)

class shapes(Scene):
    def construct(self):
        circle = Circle(color=PURPLE)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse = Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT, 5*RIGHT, color = MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow, DOWN+LEFT)
        ring = Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse,RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square), FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

class graphs(GraphScene):
    CONFIG = {"x_min": -10,
              "x_max": 10,
              "y_min": -1.5,
              "y_max": 1.5,
              "graph_origin": ORIGIN,
              "function_color": RED,
              "axes_color": GREEN,
              "x_labeled_nums": range(-10,12,2)}

    def func_to_graph(self, x):
        return np.sin(x)

    def func_to_graph2(Self, x):
        return np.cos(x)
    
    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        func_graph2 = self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label="\\sin(x)")
        graph_lab2 = self.get_graph_label(func_graph2, label="\\cos(x)")
        two_pi = TexMobject("x = 2\\pi")
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT+2*UP)

        self.play(ShowCreation(func_graph), ShowCreation(func_graph2), run_time=3)
        self.wait(1)
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2), ShowCreation(two_pi))
        self.wait(3)

class graphs2(GraphScene):
    CONFIG = {"function" : lambda x : np.cos(x), 
              "function_color" : BLUE,
              "taylor" : [lambda x: 1, lambda x: 1-x**2/2, lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4), lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6),
              lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8), lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8) - x**10/math.factorial(10)],
              "center_point" : 0,
              "approximation_color" : GREEN,
              "x_min" : -10,
              "x_max" : 10,
              "y_min" : -1,
              "y_max" : 1,
              "graph_origin" : ORIGIN,
              "x_labeled_nums" :range(-10,12,2)}

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.function, self.function_color)
        approx_graphs = [self.get_graph(f, self.approximation_color) for f in self.taylor]
        term_num = [TexMobject("n = ", str(n), aligned_edge=TOP) for n in range(0, 8)]
        term = VectorizedPoint(3*DOWN)

        approx_graph = VectorizedPoint(self.input_to_graph_point(self.center_point, func_graph))
        self.play(ShowCreation(func_graph), run_time=3)
        for n, graph in enumerate(approx_graphs):
            self.play(Transform(approx_graph, graph, run_time=2))
            Transform(term, term_num[n])
        self.wait(2)

class Dragon(MovingCameraScene):
    CONFIG = {
        "iterations":15,
        "angle":90*DEGREES,
        "border_proportion":1.25,
        "colors":[RED_A,RED_C,RED_E,BLUE_A,
                  BLUE_C,BLUE_E,YELLOW_A,YELLOW_C,
                  YELLOW_E,PURPLE_A,PURPLE_C,PURPLE_E]
    }
    def construct(self):
        self.color = it.cycle(self.colors)
        path = VGroup()
        first_line = Line(ORIGIN, UP / 5, color = next(self.color))
        path.add(first_line)

        self.camera_frame.set_height(first_line.get_height() * self.border_proportion)
        self.camera_frame.move_to(first_line)
        self.play(ShowCreation(first_line))
        self.add_foreground_mobject(path)

        self.target_path = self.get_all_paths(path,self.iterations)
        for i in range(self.iterations):
            self.duplicate_path(path,i)
        self.wait()

    def duplicate_path(self,path,i):
        set_paths = self.target_path[:2**(i + 1)]
        height = set_paths.get_height() * self.border_proportion
        new_path = path.copy()
        new_path.set_color(next(self.color))
        self.add(new_path)
        point = self.get_last_point(path)
        self.play(
            Rotating(
                new_path,
                radians=self.angle,
                about_point=path[-1].points[point],
                rate_func=linear
                ),
            self.camera_frame.move_to,set_paths,
            self.camera_frame.set_height,height,
            run_time=1, rate_func=smooth
            )
        self.add_foreground_mobject(new_path)
        post_path = reversed([*new_path])
        path.add(*post_path)

    def get_all_paths(self, path, iterations):
        target_path = path.copy()
        for _ in range(iterations):
            new_path = target_path.copy()
            point = self.get_last_point(new_path)
            new_path.rotate(
                        self.angle, 
                        about_point=target_path[-1].points[point],
                    )
            post_path = reversed([*new_path])
            target_path.add(*post_path)

        return target_path

    def get_last_point(self, path):
        return 0 if len(path) > 1 else -1