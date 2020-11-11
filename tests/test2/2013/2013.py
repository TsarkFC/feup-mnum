from math import sin, sqrt, exp

#PROBLEMA 1

'''
def f1(y,z,w):
    return (1 + y + z - w) / 4.5
def f2(x,z,w):
    return (-1 + x - z + w) / 4.5
def f3(x,y,w):
    return (-1 + x - 2*y + w) / 4.5
def f4(x,y,z):
    return (-2*x + y + z) / 4.5

xt = 0.25
yt = 0.25
zt = 0.25
wt = 0.25

x = f1(yt,zt,wt)
y = f2(xt,zt,wt)
z = f3(xt,yt,wt)
w = f4(xt,yt,zt)

print("X: " + str(x))
print("Y: " + str(y))
print("Z: " + str(z))
print("W: " + str(w))
print()
print()

xt = x
yt = y
zt = z
wt = w

x = f1(yt,zt,wt)
y = f2(xt,zt,wt)
z = f3(xt,yt,wt)
w = f4(xt,yt,zt)

print("X: " + str(x))
print("Y: " + str(y))
print("Z: " + str(z))
print("W: " + str(w))
'''

#PROBLEMA 2

'''
def dx(x,t):
    return  sin(2*x) + sin(2*t) 

def RK4(xmin,xmax,x,y,f,h):
    print(y )
    for _ in range(0, round((xmax - xmin)/h)):
        dy1 = h*f(x,y)
        dy2 = h*f(x + h/2, y + dy1 / 2)
        dy3 = h*f(x + h/2, y + dy2 / 2)
        dy4 = h*f(x + h, y + dy3)
        y += 1/6*dy1 + 1/3*dy2 + 1/3*dy3 + 1/6*dy4
        x += h
        print(y)

    print()

    return y

#a)
h = 0.5
s = RK4(1,1.5,1,1,dx,h)
h /= 2
s1 = RK4(1,1.5,1,1,dx,h)
h /= 2
s2 = RK4(1,1.5,1,1,dx,h)

#b)
print("S: " + str(s))
print("S': " + str(s1))
print("S'': " + str(s2))
print((s1-s)/(s2-s1))

'''

#PERGUNTA 3

'''
def f(x):
    return sqrt(1 + (1.5 * exp(1.5*x))**2)

def trapezio(a, b, n, f):
    h = (b - a) / n

    soma = 0
    for i in range(1, n):
        soma += f(a + i * h)

    soma *= 2
    soma += (f(a) + f(b))

    return soma * (h / 2)

def simpson(a,b,n,f):
    h = (b - a) / n
    soma = 0

    for i in range(1,n):
        if (i % 2 != 0):
            soma += 4*f(a + i*h)
        else:
            soma += 2*f(a + i*h)

    soma += f(a) + f(b)

    return soma * (h/3)

n = 4
t = trapezio(0,1,n,f)
s = simpson(0,1,n,f)
print("t: " + str(t) + " s: " + str(s))

n *= 2
t1 = trapezio(0,1,n,f)
s1 = simpson(0,1,n,f)
print("t': " + str(t1) + " s': " + str(s1))

n *= 2
t2 = trapezio(0,1,n,f)
s2 = simpson(0,1,n,f)
print("t'': " + str(t2) + " s'': " + str(s2))

print("QC: " + str((s1-s)/(s2-s1)))
print("ERRO T: " + str((t2-t1)/3))
print("ERRO S: " + str((s2-s1)/3))
'''

#PERGUNTA 4

'''
def dc(t, c, T):
    return -exp(-0.5/(T+273)) * c

def dT(t, c, T):
    return 20 * exp(-0.5/(T+273)) * c - 0.5 * (T - 20) 

def Euler(c, T, t, tmin, tmax, h):
    print("t: " + str(t) + " c: " + str(c) + " T: " + str(T))
    for _ in range(round((tmax - tmin) / h)):
        Tt = T + h*dT(t,c,T)
        c += h*dc(t,c,T)
        t += h
        T = Tt
        print("t: " + str(t) + " c: " + str(c) + " T: " + str(T))
    return c
    
def RK4(c, T, t, tmin, tmax, h):
    print("t: " + str(t) + " c: " + str(c) + " T: " + str(T))
    for _ in range(0, round((tmax - tmin)/h)):
        dc1 = h*dc(t,c,T)
        dt1 = h*dT(t,c,T)
        dc2 = h*dc(t + h/2, c + dc1 / 2, T + dt1/2)
        dt2 = h*dT(t + h/2, c + dc1 / 2, T + dt1/2)
        dc3 = h*dc(t + h/2, c + dc2 / 2, T + dt2/2)
        dt3 = h*dT(t + h/2, c + dc2 / 2, T + dt2/2)
        dc4 = h*dc(t + h, c + dc3, T + dt3)
        dt4 = h*dT(t + h, c + dc3, T + dt3)
        c += 1/6*dc1 + 1/3*dc2 + 1/3*dc3 + 1/6*dc4
        T += 1/6*dt1 + 1/3*dt2 + 1/3*dt3 + 1/6*dt4
        t += h
        print("t: " + str(t) + " c: " + str(c) + " T: " + str(T))
    return c   

print("EULER")
Euler(2,20,0,0,0.4,0.2)
print("RK4")
RK4(2,20,0,0,0.4,0.2)

h = 0.2
s = Euler(2,20,0,0,0.4,h)
h /= 2
s1 = Euler(2,20,0,0,0.4,h)
h /= 2
s2 = Euler(2,20,0,0,0.4,h)

print("s: " + str(s))
print("s': " + str(s1))
print("s'': " + str(s2))

print("QC: " + str((s1-s)/(s2-s1)))
print("ERRO: " + str(s2-s1))
'''