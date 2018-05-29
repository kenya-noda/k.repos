#2次元で重力相互作用

import numpy as np
import matplotlib.pyplot as plt
import math

#定数定義(x, y, m)
M = (((0.0, 0.0), 10.0))
#時間のリミット
TLIM = 10.0
#粒子間距離のリミット
RLIM = 0.01
#時間の刻み
H = 1


t = 0.0

plt.plot(M[0][0], M[0][1])

m = float(input("Input mass m = "))

x = float(input("Input initial position x = "))
y = float(input("Input initial position y = "))

vx = float(input("Input initial velocity vx = "))
vy = float(input("Input initial velocity vy = "))

print("{:.3f} {:.3f} {:.3f} {:.3f} {:.3f} {:.3f}".format(t, m, x, y, vx, vy))

xls = [x]
yls = [y]


while t < TLIM:
    t += H

    r = math.sqrt(x**2 + y**2)
    if r < RLIM:
        break

    vx = (x * m * M[1] * H)/(r**3)
    vy = (y * m * M[1] * H)/(r**3)

    x += vx * H
    y += vy * H

    print("{:.3f} {:.3f} {:.3f} {:.3f} {:.3f} {:.3f}".format(t, m, x, y, vx, vy))

    xls.append(x)
    yls.append(y)


plt.plot(xls, yls)
plt.show()
