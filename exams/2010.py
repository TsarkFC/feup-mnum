from math import log, sin, cos

#PERGUNTA 1

'''
Calcular as derivadas no máxima e verificar se |f'(x)| < 1 nos pontos assinalados
'''

#PERGUNTA 2

#Uma iteração do método Picard-Peano

'''
def f(x):
    return 2 * log(2*x)

def picardi(x, func):
    temp = x
    x = func(temp)
    print(x)
    return

picardi(0.9, f)
'''

#PERGUNTA 2.3
'''
print("Resíduo")
print(1.17557-0.9)
'''
#PERGUNTA 3

#RESOLUÇÃO DE UMA EQUAÇÃO DIFERENCIAL DE 1ª ORDEM COM O MÉTODO RK4

'''
def dx(t,x):
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

h = 0.5
print("1a")
s = RK4(1,1.5,1,0,dx,h)
h /= 2
print("2a")
s1 = RK4(1,1.5,1,0,dx,h)
h /= 2
print("3a")
s2 = RK4(1,1.5,1,0,dx,h)

print()
print ("QC")
print((s1-s)/(s2-s1))

#Voltar a dividir h''

'''

#PERGUNTA 4

'''
Resolvida diretamente
'''

#PERGUNTA 5

'''
def f(x,y):
    return 6*x**2 - x*y + 12*y + y**2 - 8*x

def fx(x,y):
    return 12*x - y - 8

def fy(x,y):
    return -x + 12 + 2*y

def gradiente(x,y,erro,f,fx,fy):
    contador = 0

    print("Contador: ", contador)
    print("x: ",x, "\ty: ",y)
    print("f(x,y): ",f(x,y))
    print()
    print("Gradiente:")
    print(fx(x,y), fy(x,y))
    print()

    contador += 1
    h = 0.25
    x1 = x - h*fx(x,y)
    y1 = y - h*fy(x,y)
    print("Contador: ", contador)
    print("x: ",x1, "\ty: ",y1)
    print("f(x,y): ",f(x1,y1))
    print()
    print("Gradiente:")
    print(fx(x1,y1), fy(x1,y1))
    print()

gradiente(0,0,0.001,f,fx,fy)
'''

#PERGUNTA 6

'''
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

g = estabilidade_externa(0.1, [0.552949, -0.15347, -0.10655])

m = [[18,-1,1,g[0]],
     [3,-5,4,g[1]],
     [6,8,29,g[2]]]

Gauss(m)
'''