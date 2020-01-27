from math import cos, sin

def f(x):
    return (x - 3.6) + cos(x+1.2)**3
def df(x):
    return 1 - 3 * (cos(x + 1.2)**2) * sin(x + 1.2)

def newton_root(x, err):
    xn = x
    x = xn - (f(xn))/(df(xn))
    while (abs(xn-x) > err):
        xn = x
        x = xn - (f(xn))/(df(xn))
        print("x: " + str(x))
newton_root(0.5, 0.001)