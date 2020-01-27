def x1(y):
    return -(1-y)**(0.5)
def y1(x):
    return 0.7 + x

def x2(y):
    return y - 0.7
def y2(x):
    return 1 - x**2

def picard(x,y,err):
    it = 1
    xn = x2(y) #mudar com x1/x2
    yn = y2(x) #mudar com y1/y2
    print ("it: " + str(it) + " x -> " + str(xn))
    print ("it: " + str(it) + " y -> " + str(yn))
    while (abs(xn-x) > err or abs(yn-y) > err):
        it += 1
        x = xn
        y = yn
        xn = x2(y) #mudar com x1/x2
        yn = y2(x) #mudar com y1/y2
        print ("it: " + str(it) + " x -> " + str(xn))
        print ("it: " + str(it) + " y -> " + str(yn))
    
picard(0,0.5,0.0001)