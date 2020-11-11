#Assumindo m = 2, R = 50

#f(x) tem menos operações algébricas que g(x), pelo que a derivada é mais simples
#pelo que será mais eficiente

def f(x):
    return x**2 - 50
def df(x):
    return 2*x
def g(x):
    return 1 - (50 / x**2)
def dg(x):
    return 100/x**3

def mnewton(x, err):
    it = 1
    xn = x
    x = xn - f(xn)/df(xn) #substituir com f(x) / g(x)
    print("it: " + str(it) + " -> " + "x: " + str(x))
    while (abs(xn - x) > err):
        it += 1
        xn = x
        x = xn - f(xn)/df(xn)
        print("it: " + str(it) + " -> " + "x: " + str(x))

mnewton(20, 0.0001)