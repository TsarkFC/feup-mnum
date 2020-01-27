from math import sqrt, cos, sin, exp, log

#PERGUNTA 1

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

    while (b-a > 0.001):

        if (f(c) < f(d)):
            b = d
        elif (f(c) > f(d)):
            a = c

        d = a + ((sqrt(5)-1)/2) * (b-a)
        c = a + (1 - (sqrt(5)-1)/2) * (b-a)

    return (a + b) / 2

print(optimized_golden(f, 0.001, 4), f(optimized_golden(f, 0.001, 4)))

def lm(x,y,erro,a,delta,f,fx,fy,fxx,fyy,fxy,fyx):
    contador = 1
    x1 = x - (a*fx(x,y) + 1/h(x,y,fxx,fyy,fxy,fyx)*fx(x,y))
    y1 = y - (a*fy(x,y) + 1/h(x,y,fxx,fyy,fxy,fyx)*fy(x,y))
    while(abs(x1 - x) > erro or abs(y1 - y) > erro):
        if (f(x1,y1) > f(x,y)):
            a += delta
        else:
            a -= delta
        x = x1
        y = y1
        x1 = x - (a*fx(x,y) + 1/h(x,y,fxx,fyy,fxy,fyx)*fx(x,y))
        y1 = y - (a*fy(x,y) + 1/h(x,y,fxx,fyy,fxy,fyx)*fy(x,y))
    print("Contador: ", contador)
    print("x: ",x1, "\ty: ",y1)
    print("f(x,y): ",f(x,y))
'''

#PERGUNTA 2

'''
def f(x):
    return sqrt(1 + (2.5 * exp(2.5*x))**2)

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

h = 0.125
ss =simpson(0,1,h,f)
st = trapezio(0,1,h,f)
print()

h /= 2
ss1 = simpson(0,1,h,f)
st1 = trapezio(0,1,h,f)
print()

h /= 2
ss2 = simpson(0,1,h,f)
st2 = trapezio(0,1,h,f)
print()

print("QC trapezio: ", (st1-st)/(st2-st1))
print("QC simpson: ", (ss1-ss)/(ss2-ss1))

print("ERRO TRAPEZIO:", (st2 - st1) / 3)
print("ERRO SIMPSON:", (ss2 - ss1) / 15)
'''

#PERGUNTA 3

''' intervalos de isolamento [-5,-4], [1,2] '''

'''1a expressão converge para a raíz negativa e a segunda para a positiva'''

'''
def f1(x):
    return exp(x) - 5

def df1(x):
    return exp(x)

def f2(x):
    return log(5+x)

def df2(x):
    return 1 / (5+x)

def g(x):
    return exp(x)-x-5

def dg(x):
    return exp(x) - 1

def picard(x,erro, func):
    temp = x
    x = func(temp)
    contador = 1
    print(str(contador) + '\t' + str(x) + '\t' + str(temp))
    while (abs(x - temp) > erro):
        contador += 1
        temp = x
        x = func(temp)
        print(str(contador) + '\t' + str(x) + '\t' + str(temp))

    print ("Zero: " + str(x) + '\n')

def newton(x,erro, func, func1):
    temp = x + 2*erro
    contador = 0
    while (abs(temp-x) > erro):
        temp = x
        xl = x
        xl -= func(x) / func1(x)
        x = xl
        contador += 1

        print(contador, x)

print("F1")
picard(-3,0.0001,f1)
print()
newton(-3,0.0001,g, dg)

print()
print("F2")
picard(2,0.0001,f2)
print()
newton(2,0.0001,g, dg)
'''

#PERGUNTA 4

'''
def dC(t,T,C):
    return -exp(-0.5 / (T + 273)) * C

def dT(t,T,C):
    return 30 * exp(-0.5 / (T + 273)) * C - 0.5*(T-20)

def Euler_sistemas(xmin,xmax,x,y,z,f,g,h):
    print("t", x)
    print("T", y)
    print("C", z)
    for _ in range(0, round((xmax - xmin)/h)):
        y1 = y + h*f(x,y,z)
        z += h*g(x,y,z)
        y = y1
        x += h
        print("t", x)
        print("T", y)
        print("C", z)
    return y

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
        print("t", x)
        print("T", y)
        print("C", z)

    return y

h = 0.25
t = Euler_sistemas(0, 0.5, 0, 25, 2.5, dT, dC, h)
print()
RK4_sistemas(0, 0.5, 0, 25, 2.5, dT, dC, h)

h /= 2
t1 = Euler_sistemas(0, 0.5, 0, 25, 2.5, dT, dC, h)

h /= 2
t2 = Euler_sistemas(0, 0.5, 0, 25, 2.5, dT, dC, h) 

print("QC: ", (t1-t)/(t2-t1))
print("ERRO:", t2-t1)
'''

#PERGUNTA 5

'''
def w(x,y):
    return -1.1*x*y + 12*y + 7*x**2 - 8*x

def wx(x,y):
    return -1.1*y + 14*x - 8

def wy(x,y):
    return  -1.1*x + 12

def gradiente(x,y,f,fx,fy,lamb):
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

gradiente(3,1,w,wx,wy,0.1)
'''