from math import exp

def f(x):
    return exp(-x) - x
def corda(a,b,n):
    it = 0
    while (it < n+1):
        it += 1
        x = (a*f(b)-b*f(a))/(f(b)-f(a))
        if (f(x)*f(a) > 0):
            print(a-x)
            print((a-x)/a)
            a = x
        elif (f(x)*f(b) > 0):
            print(b-x)
            print((b-x)/b)
            b = x
        else:
            print ("x final: " + str(x))
        print("x: " + str(x))

        
corda(0,1,3)