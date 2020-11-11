#PERGUNTA 1

'''
def f(x,y):
    if (x == 0 and y == 0): return 1.1
    elif (x == 0 and y == 0.9): return 2.1
    elif (x == 0 and y == 1.8): return 6.3

    if (x == 0.9 and y == 0): return 1.4
    elif (x == 0.9 and y == 0.9): return 4.9
    elif (x == 0.9 and y == 1.8): return 1.5

    if (x == 1.8 and y == 0): return 2.6
    elif (x == 1.8 and y == 0.9): return 2.2
    elif (x == 1.8 and y == 1.8): return 1.2


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

            x = round(ax + j*hx, 3)
            y = round(ay + i*hy, 3)
            s += p*q * f(x, y)

    
    print("Resultado integral duplo, pelo metodo de simpson: " + str(hx * hy / 9 * s))
    return hx * hy / 9 * s 

double_simpson(0, 1.8, 0, 1.8, 2, 2, f)
'''
'''
#Alternativa
print(((0.9*0.9) / 9) * (6.3+4*1.5+1.2+4*2.1+16*4.9+4*2.2+1.1+4*1.4+2.6))
'''

#PERGUNTA 2

'''
#2.a)

def f1(y,z,w):
    return (y + z - w + 1) / 4.8

def f2(x,z,w):
    return (x - z + w -1) / 4.8

def f3(x,y,w):
    return (x - 2*y + w -1) / 4.8 

def f4(x,y,z):
    return  (-2*x + y + z) / 4.8   

def G_Seidel(f1,f2,f3,f4,x,y,z,w,erro):
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
        wtmp = w
        x = f1(y, z, w)
        y = f2(x, z, w)
        z = f3(x, y, w)
        w = f4(x, y, z)
        contador += 1
        print("Contador: " + str(contador) + "\tX: " + str(round(x,7)) + "\tY: " + str(round(y,7)) + "\tZ: " + str(round(z,7)) + "\tW: " + str(round(w,7)) )

#G_Seidel(f1,f2,f3,f4,0,0,0,0,0.001)

#2.b)
# Método converge porque em cada linha o elemento da diagonal principal é superior
#à soma do módulo dos restantes
'''

#PERGUNTA 3

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

m =[[0.7,8,3,12],
    [-6,0.45,-0.25,15],
    [8,-3.1,1.05,23]]

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

print("Solucoes:")
print(Gauss(m))

#CALCULO DE DELTA - estabilidade externa

#da = 0.5 e db = 0.5

#[db]   [da da da]   [x]
#[db] - [da da da] * [y]
#[db]   [da da da]   [z]

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

d =[[0.7,8,3, estabilidade_externa(0.5, Gauss(m))[0]],
    [-6,0.45,-0.25, estabilidade_externa(0.5, Gauss(m))[1]],
    [8,-3.1,1.05, estabilidade_externa(0.5, Gauss(m))[2]]]

#DELTA
delta = Gauss(d)
print("Estabilidade externa: " + str(delta))
'''


#PERGUNTA 4

'''
def QC(S,S1,S2):
    return abs((S1 - S)/(S2 - S1))

def f_p4(u,v):
    return u*(u/2 + 1)*v**3 +  (u + 5/2)*v**2

def Euler(xmin,xmax,x,y,f,h):
    """Calculo de Euler para equações diferenciais
    xmin, xmax: x menor e x maior
    x,y: X0 e Y0
    f: função para diferenciar
    h: distância entre dois pontos
    """
    for _ in range(0, round((xmax - xmin)/h)):
        y += h*f(x,y)
        x += h

    return y

def RK2(xmin,xmax,x,y,f,h):
    """Calculo de Runge-Kutta de 2º grau para equações diferenciais
    xmin, xmax: x menor e x maior
    x,y: X0 e Y0
    f: função para diferenciar
    h: distância entre dois pontos
    """
    for _ in range(0, round((xmax - xmin)/h)):
        y += h * f(x+h/2, y + h/2*f(x,y))
        x += h

    return y

def RK4(xmin,xmax,x,y,f,h):
    """Calculo de Runge-Kutta de 4º grau para equações diferenciais
    xmin, xmax: x menor e x maior
    x,y: X0 e Y0
    f: função para diferenciar
    h: distância entre dois pontos
    """
    for _ in range(0, round((xmax - xmin)/h)):
        dy1 = h*f(x,y)
        dy2 = h*f(x + h/2, y + dy1 / 2)
        dy3 = h*f(x + h/2, y + dy2 / 2)
        dy4 = h*f(x + h, y + dy3)
        y += 1/6*dy1 + 1/3*dy2 + 1/3*dy3 + 1/6*dy4
        x += h

    return y


def diferential(xmin,xmax,x,y,f,h, erro, Calc):
    """Cálculo de equações diferenciais de 1ª ordem
    xmin, xmax: x menor e x maior
    x,y: X0 e Y0
    f: função para diferenciar
    h: distância entre dois pontos
    erro: erro da solução
    Calc: Método para utilizar
    """
    contador = 1
    s = Calc(xmin,xmax,x,y,f,h)
    h /= 2

    s1 = Calc(xmin,xmax,x,y,f,h)
    print("h': " + str(h))
    h /= 2

    s2 = Calc(xmin,xmax,x,y,f,h)
    print("h'': " + str(h))
    h /= 2

    if (Calc(xmin,xmax,x,y,f,h) == Euler(xmin,xmax,x,y,f,h)):
        value = 2
    elif (Calc(xmin,xmax,x,y,f,h) == RK2(xmin,xmax,x,y,f,h)):
        value = 4
    elif (Calc(xmin,xmax,x,y,f,h) == RK4(xmin,xmax,x,y,f,h)):
        value = 16
    print(str(contador) + '\t  ' + str(round(s,6)) + '\t  ' + str(round(s1,6)) + '\t  ' + str(round(s2,6)) + '\t  ' + str(round(QC(s,s1,s2),6)) + '\t  ' + str(round(h,6)) + '\t ' + str(round(s2 - s1, 6)))
    while(abs(QC(s,s1,s2) - value) > erro):
        contador += 1
        s = s1
        s1 = s2
        s2 = Calc(xmin,xmax,x,y,f,h)
        h /= 2
        print(str(contador) + '\t  ' + str(round(s,6)) + '\t  ' + str(round(s1,6)) + '\t  ' + str(round(s2,6)) + '\t  ' + str(round(QC(s,s1,s2),6)) + '\t  ' + str(round(h,6)) + '\t ' + str(round(s2 - s1, 6)))


diferential(1,1.8,1,0.1,f_p4,0.08,0.01, Euler)
'''
