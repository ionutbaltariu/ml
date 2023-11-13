from typing import List

def derivative(f, x, h=0.01):
    """
    A numerical way to calculate the derivative of a single variable function in a numerical way.
    A derivative measures the rate of change with which the argument changes (in a given point)
    very cool visualization: https://ro.wikipedia.org/wiki/Derivat%C4%83#/media/Fi%C8%99ier:Graph_of_sliding_derivative_line.gif
    https://en.wikipedia.org/wiki/Numerical_differentiation
    https://en.wikipedia.org/wiki/Symmetric_derivative
    :param f: the function
    :param x: the point
    :param h: the delta compared to the given point
    :return: the value of the derivative in that given point
    """
    return (f(x + h) - f(x - h)) / (2 * h)


def dot_product(a: List, b: List):
    if len(a) != len(b):
        raise Exception("Cannot compute dot product for vectors that aren't the same dimension!")

    return sum([x * y for x, y in zip(a, b)])


def x_squared(x):
    return x * x

def test_fct(x):
    return x ** 4 - 4 * x ** 2 + 2 * x + 1


def x_squared_minus(a, x):
    return x * x - a
# print(dot_product([1, 2, 3], [3, 2, 1]))
