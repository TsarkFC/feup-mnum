'''

Runge-Kuta
sin²(x)  (0,0)

'''
from math import sin
import matplotlib.pyplot as plt

def f(x,y):
    return sin(x) * sin(x)


def rk4(func,start_point,deltax,steps):

    points = [start_point]
    last_point = start_point


    for _ in range(0,steps):
        new_point = []

        newx = last_point[0] + deltax

        delta1 = deltax*func(last_point[0],last_point[1])
        delta2 = deltax*func(last_point[0] + deltax/2,last_point[1] + delta1/2)
        delta3 = deltax*func(last_point[0] + (deltax * deltax)/2,last_point[1] + delta2/2)
        delta4 = deltax*func(last_point[0] + deltax,last_point[1] + delta3)

        deltayn = (delta1/6) + (delta2/3) + (delta3/3) + (delta4/6)

        newy = last_point[1] + deltayn
        new_point = [newx,newy]
        points.append(new_point)
        last_point = new_point

    return points

print(rk4(f,[0,0],0.1,100))

x = [v[0] for v in rk4(f,[0,0],0.1,100)]
y = [v[1] for v in rk4(f,[0,0],0.1,100)]

plt.plot(x,y)
# plt.plot(x,error)
plt.show()

#error = [real_sol(v[0]) - v[1] for v in diffeq_euler(f,[0,1],0.1,100)]