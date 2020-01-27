import math

######################################################################################################
#######################             GAUSS METHOD AND ERRORS             ##############################
######################################################################################################

m =[[7,3,1,24],
    [11,13,3,64],
    [3,11,17,56]]

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

#Cálculo de resíduos
#Cálculo da distribuição do resíduo pelas soluções
result = [24,64,56]

m1 =[[7,3,1],
    [11,13,3],
    [3,11,17]]

m2 = [2.05,3.2,0.89]

def residuo_gauss(m1, m2, result):
    soma = 0
    residuo = []
    ind = 0

    for lin1 in range(len(m1)):
        for lin2 in range(len(m2)):
            soma += m1[lin1][lin2] * m2[lin2]
        residuo.append(soma - result[ind]) #gives residual values
        #lista.append(soma) # gives multiplication result
        soma = 0
        ind += 1
    print("Residuo:")
    print(residuo)
    return residuo


######################################################################################################
#############################           ESTABILIDADE EXTERNA             #############################
######################################################################################################

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

######################################################################################################
###################################             QC             #######################################
######################################################################################################

def QC(S,S1,S2):
    return abs((S1 - S)/(S2 - S1))


######################################################################################################
#######################                GAUSS JACOBI             ######################################
######################################################################################################

def G_Jacobi(f1,f2,f3,x,y,z, erro):
    xtmp = x + 100*erro
    ytmp = y + 100*erro
    ztmp = z + 100*erro
    contador = 0
    while((abs(x-xtmp) > erro) or (abs(y-ytmp) > erro) or (abs(z-ztmp) > erro)):
        xtmp = x
        ytmp = y
        ztmp = z
        x = f1(ytmp, ztmp)
        y = f2(xtmp, ztmp)
        z = f3(xtmp, ytmp)
        contador += 1
        print("Contador: " + str(contador) + "\tX: " + str(round(x,7)) + "\tY: " + str(round(y,7)) + "\tZ: " + str(round(z,7)) )


######################################################################################################
#######################                 GAUSS SEIDEL                    ##############################
######################################################################################################


def G_Seidel(f1,f2,f3,x,y,z,erro):
    xtmp = x + 100*erro
    ytmp = y + 100*erro
    ztmp = z + 100*erro
    contador = 0
    while((abs(x-xtmp) > erro) or (abs(y-ytmp) > erro) or (abs(z-ztmp) > erro)):
        xtmp = x
        ytmp = y
        ztmp = z
        x = f1(y, z)
        y = f2(x, z)
        z = f3(x, y)
        contador += 1
        print("Contador: " + str(contador) + "\tX: " + str(round(x,7)) + "\tY: " + str(round(y,7)) + "\tZ: " + str(round(z,7)) )


######################################################################################################
#############################             TRAPEZIO INTEGRAL             ##############################
######################################################################################################

def trapezio(a, b, n, f):
    h = (b - a) / n

    soma = 0
    for i in range(1, n):
        soma += f(a + i * h)

    soma *= 2
    soma += (f(a) + f(b))

    print("Valor do integral, pelo metodo do trapezio " + str(soma * (h/2)))
    return soma * (h / 2)

######################################################################################################
#############################             TRAPEZIO INTEGRAL (QC)        ##############################
######################################################################################################

def trapezio_qc(left, right, f, erro):
    contador = 1
    n = 2
    h = (right - left) / n
    s = f(left)
    s1 = f(left)
    s2 = f(left)
    for i in range(1,n):
        s += 2*f(i*h)
    s = (s + f(right))* h/2
    n *= 2
    h = (right - left) / n
    for i in range(1,n):
        s1 += 2*f(i*h)
    s1 = (s1 + f(right))* h/2
    n *= 2
    h = (right - left) / n
    for i in range(1,n):
        s2 += 2*f(i*h)
    s2 = (s2 + f(right)) * h/2
    print("Contador: " + str(contador) + "\tS: " + str(round(s,7)) + "\tS1: " + str(round(s1,7)) + "\tS2: " + str(round(s2,7)))
    while (abs(abs((s1-s)/(s2-s1)) - 4) > erro):
        s = s1
        s1 = s2
        s2 = f(left)
        n *= 2
        h = (right - left) / n
        for i in range(1,n):
            s2 += 2*f(i*h)
        s2 = (s2 + f(right)) * h/2
        print("Contador: " + str(contador) + "\tS: " + str(round(s,7)) + "\tS1: " + str(round(s1,7)) + "\tS2: " + str(round(s2,7)))

######################################################################################################
#############################             TRAPEZIO INTEGRAL (QC)        ##############################
######################################################################################################

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

######################################################################################################
#############################             SIMPSON INTEGRAL        ####################################
######################################################################################################

def simpson(a, b, n, f):

    h = (b - a)/n
    soma = f(a) + f(b)

    for i in range(1, n):
        if (i % 2 != 0):
            soma += 4 * f(a + i * h)
        else:
            soma += 2 * f(a + i * h)

    print("Valor do integral, pelo metodo de Simpson " + str((h/3)*soma))
    return (h/3)* soma

######################################################################################################
#############################             SIMPSON DOUBLE INTEGRAL        #############################
######################################################################################################

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

    
    print("Resultado integral duplo, pelo método de simpson: " + str(hx * hy / 9 * s))
    return hx * hy / 9 * s 

######################################################################################################
#############################             SIMPSON INTEGRAL (QC)        ###############################
######################################################################################################


def simpson_qc(f,left,right,erro):
    contador = 1
    n = 1
    n *= 2
    s = simpson(left, right, n, f)
    n *= 2
    s1 = simpson(left, right, n, f)
    n *= 2
    s2 = simpson(left, right, n, f)
    print("Contador: " + str(contador) + "\tS: " + str(round(s,15)) + "\tS1: " + str(round(s1,15)) + "\tS2: " + str(round(s2,15)))
    while (abs(abs((s1-s)/(s2-s1)) - 16) > erro):
        contador += 1
        s = s1
        s1 = s2
        n *= 2
        s2 = simpson(left, right, n, f)
        print("Contador: " + str(contador) + "\tS: " + str(round(s,15)) + "\tS1: " + str(round(s1,15)) + "\tS2: " + str(round(s2,15)))
        

######################################################################################################
##################             EQUAÇÕES DIFERENCIAIS PRIMEIRA ORDEM              #####################
######################################################################################################

def Euler(xmin,xmax,x,y,f,h):
    for _ in range(0, round((xmax - xmin)/h)):
        y += h*f(x,y)
        x += h

    return y


def RK2(xmin,xmax,x,y,f,h):
    for _ in range(0, round((xmax - xmin)/h)):
        y += h * f(x+h/2, y + h/2*f(x,y))
        x += h

    return y

def RK4(xmin,xmax,x,y,f,h):
    for _ in range(0, round((xmax - xmin)/h)):
        dy1 = h*f(x,y)
        dy2 = h*f(x + h/2, y + dy1 / 2)
        dy3 = h*f(x + h/2, y + dy2 / 2)
        dy4 = h*f(x + h, y + dy3)
        y += 1/6*dy1 + 1/3*dy2 + 1/3*dy3 + 1/6*dy4
        x += h

    return y

def diferential(xmin,xmax,x,y,f,h, erro, Calc):
    contador = 1
    s = Calc(xmin,xmax,x,y,f,h)
    h /= 2

    s1 = Calc(xmin,xmax,x,y,f,h)
    h /= 2

    s2 = Calc(xmin,xmax,x,y,f,h)
    h /= 2
    if (Calc(xmin,xmax,x,y,f,h) == Euler(xmin,xmax,x,y,f,h)):
        value = 2
    elif (Calc(xmin,xmax,x,y,f,h) == RK2(xmin,xmax,x,y,f,h)):
        value = 4
    elif (Calc(xmin,xmax,x,y,f,h) == RK4(xmin,xmax,x,y,f,h)):
        value = 16
    print(str(contador) + '\t  ' + str(round(s,5)) + '\t  ' + str(round(s1,5)) + '\t  ' + str(round(s2,5)) + '\t  ' + str(round(QC(s,s1,s2),2)))
    while(abs(QC(s,s1,s2) - value) > erro):
        contador += 1
        s = s1
        s1 = s2
        s2 = Calc(xmin,xmax,x,y,f,h)
        h /= 2
        print(str(contador) + '\t  ' + str(round(s,5)) + '\t  ' + str(round(s1,5)) + '\t  ' + str(round(s2,5)) + '\t  ' + str(round(QC(s,s1,s2),2)))

######################################################################################################
#############################    EQUAÇÕES DIFERENCIAIS (SISTEMA DE 2 EQ)        ######################
######################################################################################################

def Euler_sistemas(xmin,xmax,x,y,z,f,g,h):
    for _ in range(0, round((xmax - xmin)/h)):
        y1 = y + h*f(x,y,z)
        z += h*g(x,y,z)
        y = y1
        x += h
    return (y,z)

def RK2_sistemas(xmin,xmax,x,y,z,f,g,h):
    for _ in range(0, round((xmax - xmin)/h)):
        y1 = y + h * f(x + h/2, y + h/2 *  f(x,y,z), z + h/2 * g(x,y,z))
        z += h * g(x + h/2, y + h/2 *  f(x,y,z), z + h/2 * g(x,y,z))
        y = y1
        x += h
    return (y,z)

def RK4_sistemas(xmin,xmax,x,y,z,f,g,h):
    for _ in range(0, round((xmax - xmin)/h)):
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

    return (y,z)

def diferential_sistemas(xmin,xmax,x,y,z,f,g,h,erro, Calc):
    contador = 1
    s = Calc(xmin,xmax,x,y,z,f,g,h)
    h /= 2
    s1 = Calc(xmin,xmax,x,y,z,f,g,h)
    h /= 2
    s2 = Calc(xmin,xmax,x,y,z,f,g,h)
    h /= 2
    print(str(contador) + '\t  ' + str(s) + '\t  ' + str(s1) + '\t  ' + str(s2) + '\t  ' + str(round(QC(s[0],s1[0],s2[0]),5)) + '\t' + str(round(QC(s[1],s1[1],s2[1]),5)))
    if (Calc(xmin,xmax,x,y,z,f,g,h) == Euler_sistemas(xmin,xmax,x,y,z,f,g,h)):
        value = 2
    elif (Calc(xmin,xmax,x,y,z,f,g,h) == RK2_sistemas(xmin,xmax,x,y,z,f,g,h)):
        value = 4
    elif (Calc(xmin,xmax,x,y,z,f,g,h) == RK4_sistemas(xmin,xmax,x,y,z,f,g,h)):
        value = 16
    while (abs(QC(s[0],s1[0],s2[0]) - value) > erro or abs(QC(s[1],s1[1],s2[1]) - value) > erro):
        contador += 1
        s = s1
        s1 = s2
        s2 = Calc(xmin,xmax,x,y,z,f,g,h)
        h /= 2
        print(str(contador) + '\t  ' + str(s) + '\t  ' + str(s1) + '\t  ' + str(s2) + '\t  ' + str(round(QC(s[0],s1[0],s2[0]),5)) + '\t' + str(round(QC(s[1],s1[1],s2[1]),5)))