def f(x):
    return -12 - 21*x + 18*x**2 - 2.75*x**3

def bissec(a,b,err):
    x = (a+b)/2
    #temp = 0
    while (abs(a-b) > err):
        #temp = x
        if (f(a)*f(x) > 0):
            a = x
        elif (f(b)*f(x) > 0):
            b = x
        x = (a+b) / 2

    print("x: " + str(x))

bissec(-1,0,0.001)