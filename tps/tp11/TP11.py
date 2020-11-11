'''
-----------------------GRADIENTE-----------------------------------
X(n+1) = X(n) - lambda * Yf(X(n)), em que Y representa o gradiente

Caso f(X(n)) > f(X(n+1)) -> lambda aumenta
Caso contrário -> lambda diminui

---------------------CONDIÇÕES DE PARAGEM:-------------------------

(à parte -> controlo de qualidade de resultados -> verificação de resíduos)

ERRO: |f(X(n)) - f(X(n+1))| < Ev

distância(X(n), X(n+1)) < Edistancia

  O métoo do gradiente deve parar quando o gradiente for inferior a um valor muito pequeno 
para não comprometer a eficiência do programa

'''

from math import sqrt

def f(x,y):
    return (y**2 + x**2)

def dfdx(x,y):
    return 2*x + y**2

def dfdy(x,y):
    return 2*y + x**2

def dist(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def gradiente(xo, yo, lamb, err, f, dfdx, dfdy):

    x = xo - lamb*dfdx(xo,yo)
    y = yo - lamb*dfdy(xo,yo)

    while(abs(f(x,y) - f(xo,yo)) > err):
        #update lambda value
        if (f(xo, yo) > f(x, y)):
            lamb *= 2
        else:
            lamb /= 2
        
        #update temporary values
        xo = x
        yo = y

        #update x, y values
        x = xo - lamb*dfdx(xo,yo)
        y = yo - lamb*dfdy(xo,yo)

    return (x,y)

print("Resultado: " + str(gradiente(10, 10, 0.1, 0.001,f,dfdx,dfdy)))


'''
----------------------MÉTODO QUÁDRICA------------------------------

-> -H**-1 * Yf(), em que H = [ddf/dx**2 ddf/dxdy] e Y é o gradiente
                             [ddf/dydx  ddf/dy**2]

-> Útil quando aplicado intercaladamente com o passo iterativo de gradiente  
-> Aplicar no máxima                        
'''




