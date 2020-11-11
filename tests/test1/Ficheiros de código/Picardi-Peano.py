import math

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

def picardi_sistema(x,y,erro,funcx,funcy):
    xtemp = x
    ytemp = y
    x = funcx(xtemp,ytemp)
    y = funcy(xtemp,ytemp)
    contador = 1
    print(str(contador) + '\t (' + str(x) + ',' + str(y) + ')')
    while (abs(x-xtemp) > erro or abs(y-ytemp) > erro):
        contador += 1
        xtemp = x
        ytemp = y
        x = funcx(xtemp,ytemp)
        y = funcy(xtemp,ytemp)
        print(str(contador) + '\t (' + str(round(x,7)) + ',' + str(round(y,7)) + ')')

    print ("Zero: (" + str(round(x,7)) + ',' + str(round(y,7)) + ')' + '\n')


def newton(x,y,erro, f1,f2,f1x,f1y,f2x,f2y):
    xtemp = x
    ytemp = y
    x = xtemp - (f1(xtemp,ytemp)*f2y(xtemp,ytemp) - f2(xtemp,ytemp)*f1y(xtemp,ytemp)) / (f1x(xtemp,ytemp) * f2y(xtemp,ytemp) - f1y(xtemp,ytemp) * f2x(xtemp,ytemp))
    y = ytemp - (f2(xtemp,ytemp)*f1x(xtemp,ytemp) - f1(xtemp,ytemp)*f2x(xtemp,ytemp)) / (f1x(xtemp,ytemp) * f2y(xtemp,ytemp) - f1y(xtemp,ytemp) * f2x(xtemp,ytemp))
    contador = 1
    print(str(contador) + '\t (' + str(x) + ',' + str(y) + ')')
    while (abs(x-xtemp) >= erro or abs(y-ytemp) >= erro):
        contador += 1
        xtemp = x
        ytemp = y
        x = xtemp - (f1(xtemp,ytemp)*f2y(xtemp,ytemp) - f2(xtemp,ytemp)*f1y(xtemp,ytemp)) / (f1x(xtemp,ytemp) * f2y(xtemp,ytemp) - f1y(xtemp,ytemp) * f2x(xtemp,ytemp))
        y = ytemp - (f2(xtemp,ytemp)*f1x(xtemp,ytemp) - f1(xtemp,ytemp)*f2x(xtemp,ytemp)) / (f1x(xtemp,ytemp) * f2y(xtemp,ytemp) - f1y(xtemp,ytemp) * f2x(xtemp,ytemp))
        print(str(contador) + '\t (' + str(round(x,7)) + ',' + str(round(y,7)) + ')')

    print ("Zero: (" + str(round(x,7)) + ',' + str(round(y,7)) + ')' + '\n')

