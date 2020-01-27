#PERGUNTA 1

'''
def f(x):
    if x == 0: return 0.36
    elif x == 0.25: return 1.19
    elif x == 0.50: return 1.32
    elif x == 0.75: return 0.21
    elif x == 1.00: return 1.15
    elif x == 1.25: return 1.39
    elif x == 1.50: return 0.12
    elif x == 1.75: return 1.22
    elif x == 2.00: return 0.60

def simpson(a,b,n):
    h = (b-a) / n
    soma = 0

    for i in range(1,n):
        if (i % 2 != 0):
            soma += 4 * f(a + i*h)
        else:
            soma += 2 * f(a + i*h)

    soma += f(a) + f(b)

    return soma * (h/3)

print("Simpson integral value: " + str(simpson(0,2,8)))

#Cálculo do erro

n = 2
s = simpson(0,2,n)
n *= 2
s1 = simpson(0,2,n)
n *= 2
s2 = simpson(0,2,n)

print("ERRO: " + str((s2-s1)/15))
'''

#PERGUNTA 2

'''
def f1(y,z,w):
    return (1 + y + z - w) / 4.5
def f2(x,z,w):
    return (-1 + x - z + w) / 4.5
def f3(x,y,w):
    return (-1 + x - 2*y + w) / 4.5
def f4(x,y,z):
    return (-2*x + y + z) / 4.5

xtemp = 0.25
ytemp = 0.25
wtemp = 0.25
ztemp = 0.25

x = f1(ytemp, ztemp, wtemp)
y = f2(xtemp, ztemp, wtemp)
z = f3(xtemp, ytemp, wtemp)
w = f4(xtemp, ytemp, ztemp)

print("x: " + str(x))
print("y: " + str(y))
print("z: " + str(z))
print("w: " + str(w))

xtemp = x
ytemp = y
ztemp = z
wtemp = w

x = f1(ytemp, ztemp, wtemp)
y = f2(xtemp, ztemp, wtemp)
z = f3(xtemp, ytemp, wtemp)
w = f4(xtemp, ytemp, ztemp)

print()
print()

print("x: " + str(x))
print("y: " + str(y))
print("z: " + str(z))
print("w: " + str(w))
'''

#PERGUNTA 3

'''
[a,y]
'''

#PERGUNTA 4

'''
def dT(T):
    return -0.25 * (T - 45)

def Euler(T,t,h):
    for _ in range(2):
        T += h*dT(T)
        t += h
    return T

print(Euler(23, 1, 0.4))
'''

#PERGUNTA 5

'''
#Primeira equação
def dy(x,y,z):
    return z
#Segunda equação
def dz(x,y,z):
    return -7*z - 2*y
'''