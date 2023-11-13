from manim import *

from gradient_descent import get_gradient_descent_dots
from helpers import x_squared, x_squared_minus, test_fct, derivative


class GradientDescent(Scene):
    def construct(self):
        # Create a graph
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-10, 10],
            axis_config={"color": BLUE},
            x_axis_config={"include_numbers": True}
        )
        graph = axes.plot(test_fct, color=BLUE)
        der = axes.plot(lambda x: derivative(test_fct, x), color=YELLOW)
        all_dots = get_gradient_descent_dots(test_fct, 0.22)
        print(all_dots[:40])
        # Animation to update parameter and cost

        self.play(Create(axes))
        self.play(Create(graph))
        self.play(Create(der))

        for dot in all_dots[:15]:
            self.play(Create(Dot(color=RED).move_to(axes.c2p(dot[0], dot[1]))))