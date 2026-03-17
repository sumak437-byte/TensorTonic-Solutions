def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x=x0
    for step in range(steps):
        dy = 2*a*x + b #compute derivative 
        x_new = x-(lr*dy)
        x=x_new 
    return x 
    