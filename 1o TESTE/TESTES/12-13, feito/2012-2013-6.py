from math import log, sqrt

def f1(x,y):
    return y - log(x-1)
def f2(x,y):
    return y*y + (x-3)*(x-3) - 4
def f1x(x,y):
    return - 1 / (x-1)
def f2x(x,y):
    return 2*(x-3)
def f1y(x,y):
    return 1
def f2y(x,y):
    return 2*y

def g1(x,y):
    return sqrt((x*y+5*x-1)/2)
def g2(x,y):
    return sqrt(x+3*log(x,10))

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

print(sistema_newton(f1, f1x, f1y, f2, f2x, f2y, 1.5, 1.3, 1))

#Pelo método Picard-Peano

def picard_sistema(x,y,erro,f1,f2):
    xtemp = x
    ytemp = y
    x = g1(xtemp,ytemp)
    y = g2(xtemp,ytemp)
    while (abs(x-xtemp) > erro or abs(y-ytemp) > erro):
        xtemp = x
        ytemp = y
        x = g1(xtemp,ytemp)
        y = g2(xtemp,ytemp)
        print("x: " + str(x))
        print("y: " + str(y))

#picard_sistema(3.5,2.3,0.000001)

