from helpers import derivative


def one_var_stochastic_grad_descent(f):
    pass


def get_gradient_descent_dots(fct, start_x, learning_rate=0.1, tolerance=10e-6, num_of_iterations=1000):
    dots = []
    x = start_x

    for iteration in range(num_of_iterations):
        dots.append((x, fct(x)))
        gradient = derivative(fct, x)
        x_new = x - learning_rate * gradient
        if abs(x_new - x) < tolerance:
            break
        x = x_new

    return dots
