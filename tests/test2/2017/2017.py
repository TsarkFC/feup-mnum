#PERGUNTA 1

'''
#MODULO VETOR
def modulo_vetor(lista):
    soma = 0
    for i in lista:
        soma += (i)**2
    return soma**(0.5)

#SUBTRACAO DE LISTAS
def dif_listas(l1, l2):
    res = []
    for i in range(len(l1)):
        res.append(l1[i] - l2[i])
    return res


def Gauss(m):
    for diag in range(0,3):
        save = m[diag][diag]
        for col in range(0,4):
            m[diag][col] = m[diag][col] / save
        for lin in range(diag + 1, 3):
            save1 = m[lin][diag]
            for col in range(diag, 4):
                m[lin][col] = m[lin][col] - m[diag][col] * save1

    z = m[2][3]
    y = m[1][3] - z*m[1][2]
    x = m[0][3] - z*m[0][2] - y*m[0][1]

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

res = [0.552949, -0.15347, -0.10655]

estabilidade_externa(0.1, res)

d = [[18, -1, 1, estabilidade_externa(0.1, res)[0]],
     [3, -5, 4, estabilidade_externa(0.1, res)[1]],
     [6, 8, 29, estabilidade_externa(0.1, res)[2]]]

print("Valores de estabilidade externa: " + str(Gauss(d)))
'''

#PERGUNTA 2

'''
def f1(y,z,w):
    return (25 - 0.5*y -3*z -0.25*w) / 6

def f2(x,z,w):
    return (10 - 1.2*x - 0.25*z - 0.2*w) / 3

def f3(x,y,w):
    return (7 + x - 0.25*y - 2*w) / 4

def f4(x,y,z):
    return (-12 - 2*x - 4*y - z) / 8

def G_Seidel(f1,f2,f3,f4,x,y,z,w,erro):
    xtmp = x + 100*erro
    ytmp = y + 100*erro
    ztmp = z + 100*erro
    wtmp = w + 100*erro
    contador = 0
    while((abs(x-xtmp) > erro) or (abs(y-ytmp) > erro) or (abs(z-ztmp) > erro) or (abs(w-wtmp) > erro)):
        xtmp = x
        ytmp = y
        ztmp = z
        wtmp = w
        x = f1(y, z, w)
        y = f2(x, z, w)
        z = f3(x, y, w)
        w = f4(x, y, z)
        contador += 1
        print("Contador: " + str(contador) + "\tX: " + str(round(x,5)) + "\tY: " + str(round(y,5)) + "\tZ: " + str(round(z,5)) + "\tW: " + str(round(w,5)) )

G_Seidel(f1, f2, f3, f4, 2.12687, 2.39858, 3.99517, -3.73040, 0.01)
'''

#PERGUNTA 3

'''
def f(x):
    if x == 0: return 1.04
    elif x == 0.25: return 0.37
    elif x == 0.5: return 0.38
    elif x == 0.75: return 1.49
    elif x == 1: return 1.08
    elif x == 1.25: return 0.13
    elif x == 1.5: return 0.64
    elif x == 1.75: return 0.84
    elif x == 2: return 0.12

def simpson(a, b, n, f):

    h = (b - a)/n
    soma = f(a) + f(b)

    for i in range(1, n):
        if (i % 2 != 0):
            soma += 4 * f(a + i * h)
        else:
            soma += 2 * f(a + i * h)
        
        print("S: " + str((h/3)*soma))

    return (h/3)* soma

#VALOR DO INTEGRAL
print("Valor do integral",simpson(0, 2, 8, f))

#ERRO PARA O MENOR PASSO DE INTEGRAÇÃO

n = 1
n *= 2
s = simpson(0, 2, n, f)
n *= 2
s1 = simpson(0, 2, n, f)
n *= 2
s2 = simpson(0, 2, n, f)

print ("ERRO: " + str((s2 - s1) / 15))
'''

#PERGUNTA 4

'''
def double_trapezio(table):
    soma = 0
    for i in range(len(table)):
        for j in range(len(table)):
            if (i == 0 or i == len(table) - 1) and (j == 0 or j == len(table) - 1):
                soma += table[i][j]
            elif (i == 0 or i == len(table) - 1) or (j == 0 or j == len(table) - 1):
                soma += 2*table[i][j]
            else:
                soma += 4*table[i][j]
    
    return soma / 4

print("Integral duplo: " + str(double_trapezio([[1.1, 1.4, 7.7],[2.1, 3.1, 2.2],[7.3, 1.5, 1.2]])))
'''

#PERGUNTA 6

'''
def dz(t,y,z):
    return 2 + t**2 + t*z

def dy(t,y,z):
    return z

def Euler_2(y,t,z,dz,h):
    print(str(0) + ": " + "T: " + str(t) + " Y: " + str(y))
    for i in range(0, 3):
        y += h*z
        z += h*dz(t,y,z)
        t += h
        print(str(i+1) + ": " + "T: " + str(t) + " Y: " + str(y))

    return (t,y)

print("EULER:")
Euler_2(1, 1, 0, dz, 0.25)

def RK4_2(x,y,z,f,g,h):
    print(str(0) + ": " + "T: " + str(x) + " Y: " + str(y))
    for j in range(0, 2):
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
        print(str(j+1) + ": " + "T: " + str(x) + " Y: " + str(y))
    return (y,z)

print()
print("RK4")
RK4_2(1,1,0,dy,dz,0.25) 
'''