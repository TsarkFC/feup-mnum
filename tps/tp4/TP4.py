from math import sqrt

#2x^2 - 5x - 5
#-1 - resolver fórmula resolvente
# 0 - guess

#fórmula resolvente
def f_resol(a, b, c):
    return [(-b + sqrt(b*b-4*a*c)) / (2 * a), (-b - sqrt(b*b-4*a*c)) / (2 * a)]

#função
def function(x):
    return 2*x*x - 5*x -5

#função derivada
def d_function(x):
    return 4*x - 5

def metodo_tangente(x):
    count = 0
    while (True):
        if (count == 5):
            break
        if (x == x - function(x) / d_function(x)):
            count += 1
        x = x - function(x) / d_function(x)
        print(x)
    return x

print(f_resol(2, -5, -5))
#print(metodo_tangente(0))

def metodo_corda(x1, x2):
    x = (x1 * function(x2) - x2 * function(x1)) / (function(x2) - function(x1))
    for _ in range(10):
        if (x*x1 < 0):
            x2 = x
            x = (x1 * function(x2) - x2 * function(x1)) / (function(x2) - function(x1))
        else:
            x1 = x
            x = (x1 * function(x2) - x2 * function(x1)) / (function(x2) - function(x1))
        print(x)
    return x

print(metodo_corda(2,-5))
