from math import pi, sin

def f(x):
    return x**3

#INTEGRAÇÃO PELO MÉTODO DO TRAPÉZIO
def trapezio(a, b, n, f):
    h = (b - a) / n

    soma = 0
    for i in range(1, n):
        soma += f(a + i * h)
    soma += (f(a) + f(b)) / 2

    return soma * h

print("Valor do integral, pelo metodo do trapezio " + str(trapezio(0, 2, 100, f)))

#CÁLCULO DO QUOCIENTE DE CONVERGÊNCIA PARA MÉTODO DO TRAPÉZIO
def qc(n):
    s = trapezio(0, 2, n, f)
    s1 = trapezio(0, 2, n*2, f)
    s2 = trapezio(0, 2, n*4, f)

    return (s1 - s) / (s2 - s1)

#---------------------------------Calculate QC and ERRORS------------------------------
# QC = (2n result - 1st result) / (3rd result - 2nd result) (Quociente de Convergência)
# QC = | (4.25 - 5) / (4.0625 - 4.25) | -> 4
# ERRO estimado = | (4.0625 - 4.25) / 3 | -> 0.0625
# ERRO obtido = | 4 - 4.0625 |
#--------------------------------------------------------------------------------------

#--------------TPC---------------------
#integrar x**2 * sin(x), entre 0 e pi/2

def f_1(x):
    return x**2 + sin(x)

print("Valor do integral TPC: " + str(trapezio(0, pi/2, 100, f_1)))
#--------------------------------------

#INTEGRAÇÃO PELO MÉTODO DE SIMPSON

def simpson(a, b, n, f):

    h = (b - a)/n
    soma = f(a) + f(b)

    for i in range(1, n):
        if (i % 2 != 0):
            soma += 4 * f(a + i * h)
        else:
            soma += 2 * f(a + i * h)

    return (h/3)* soma

print("Valor do integral, pelo metodo de Simpson " + str(simpson(0, 2, 100, f)))

#CÁLCULO DE INTEGRAL DUPLO COM MÉTODO DE SIMPSON - RESOLUÇÃO EM SALA DE AULA

def g(x):
    return x

def func(x, n):
    return simpson(0, 1, n, g) + g(x)

def double_simpson_class(a, b, n, f):
    h = (b - a)/n
    soma = f(a, n) + f(b, n)

    for i in range(1, n):
        if (i % 2 != 0):
            soma += 4 * f(a + i * h, n)
        else:
            soma += 2 * f(a + i * h, n)

    return (h/3)* soma

print("Resultado integral duplo, pelo metodo de simpson: " + str(double_simpson_class(0, 1, 10, func)))

#CÁLCULO DO INTEGRAL DUPLO PELO MÉTODO DE SIMPSON - ANÁLISE DE UM VÍDEO NO YOUTUBE

# y entre [-1,1] (por fora)
# x entre [1,2] (por dentro)

def f_2(x, y):
    return x**2*y + x*y**2

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

    return hx * hy / 9 * s 

print("Resultado integral duplo, pelo método de simpson: " + str(double_simpson(1, 2, -1, 1, 16, 14, f_2)))
        