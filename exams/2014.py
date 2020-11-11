from math import cos, sin, sqrt

#PERGUNTA 1

'''
Passo de integração: ver frequência dos pontos do gráfico no eixo dos x

x(0) = 1, por análise do gráfico
'''

'''
Teste para k, substituir valor 20 por 5 e 40 para comparar
'''

'''
def dx(t,x,z):
    return z

def dz(t,x,z):
    return (-20*x - z) / 20 

def Euler_sistemas(xmin,xmax,x,y,z,f,g,h):
    for _ in range(0, round((xmax - xmin)/h)):
        y1 = y + h*f(x,y,z)
        z += h*g(x,y,z)
        y = y1
        x += h
        print((x,y,z))

h = 0.1
Euler_sistemas(0, 1.7, 0, 1, 0, dx, dz, h)
'''

#PERGUNTA 2

'''
3 zeros, desenhar gráficos no máxima
'''

'''
def f(x):
    return -x + 40 * cos(sqrt(x)) + 3

def df(x):
    return (-20 * sin(sqrt(x))) / sqrt(x) - 1

def newton(x, func, func1):
    print(x, func(x))
    for _ in range(2):
        x -= func(x) / func1(x)  
        print(x, func(x))

newton(1.7, f, df)
'''

#PERGUNTA 3

'''
m = [[0.1, 0.5, 3, 0.25, 0],
     [1.2, 0.2, 0.25, 0.2, 1],
     [-1, 0.25, 0.3, 2, 2],
     [2, 0.00001, 1, 0.4, 3]]

def Gauss(m):
    for diag in range(0,4):
        save = m[diag][diag]
        for col in range(0,5):
            m[diag][col] = m[diag][col] / save
        for lin in range(diag + 1, 4):
            save1 = m[lin][diag]
            for col in range(diag, 5):
                m[lin][col] = m[lin][col] - m[diag][col] * save1

    print("Matriz diagonalizada:")
    print(m)

    w = m[3][4]
    z = m[2][4] - w*m[2][3]
    y = m[1][4] - w*m[1][3] - z*m[1][2]
    x = m[0][4] - w*m[0][3] - z*m[0][2] - y*m[0][1] 

    print("Solucoes:")
    print([x,y,z,w])

    return [x,y,z,w]

Gauss(m)

def estabilidade_externa(erro, res):
    db = [erro, erro, erro, erro]

    da = [[erro, erro, erro, erro], 
          [erro, erro, erro, erro],
          [erro, erro, erro, erro],
          [erro, erro, erro, erro]]

    final = []
    soma = 0

    for lin1 in range(len(da)):
        for lin2 in range(len(res)):
            soma += da[lin1][lin2] * res[lin2]

        final.append(db[lin1] - soma)
        soma = 0

    return final

est = estabilidade_externa(0.3, Gauss(m))[0]

e = [[0.1, 0.5, 3, 0.25, est],
     [1.2, 0.2, 0.25, 0.2, est],
     [-1, 0.25, 0.3, 2, est],
     [2, 0.00001, 1, 0.4, est]]

print("Estabilidade")
Gauss(e)
'''

#PERGUNTA 4
'''
R = 10 e m = 2
'''

'''
def f1(x):
    return x**2 - 10

def df1(x):
    return 2*x

def f2(x):
    return 1 - 10/x**2

def df2(x):
    return 20 / x**3

def newton(x,erro, func, func1):
	temp = x + 10**10 * erro
	contador = 0
	while (abs(temp - x) > erro):
		temp = x
		x -= func(x)/func1(x)
		contador += 1
		print(str(contador) + '\t x = ' + str(x))
	print ("\nZero: " + str(x) + '\n')

newton(6, 0.001, f1, df1)
print()
print() 
#segundo método gasta muito mais iterações
print()
print()
newton(6, 0.001, f2, df2)
'''

#PERGUNTA 5

'''
def f(x):
    return 5 * cos(x) - sin(x)

def optimized_golden(f, a, b):

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

optimized_golden(f, 2, 4)
'''

#PERGUNTA 7

'''
def f(x):
    return (4*x**3 - x + 3)**(1/4)

def picardi(x, func):
    temp = x
    x = func(temp)
    contador = 1
    print(str(contador) + '\t' + str(x) + '\t' + str(temp))
    for _ in range(2):
        contador += 1
        temp = x
        x = func(temp)
        print(str(contador) + '\t' + str(x) + '\t' + str(temp))

picardi(3.5, f)
'''
