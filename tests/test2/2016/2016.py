from math import exp

#PROBLEMA 1


def dc(t,c,tem):
    return -exp((-0.5)/(tem+273)) * c

def dt(t,c,tem):
    return 20 * exp((-0.5)/(tem+273)) * c - 0.5 *(tem-20)

def Euler_2(t,c,tem,step,tmax,tmin):
    print(str(0) + ": t: " + str(t) + " c: "+ str(c) + " T: " +str(tem))
    for i in range(round((tmax-tmin)/step)):
        tem1 = tem + step*dt(t,c,tem)
        c += step*dc(t,c,tem)
        t += step
        tem = tem1

        print(str(i+1) + ": t: " + str(t) + " c: "+ str(c) + " T: " +str(tem))

    return c

print("EULER:")
Euler_2(0,1,15,0.25,0.5,0)

def RK4_2(t,c,tem,step):
    print("0:\tt: " + str(t) + "\tc: " + str(c) + "\tT: " + str(tem))
    for i in range(2):
        dc1 = step * dc(t,c,tem)
        dt1 = step * dt(t,c,tem)
        dc2 = step * dc(t + step/2, c + dc1/2, tem + dt1/2)
        dt2 = step * dt(t + step/2, c + dc1/2, tem + dt1/2)
        dc3 = step * dc(t + step/2, c + dc2/2, tem + dt2/2)
        dt3 = step * dt(t + step/2, c + dc2/2, tem + dt2/2)
        dc4 = step * dc(t + step, c + dc3, tem + dt3)
        dt4 = step * dt(t + step, c + dc3, tem + dt3)

        c += dc1/6 + dc2/3 + dc3/3 + dc4/6
        tem += dt1/6 + dt2/3 + dt3/3 + dt4/6
        t += step
        print(str(i+1) + ":\tt: " + str(t) + "\tc: " + str(c) + "\tT: " + str(tem))

print("RK4:")
RK4_2(0,1,15,0.25)
print()

#Alínea c)

h = 0.25
s = Euler_2(0,1,15,h,0.5,0)
h /= 2
s1 = Euler_2(0,1,15,h,0.5,0)
h /= 2
s2 = Euler_2(0,1,15,h,0.5,0)


print("Ch1: " + str(s1))
print("Ch2: " + str(s2))
print("QC: " + str((s1-s) / (s2-s1)))
print("ERRO: " + str(s2 - s1))


#PROBLEMA 2

'''
def f(x):
    if x == 0: return 0.18
    elif x == 0.20: return 0.91
    elif x == 0.40: return 0.83
    elif x == 0.60: return 1.23
    elif x == 0.80: return 0.88
    elif x == 1.0: return 1.37
    elif x == 1.20: return 0.8
    elif x == 1.40: return 1.34
    elif x == 1.60: return 0.43 

def simpson(a, b, n, f):

    h = (b - a)/n
    soma = f(a) + f(b)

    for i in range(1, n):
        if (i % 2 != 0):
            soma += 4 * f(round(a + i * h, 2))
        else:
            soma += 2 * f(round(a + i * h, 2))

    print("Valor do integral, pelo metodo de Simpson " + str((h/3)*soma))
    return (h/3)* soma

simpson(0, 1.6, 8, f)

#CÁLCULO DO ERRO ESTIMADO PARA CADA SOLUÇÃO

n = 1
n *= 2
s = simpson(0, 1.6, n, f)
n *= 2
s1 = simpson(0, 1.6, n, f)
n *= 2
s2 = simpson(0, 1.6, n, f)

print("ERRO: ", str((s2-s1)/15))
'''

#PERGUNTA 3
'''
Estratégias para garantir um determinado erro absoluto máximo no cálculo numérico de um integral definido
(???)

'''

#PROBLEMA 4

'''
def dT(T):
    return -0.25 * (T - 42)

def Euler(t, T, h):
    for _ in range(2):
        T += h * dT(T)
        t += h
    
    return T

print("Resultado: " + str(Euler(5,10,0.4)))
'''

#PERGUNTA 5

'''
def f1(y,z,w):
    return (2.5 - 0.5*y - 3*z - 0.25*w) / 6
def f2(x,z,w):
    return (3.8 - 1.2*x - 0.25*z - 0.2*w) / 3
def f3(x,y,w):
    return (10 + x - 0.25*y - 2*w) / 4
def f4(x,y,z):
    return (7 - 2*x - 4*y - z) / 8

def G_Seidel(x,y,z,w,erro):
    """Resolver sistemas de 3 equações usando o método Gauss-Seidel
    f1: 1ºa equação em função de y e z
    f2: 2ºa equação em função de x e z
    f3: 3ºa equação em função de x e y
    x, y, z: X0,Y0,Z0
    erro: erro da solução
    """
    xtmp = x + 100*erro
    ytmp = y + 100*erro
    ztmp = z + 100*erro
    wtmp = w + 100*erro
    contador = 0
    while((abs(x-xtmp) > erro) or (abs(y-ytmp) > erro) or (abs(z-ztmp) > erro) or (abs(w-wtmp) > erro)):
        xtmp = x
        ytmp = y
        ztmp = z
        x = f1(y, z, w)
        y = f2(x, z, w)
        z = f3(x, y, w)
        w = f4(x, y, z)
        contador += 1
        print("Contador: " + str(contador) + "\tX: " + str(round(x,7)) + "\tY: " + str(round(y,7)) + "\tZ: " + str(round(z,7)) + "\tW: " + str(round(w,7) ))

G_Seidel(0,0,0,0,0.01)
'''
