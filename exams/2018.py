from math import sin, cos, exp, sqrt, log

#PERGUNTA 1

'''
def f(x,y):
    return sin(x+y) - exp(x-y)

def g(x,y):
    return cos(x+y) - x**2*y**2

def fx(x,y):
    return cos(x+y) - exp(x-y)

def fy(x,y):
    return cos(x+y) + exp(x-y)

def gx(x,y):
    return -sin(x+y) - 2*x*y**2

def gy(x,y):
    return -sin(x+y) - 2*y*x**2


def sistema_newton(f1, f1x, f1y, f2, f2x, f2y, x, y):
    for _ in range(2):
        xi = x
        yi = y
        x = xi - (f1(xi,yi)*f2y(xi,yi) - f2(xi,yi)*f1y(xi,yi)) / (f1x(xi,yi)*f2y(xi,yi) - f1y(xi,yi)*f2x(xi,yi))
        y = yi - (f2(xi,yi)*f1x(xi,yi) - f1(xi,yi)*f2x(xi,yi)) / (f1x(xi,yi)*f2y(xi,yi) - f1y(xi,yi)*f2x(xi,yi))
        print("x: " + str(x))
        print("y: " + str(y))

sistema_newton(f,fx,fy,g,gx,gy,0.5,0.25)
'''

#PERGUNTA 3

'''
def f(x,y):
    if x == 0 and y == 0:
        return 1.1
    elif x == 0 and y == 1:
        return 2.1
    elif x == 0 and y == 2:
        return 7.8
    elif x == 1 and y == 0:
        return 1.4
    elif x == 1 and y == 1:
        return 4
    elif x == 1 and y == 2:
        return 1.5
    elif x == 2 and y == 0:
        return 9.8
    elif x == 2 and y == 1:
        return 2.2
    elif x == 2 and y == 2:
        return 1.2

def double_simpson(ax, bx, ay, by, nx, ny, f):
    hx = (bx - ax) / nx
    hy = (by - ay) / ny
    s = 0

    for i in range(0, ny + 1):
        if i == 0 or i == ny:
            p = 1
        elif i % 2 != 0:
            p = 4
        else:
            p = 2

        for j in range(0, nx + 1):
            if j == 0 or j == nx:
                q = 1
            elif j % 2 != 0:
                q = 4
            else:
                q = 2

            x = ax + j*hx
            y = ay + i*hy
            s += p*q * f(x, y)

    
    print("Resultado integral duplo, pelo método de simpson: " + str(hx * hy / 9 * s))
    return hx * hy / 9 * s   

double_simpson(0,2,0,2,2,2,f)
'''

#PERGUNTA 4

'''
def dy(t,y,z):
    return z

def dz(t,y,z):
    return -7*z - 4*y

def Euler_sistemas(xmin,xmax,x,y,z,f,g,h):
    for _ in range(0, round((xmax - xmin)/h)):
        y1 = y + h*f(x,y,z)
        z += h*g(x,y,z)
        y = y1
        x += h
        print(y,z)
    return (y,z)

Euler_sistemas(0.4,1,0.4,2,1,dy,dz,0.2)
'''

#PERGUNTA 5

'''
def f(x):
    return (x-9)**2 + x**4

def optimized_golden(f, step, guess):

    #Get search direction
    if (f(guess + step) > f(guess)):
        step = -step

    a = guess

    while (f(guess + step) < f(guess)):
        a = guess
        guess += step

    b = guess

    #Intervalo [a,b]

    #GOLDEN SECTION
    d = a + ((sqrt(5)-1)/2) * (b-a)
    c = a + (1 - (sqrt(5)-1)/2) * (b-a)

    print("a = " + str(a) + "\t" + "f(a)" + str(f(a)))
    print("b = " + str(b) + "\t" + "f(b)" + str(f(b)))
    print("c = " + str(c) + "   f(c)" + str(f(c)))
    print("d = " + str(d) + "   f(d)" + str(f(d)))
    print()

    while (b-a > 0.0001):

        if (f(c) < f(d)):
            b = d
        elif (f(c) > f(d)):
            a = c

        d = a + ((sqrt(5)-1)/2) * (b-a)
        c = a + (1 - (sqrt(5)-1)/2) * (b-a)

        print("a = " + str(a) + "\t" + "f(a)" + str(f(a)))
        print("b = " + str(b) + "\t" + "f(b)" + str(f(b)))
        print("c = " + str(c) + "   f(c)" + str(f(c)))
        print("d = " + str(d) + "   f(d)" + str(f(d)))
        print()

    return (a + b) / 2


print(optimized_golden(f, 0.05, 6))
'''
