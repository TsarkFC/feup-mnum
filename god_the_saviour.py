from math import sqrt

######################################################################################################
#######################                BISSEÇÃO                  #####################################
######################################################################################################

def erro_absoluto_bissecao(a,b,erro,f):
    x = (a+b)/2
    contador = 1
    temp = 0
    while(abs(temp - x) > erro):
        print(str(contador) + '\t x = ' + str(x))
        contador += 1
        if (f(a) * f(x) < 0):
            b = x
        else:
            a = x
        temp = x
        x = (a+b)/2
    
    print(str(contador) + '\t x = ' + str(x) + '\n')
    return x

######################################################################################################
#######################                   CORDA                  #####################################
######################################################################################################


def erro_absoluto_corda(a,b,erro,f):
    x= (f(a)*b - f(b)*a) / (f(a)-f(b))
    contador = 1
    temp = 0
    while (abs(temp - x) > erro):
        print(str(contador) + '\t x = ' + str(x))
        contador += 1
        if (f(a) * f(x) < 0):
            b = x
        else:
            a = x       
        temp = x
        x= (f(a)*b - f(b)*a) / (f(a)-f(b))

    print(str(contador) + '\t x = ' + str(x) + '\n')
    return x

######################################################################################################
#######################                PICARDI-PEANO                  ################################
######################################################################################################

def picardi(x,erro, func):
    temp = x
    x = func(temp)
    contador = 1
    print(str(contador) + '\t' + str(x) + '\t' + str(temp))
    while (abs(x - temp) > erro):
        contador += 1
        temp = x
        x = func(temp)
        print(str(contador) + '\t' + str(x) + '\t' + str(temp))

    print ("Zero: " + str(x) + '\n')

######################################################################################################
#######################            PICARDI-PEANO SYSTEMS                 #############################
######################################################################################################

def picard_sistema(x,y,erro,f1,f2):
    xtemp = x
    ytemp = y
    x = f1(xtemp,ytemp)
    y = f2(xtemp,ytemp)
    while (abs(x-xtemp) > erro or abs(y-ytemp) > erro):
        xtemp = x
        ytemp = y
        x = f1(xtemp,ytemp)
        y = f2(xtemp,ytemp)
        print("x: " + str(x))
        print("y: " + str(y))


######################################################################################################
#######################                   NEWTON                        ##############################
######################################################################################################

def newton(x,erro, func, func1):
	temp = x + 10**10 * erro
	contador = 0
	while (abs(temp - x) > erro):
		temp = x
		x -= func(x)/func1(x)
		contador += 1
		print(str(contador) + '\t x = ' + str(x))
	print ("\nZero: " + str(x) + '\n')


######################################################################################################
#######################                 NEWTON SYSTEMS                  ##############################
######################################################################################################

def sistema_newton(f1, f1x, f1y, f2, f2x, f2y, x, y, erro): #duas primeiras iterações
    xi = x
    yi = y
    x = xi - (f1(xi,yi)*f2y(xi,yi) - f2(xi,yi)*f1y(xi,yi)) / (f1x(xi,yi)*f2y(xi,yi) - f1y(xi,yi)*f2x(xi,yi))
    y = yi - (f2(xi,yi)*f1x(xi,yi) - f1(xi,yi)*f2x(xi,yi)) / (f1x(xi,yi)*f2y(xi,yi) - f1y(xi,yi)*f2x(xi,yi))
    print("x: " + str(x))
    print("y: " + str(y))
    while (abs(xi - x ) > erro):
        xi = x
        yi = y
        x = xi - (f1(xi,yi)*f2y(xi,yi) - f2(xi,yi)*f1y(xi,yi)) / (f1x(xi,yi)*f2y(xi,yi) - f1y(xi,yi)*f2x(xi,yi))
        y = yi - (f2(xi,yi)*f1x(xi,yi) - f1(xi,yi)*f2x(xi,yi)) / (f1x(xi,yi)*f2y(xi,yi) - f1y(xi,yi)*f2x(xi,yi))
        print("x: " + str(x))
        print("y: " + str(y))


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
#############################          TRAPEZIO DOUBLE INTEGRAL      #################################
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

######################################################################################################
#############################       OPTIMIZATION GOLDEN SECTION        ###############################
######################################################################################################


def optimized_golden(f, step, guess):

    #Get search direction
    if (f(guess + step) > f(guess)):
        step = -step

    a = guess

    while (f(guess + step) < f(guess)):
        a = guess
        guess += step

    b = guess

    #Intervalo [a,b]

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

######################################################################################################
#############################                  GRADIENTE               ###############################
######################################################################################################

def gradiente(x,y,erro,f,fx,fy,lamb):
    contador = 0

    print("Contador: ", contador)
    print("x: ",x, "\ty: ",y)
    print("f(x,y): ",f(x,y))
    print()
    print("Gradiente:")
    print(fx(x,y), fy(x,y))
    print()

    contador += 1

    x1 = x - lamb*fx(x,y)
    y1 = y - lamb*fy(x,y)

    print("Contador: ", contador)
    print("x: ",x1, "\ty: ",y1)
    print("f(x,y): ",f(x1,y1))
    print()
    print("Gradiente:")
    print(fx(x1,y1), fy(x1,y1))
    print()

    while(abs(x1 - x) > erro or abs(y1 - y) > erro):
        if (f(x1,y1) < f(x,y)):
            lamb *= 2
            x = x1
            y = y1
        else:
            lamb /= 2

        x1 = x - lamb*fx(x,y)
        y1 = y - lamb*fy(x,y)
        contador += 1

        print("Contador: ", contador)
        print("x: ",x1, "\ty: ",y1)
        print("f(x,y): ",f(x1,y1))
        print()
        print("Gradiente:")
        print(fx(x1,y1), fy(x1,y1))
        print()

######################################################################################################
#############################                 QUÁDRICA                 ###############################
######################################################################################################
def h(x,y,fxx,fyy,fxy,fyx):
    return fxx(x,y)*fyy(x,y) - fxy(x,y)*fyx(x,y)

def quadrica(x,y,erro,f,fx,fy,fxx,fyy,fxy,fyx):
    contador = 1
    x1 = x - 1/h(x,y,fxx,fyy,fxy,fyx) * fx(x,y)
    y1 = y - 1/h(x,y,fxx,fyy,fxy,fyx) * fy(x,y)
    while(abs(x1 - x) > erro or abs(y1 - y) > erro):
        x = x1
        y = y1
        x1 = x - 1/h(x,y,fxx,fyy,fxy,fyx) * fx(x,y)
        y1 = y - 1/h(x,y,fxx,fyy,fxy,fyx) * fy(x,y)
    print("Contador: ", contador)
    print("x: ",x, "\ty: ",y)
    print("f(x,y): ",f(x,y))

######################################################################################################
#############################           LEVEMBERG-MARQUARDT            ###############################
######################################################################################################

def lm(x,y,erro,a,delta,f,fx,fy,fxx,fyy,fxy,fyx):
    contador = 1
    x1 = x - (a*fx(x,y) + 1/h(x,y,fxx,fyy,fxy,fyx)*fx(x,y))
    y1 = y - (a*fy(x,y) + 1/h(x,y,fxx,fyy,fxy,fyx)*fy(x,y))
    while(abs(x1 - x) > erro or abs(y1 - y) > erro):
        if (f(x1,y1) > f(x,y)):
            a += delta
        else:
            a -= delta
        x = x1
        y = y1
        x1 = x - (a*fx(x,y) + 1/h(x,y,fxx,fyy,fxy,fyx)*fx(x,y))
        y1 = y - (a*fy(x,y) + 1/h(x,y,fxx,fyy,fxy,fyx)*fy(x,y))
    print("Contador: ", contador)
    print("x: ",x1, "\ty: ",y1)
    print("f(x,y): ",f(x,y))