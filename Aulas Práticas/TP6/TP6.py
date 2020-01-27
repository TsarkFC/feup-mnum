#[7  3  1 ] [24]
#[11 13 3 ] [64]
#[3  11 17] [56]

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

#GET RESIDUAL VALUE
res = residuo_gauss(m1, m2, result)

#a(matriz 3x3) * delta = residuos
#CALCULO DE DELTA

d = [[7,3,1,res[0]],
    [11,13,3,res[1]],
    [3,11,17,res[2]]]

#PRIMEIRO DELTA
delta1 = Gauss(d)
