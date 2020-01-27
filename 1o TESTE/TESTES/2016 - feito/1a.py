def f(x,y):
    return 1 - x**2 - y
def g(x,y):
    return 0.7 + x - y
def dfx(x,y):
    return -2*x
def dfy(x,y):
    return -1
def dgx(x,y):
    return 1
def dgy(x,y):
    return -1

def mnewton(x,y,err):
    xn = x
    yn = y
    x = xn - (f(xn,yn)*dgy(xn,yn) - g(xn,yn)*dfy(xn,yn))/(dfx(xn,yn)*dgy(xn,yn) - dfy(xn,yn)*dgx(xn,yn))
    y = yn - (g(xn,yn)*dfx(xn,yn) - f(xn,yn)*dgx(xn,yn))/(dfx(xn,yn)*dgy(xn,yn) - dfy(xn,yn)*dgx(xn,yn))
    while(abs(xn-x) > err or abs(yn-y) > err):
        xn = x
        yn = y
        x = xn - (f(xn,yn)*dgy(xn,yn) - g(xn,yn)*dfy(xn,yn))/(dfx(xn,yn)*dgy(xn,yn) - dfy(xn,yn)*dgx(xn,yn))
        y = yn - (g(xn,yn)*dfx(xn,yn) - f(xn,yn)*dgx(xn,yn))/(dfx(xn,yn)*dgy(xn,yn) - dfy(xn,yn)*dgx(xn,yn))
        print("x: " + str(x))
        print("y: " + str(y))

mnewton(-1,0,10**(-3))
