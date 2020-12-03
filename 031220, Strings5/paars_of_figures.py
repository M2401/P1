#В текстовый файл занесены пары чисел, разделенных пробелом (каждая пара чисел – в
# новой строке). Рассматривая каждую пару как координаты точек на плоскости,
# найти наибольшее и наименьшее расстояния между этими точками.

import math
a = []

with open("pairs.txt", "r") as file:
    for line in file:
        b = list(map(int, line.split()))
        a.append(b)
print(a)

def dir(x1, y1, x2, y2):
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return d

for i in range(len(a)-1):
    d = dir(a[i][0], a[i][1], a[i+1][0], a[i+1][1])
    print(d)
