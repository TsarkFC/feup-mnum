from math import exp, cos, sin, sqrt, log

#PERGUNTA 1

'''
def dT(t,T):
    return -0.25 * (T - 37)

def Euler(x, y, f, h):
    for _ in range(2):
        y += h*f(x,y)
        x += h
        print(x,y)

Euler(5,3,dT,0.4)
'''

#PERGUNTA 3

'''
m =[[1,0.5,1/3,-1],
    [1/2,1/3,1/4,1],
    [1/3,1/4,1/5,1]]

def Gauss(m):
    for diag in range(0,3):
        save = m[diag][diag]
        for col in range(0,4):
            m[diag][col] = m[diag][col] / save
        for lin in range(diag + 1, 3):
            save1 = m[lin][diag]
            for col in range(diag, 4):
                m[lin][col] = m[lin][col] - m[diag][col] * save1

    print("Matriz diagonalizada:")
    print(m)

    z = m[2][3]
    y = m[1][3] - z*m[1][2]
    x = m[0][3] - z*m[0][2] - y*m[0][1]

    print("Solucoes:")
    print([x,y,z])

    return [x,y,z]

res = Gauss(m)


def estabilidade_externa(erro, res):
    db = [erro, erro, erro]

    da = [[erro, erro, erro], 
          [erro, erro, erro],
          [erro, erro, erro]]

    final = []
    soma = 0

    for lin1 in range(len(da)):
        for lin2 in range(len(res)):
            soma += da[lin1][lin2] * res[lin2]

        final.append(db[lin1] - soma)
        soma = 0

    return final

p = estabilidade_externa(0.05, res)[0]

g =[[1,0.5,1/3,p],
    [1/2,1/3,1/4,p],
    [1/3,1/4,1/5,p]]

print()
Gauss(g)
'''

#PERGUNTA 4

'''
def f(x):
    return 2*log(2*x)

def picard(x, f):
    x = f(x)
    print(x)    

picard(1.1, f)
'''

#PERGUNTA 5

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
st = trapezio(0,1,h,f)
ss =simpson(0,1,h,f)
print()
h /= 2
st1 = trapezio(0,1,h,f)
ss1 = simpson(0,1,h,f)
print()
h /= 2
st2 = trapezio(0,1,h,f)
ss2 = simpson(0,1,h,f)
print()

print("QC trapezio")
print((st1 - st) / (st2 - st1))
print()
print("QC simpson")
print((ss1 - ss) / (ss2 - ss1))
print()

print("ERRO TRAPEZIO:", (st2 - st1) / 3)
print("ERRO SIMPSON:", (ss2 - ss1) / 15)
'''

#PERGUNTA 7

'''
def f(x):
    return x**3 - 10*sin(x) + 2.8

def erro_absoluto_bissecao(a,b,f):
    x = (a+b)/2
    for _ in range(2):
        if (f(a) * f(x) < 0):
            b = x
        else:
            a = x
        x = (a+b)/2

    print(b)
    return x

erro_absoluto_bissecao(1.5, 4.2, f)
'''