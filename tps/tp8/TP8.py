#--------------------------------------------
#---------EQUAÇÕES DIFERENCIAIS--------------
#--------------------------------------------

#---------------------
#---MÉTODO DE EULER---
#---------------------

# dy / dx = x 
# Solução analítica: x**2 / 2 + C

def f(x, y):
    return x

def diff_euler(f, delta_x, n, xi, yi):
    last_point = [xi, yi]
    points = [last_point]

    for _ in range(1, n):
        new_x = last_point[0] + delta_x

        delta_y = delta_x * f(last_point[0], last_point[1])
        new_y = last_point[1] + delta_y

        new_point = [new_x, new_y]

        points.append(new_point)
        last_point = new_point
    
    return points 


#CÁLCULO DO QUOCIENTE DE CONVERGÊNCIA PARA O MÉTODO DE EULER, h que está no texto é igual a delta_x -> QC = 2
def qc(n, delta_x, f, points):

    values = []
    for i in range(len(points)):

        s = diff_euler(f, delta_x, n, points[0], points[1])[i][1]
        s1 = diff_euler(f, delta_x * 2, n / 2, points[0], points[1])[i][1]    
        s2 = diff_euler(f, delta_x * 4, n / 4, points[0], points[1])[i][1]

        values.append((s1 - s) / (s2 - s1))

    return values

