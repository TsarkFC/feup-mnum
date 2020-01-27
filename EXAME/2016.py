from math import sin, cos, sqrt, exp

#PERGUNTA 2

'''
def f1(x,y):
    return x**2 - y - 1.2

def f1x(x,y):
    return 2*x

def f1y(x,y):
    return -1

def f2(x,y):
    return -x + y**2 - 1

def f2x(x,y):
    return -1

def f2y(x,y):
    return 2*y

def sistema_newton(x, y):
    for _ in range(2):
        xi = x
        yi = y
        x = xi - (f1(xi,yi)*f2y(xi,yi) - f2(xi,yi)*f1y(xi,yi)) / (f1x(xi,yi)*f2y(xi,yi) - f1y(xi,yi)*f2x(xi,yi))
        y = yi - (f2(xi,yi)*f1x(xi,yi) - f1(xi,yi)*f2x(xi,yi)) / (f1x(xi,yi)*f2y(xi,yi) - f1y(xi,yi)*f2x(xi,yi))
        print("x: " + str(x))
        print("y: " + str(y))
        print()

sistema_newton(1,1)
'''

#PERGUNTA 4

'''
def f(x):
    return x**7 + 0.5*x - 0.5

def corda(a,b,f):
    print(a,b)
    x= (f(a)*b - f(b)*a) / (f(a)-f(b))
    contador = 1
    for _ in range(3):
        contador += 1
        if (f(a) * f(x) < 0):
            b = x
        else:
            a = x  
        x= (f(a)*b - f(b)*a) / (f(a)-f(b))
        print(a,b)
        print(str(contador) + '\t x = ' + str(x))
    return x

corda(0, 0.8, f)
'''

#PERGUNTA 5

'''
def dy(t,y,z):
    return z

def dz(t,y,z):
    return 0.5 + t**2 + t*z

def Euler_sistemas(x,y,z,f,g,h):
    print("t   y")
    print(x,y)
    print()
    for _ in range(2):
        y1 = y + h*f(x,y,z)
        z += h*g(x,y,z)
        y = y1
        x += h
        print("t   y")
        print(x,y)
        print()
    return (y,z)

def RK4_sistemas(x,y,z,f,g,h):
    print("t   y")
    print(x,y)
    print()
    for _ in range(2):
        dy1 = h*f(x,y,z)
        dz1 = h*g(x,y,z)
        dy2 = h*f(x + h/2, y + dy1 / 2, z + dz1/2)
        dz2 = h*g(x + h/2, y + dy1 / 2, z + dz1/2)
        dy3 = h*f(x + h/2, y + dy2 / 2, z + dz2/2)
        dz3 = h*g(x + h/2, y + dy2 / 2, z + dz2/2)
        dy4 = h*f(x + h, y + dy3, z + dz3)
        dz4 = h*g(x + h, y + dy3, z + dz3)
        y += 1/6*dy1 + 1/3*dy2 + 1/3*dy3 + 1/6*dy4
        z += 1/6*dz1 + 1/3*dz2 + 1/3*dz3 + 1/6*dz4
        x += h
        print("t   y")
        print(x,y)
        print()

    return (y,z)

h = 0.25
print("Euler")
Euler_sistemas(0,0,1,dy,dz,h)
print("RK4")
RK4_sistemas(0,0,1,dy,dz,h)
'''

#PERGUNTA 6

'''
def f(x):
    return sqrt(1 + (1.5*exp(1.5*x))**2)

def simpson(a, b, h, f):

    n = int((b - a)/h)
    soma = f(a) + f(b)

    for i in range(1, n):
        if (i % 2 != 0):
            soma += 4 * f(a + i * h)
        else:
            soma += 2 * f(a + i * h)

    print("Valor do integral, pelo metodo de Simpson " + str((h/3)*soma))
    return (h/3)* soma

def trapezio(a, b, h, f):
    n = int((b - a) / h)

    soma = 0
    for i in range(1, n):
        soma += f(a + i * h)

    soma *= 2
    soma += (f(a) + f(b))

    print("Valor do integral, pelo metodo do trapezio " + str(soma * (h/2)))
    return soma * (h / 2)

h = 0.5
st = trapezio(0,2,h,f)
ss = simpson(0,2,h,f)
h /= 2
st1 = trapezio(0,2,h,f)
ss1 = simpson(0,2,h,f)
h *= 0.5
st2 = trapezio(0,2,h,f)
ss2 = simpson(0,2,h,f)

print("QC trapezio")
print((st1 - st) / (st2 - st1))
print()
print("QC simpson")
print((ss1 - ss) / (ss2 - ss1))
print()

print("ERRO TRAPEZIO:", (st2 - st1) / 3)
print("ERRO SIMPSON:", (ss2 - ss1) / 15)
'''
