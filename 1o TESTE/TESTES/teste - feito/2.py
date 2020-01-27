def f(x,y):
    return x**2 - y - 1.2
def fx(x,y):
    return 2*x
def fy(x,y):
    return -1

def g(x,y):
    return -x + y**2 -0.5
def gx(x,y):
    return -1
def gy(x,y):
    return 2*y

def newton(a,b):
    for _ in range(2):
        x = a - (f(a,b)*gy(a,b)-g(a,b)*fy(a,b))/(fx(a,b)*gy(a,b) - fy(a,b)*gx(a,b))
        y = b - (g(a,b)*fx(a,b)-f(a,b)*gx(a,b))/(fx(a,b)*gy(a,b) - fy(a,b)*gx(a,b))
        a = x
        b = y
        print("x: " + str(x))
        print("y: " + str(y))

print(newton(1.1, 1.1))
