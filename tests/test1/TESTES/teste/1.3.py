from math import exp

def f(x):
    return exp(0.7*x) - x**2 - 0.5

def bissec(a, b):
    x = (a+b)/2
    print("x: " + str(x))

    for _ in range(3):
        print("f(x): " + str(f(x)))
        print("f(a): " + str(f(a)))
        print("f(b): " + str(f(b)))
        if (f(x)*f(a) > 0):
            a = x
        elif (f(x)*f(a) < 0):
            b = x
        print ("a: " + str(a))
        print("b: " + str(b))
        x = (a+b)/2
        print("x: " + str(x))
print(bissec(-1,0))    