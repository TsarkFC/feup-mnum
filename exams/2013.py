from math import exp, cos, sin

#PERGUNTA 1

'''
def dy(t,y,z):
    return z

def dz(t,y,z):
    return 0.5 + t**2 + t*z

def Euler_sistemas(xmin,xmax,x,y,z,f,g,h):
    for _ in range(0, round((xmax - xmin)/h)):
        y1 = y + h*f(x,y,z)
        z += h*g(x,y,z)
        y = y1
        x += h  
        print("x", x)
        print("y", y)
        print()
    return (y,z)

h = 0.25
Euler_sistemas(0, 0.5, 0, 0, 1, dy, dz, h)

def RK4_sistemas(xmin,xmax,x,y,z,f,g,h):
    for _ in range(0, round((xmax - xmin)/h)):
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
        print("x", x)
        print("y", y)
        print()

    return (y,z)

h = 0.25
RK4_sistemas(0, 0.5, 0, 0, 1, dy, dz, h)
'''

#PERGUNTA 2

'''
Pergunta teórica sobre pivotagem
'''

#PERGUNTA 3

'''
def z(x,y):
    return 3*x**2 - x*y + 11*y + y**2 - 8*x

def zx(x,y):
    return 6*x - y -8

def zy(x,y):
    return -x + 11 + 2*y

def gradiente(x,y,erro,f,fx,fy,lamb):
    contador = 0

    print("Contador: ", contador)
    print("x: ",x, "\ty: ",y)
    print("f(x,y): ",f(x,y))
    print()
    print("Gradiente:")
    print(fx(x,y), fy(x,y))
    print()

    contador += 1

    x1 = x - lamb*fx(x,y)
    y1 = y - lamb*fy(x,y)

    print("Contador: ", contador)
    print("x: ",x1, "\ty: ",y1)
    print("f(x,y): ",f(x1,y1))
    print()
    print("Gradiente:")
    print(fx(x1,y1), fy(x1,y1))
    print()

gradiente(2,2,0.001,z,zx,zy,0.5)
'''

#PERGUNTA 4

'''
def f(x):
    return exp(1.5*x)

def simpson(a, b, h, f):

    soma = f(a) + f(b)
    n = (b - a) / h

    for i in range(1, int(n)):
        if (i % 2 != 0):
            soma += 4 * f(a + i * h)
        else:
            soma += 2 * f(a + i * h)

    print("Valor do integral, pelo metodo de Simpson " + str((h/3)*soma))
    return (h/3)* soma

h = 0.125
s = simpson(1, 1.5, h, f)
h /= 2
s1 = simpson(1, 1.5, h, f)
h /= 2
s2 = simpson(1, 1.5, h, f)

print("QC:")
print((s1-s)/(s2-s1))

print("ERRO:")
print((s2-s1)/15)
'''

#PERGUNTA 5

'''
def f(x):
    return (x -3.7) + (cos(x+1.2))**3

def df(x):
    return 1 - 3 * cos(x + 1.2)**2 * sin(x + 1.2)

def newton(x, func, func1):
	x -= func(x)/func1(x)
	print ("\nZero: " + str(x) + '\n')

newton(3.8, f, df)
'''
