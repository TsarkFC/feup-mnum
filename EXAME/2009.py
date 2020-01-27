from math import sin, cos, sqrt

#PERGUNTA 1
#Cálcular o zero de f(x) = (x - 2.6) + (cos(x + 1.1))**3
#Com base no método de newton (1ª iteração) e partindo de x = 1.8

'''
def f(x):
    return (x - 2.6) + (cos(x + 1.1))**3

def f1(x):
    return 1 + 3 * (cos(x + 1.1))**2 * (-sin(x + 1.1))

def newton(x,erro, func, func1):
	x -= func(x)/func1(x)
	print ("\n1a iteração: " + str(x) + '\n')

newton(1.8, 0.0001, f, f1)
'''

#PERGUNTA 2
#PERGUNTA TEÓRICA SOBRE MÉTODO DE NEWTON

'''
Optaria pela opção a), uma vez que tem uma derivada menos complexa sendo o número de cálculos
algébricos a realizar menor, o que leva a um menor erro

'''

#PERGUNTA 3
#Resolver um sistemas de equações pelo método de eliminação de Gauss

'''
m =[[0.1,0.5,3,0.25,0],
    [1.2,0.2,0.25,0.2,1],
    [-1,0.25,0.3,2,2],
	[2,0.00001,1,0.4,3]]

def Gauss(m,n):
    for diag in range(0,n):
        save = m[diag][diag]
        for col in range(0,n+1):
            m[diag][col] = m[diag][col] / save
        for lin in range(diag + 1, n):
            save1 = m[lin][diag]
            for col in range(diag, n+1):
                m[lin][col] = m[lin][col] - m[diag][col] * save1

    #Alínea a)
    print("Matriz diagonalizada:")
    print(m)

    w = m[3][4]
    z = m[2][4] - w*m[2][3]
    y = m[1][4] - w*m[1][3] - z*m[1][2]
    x = m[0][4] - w*m[0][3] - z*m[0][2] - y*m[0][1]

    #Alínea b)
    print("Solucoes:")
    print([x,y,z,w])

    return [x,y,z,w]
	
s = Gauss(m,4)

#Alínea c)

#[db]   [da da da]   [x]
#[db] - [da da da] * [y]
#[db]   [da da da]   [z]

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

d =[[0.1,0.5,3,0.25,estabilidade_externa(0.5, s)[0]],
    [1.2,0.2,0.25,0.2,estabilidade_externa(0.5, s)[1]],
    [-1,0.25,0.3,2,estabilidade_externa(0.5, s)[2]],
	[2,0.00001,1,0.4,estabilidade_externa(0.5, s)[3]]]

sol = Gauss(d, 4)

print("Estabilidade externa")
print(sol)

'''

#PERGUNTA 4


'''
def f(x):
    return 5 * cos(x) - sin(x)

def optimized_golden(f, a, b):

    #GOLDEN SECTION
    print("a = " + str(a) + "   f(a)" + str(f(a)))
    print("b = " + str(b) + "   f(b)" + str(f(b)))
    d = a + ((sqrt(5)-1)/2) * (b-a)
    c = a + (1-(sqrt(5)-1)/2) * (b-a)
    print("c = " + str(c) + "   f(c)" + str(f(c)))
    print("d = " + str(d) + "   f(d)" + str(f(d)))
    print()

    while (b-a > 0.0001):

        if (f(c) < f(d)):
            b = d
        elif (f(c) > f(d)):
            a = c

        d = a + ((sqrt(5)-1)/2) * (b-a)
        c = a + (1-(sqrt(5)-1)/2) * (b-a)

        print("a = " + str(a) + "\t" + "f(a)" + str(f(a)))
        print("b = " + str(b) + "\t" + "f(b)" + str(f(b)))
        print("c = " + str(c) + "   f(c)" + str(f(c)))
        print("d = " + str(d) + "   f(d)" + str(f(d)))
        print()

    return (a + b) / 2

print(optimized_golden(f, 2, 4))
'''


#PERGUNTA 5

#dx / dt = sin(x) + sin(2*t)

'''
def f(t,x):
    return sin(x) + sin(2*t)

def RK4(xmin,xmax,x,y,f,h):
    for _ in range(0, round((xmax - xmin)/h)):
        dy1 = h*f(x,y)
        dy2 = h*f(x + h/2, y + dy1 / 2)
        dy3 = h*f(x + h/2, y + dy2 / 2)
        dy4 = h*f(x + h, y + dy3)
        y += 1/6*dy1 + 1/3*dy2 + 1/3*dy3 + 1/6*dy4
        x += h
        print(y)

    return y

#Alínea a)

h = 0.5
print("1a")
s = RK4(1,1.5,1,1,f,h)
h /= 2
print("2a")
s1 = RK4(1,1.5,1,1,f,h)
h /= 2
print("3a")
s2 = RK4(1,1.5,1,1,f,h)

#Alínea b)
print()
print((s1-s)/(s2-s1))
'''

#PERGUNTA 6

'''
#Alínea b)
print((5.27-5.18) / (5.235-5.27))

#Alínea e)
print((5.235-5.27)/3)
'''

'''
def f(x):
    return 5*cos(x) - sin(x)

def otimizacao_unidimensional(x1,x2,erro,min):
    contador = 0
    number = (sqrt(5)-1)/2
    x3 = x1 + number**2 * (x2 - x1)
    x4 = x1 + number * (x2 - x1)
    print("x1 x2")
    print(x1,x2)
    print("x3 x4")
    print(x3,x4)

    while(abs(x2-x1) > erro):
        contador += 1
        if (min == True):
            if (f(x3) < f(x4)): 
                x2 = x4
            else:
                x1 = x3
        else:
            if (f(x3) > f(x4)): 
                x2 = x4
            else:
                x1 = x3

        x3 = x1 + number**2 * (x2 - x1)
        x4 = x1 + number * (x2 - x1)

        print("x1 x2")
        print(x1,x2)
        print("x3 x4")
        print(x3,x4)

    if (min == True):
        if (f(x1) < f(x2)):
            print(x1,f(x1))
        else:
            print(x2,f(x2))
    else:
        if (f(x1) > f(x2)):
            print(x1,f(x1))
        else:
            print(x2,f(x2))

otimizacao_unidimensional(2,4,0.001,True)
'''
