#放物線をグラフとして表示

import matplotlib.pyplot as plt
import math
import random

#定数定義
g = 9.8
#時間のリミット
TLIM = 30.0
#時間の刻み幅
H = 0.001

#格納リスト
xls = []
yls = []


print ('Input initial velocity')
vel = float(input("(km/h) >>"))

#角度を乱数で与える
theta = random.uniform(0, 1.57)
print('Angle (degrees):', int(math.degrees(theta)))

t = 0.0
vel = vel * 0.278


while t < TLIM:
    
    x = vel * math.cos(theta) * t
    y = -(g/2) * t**2 + vel * math.sin(theta) * t
#yが負になったらbreak
    if y < 0:
        break

#リストに追加していく
    xls.append(x)
    yls.append(y)

    t += H

#フェンスの表示
plt.plot([122.0,122.0],[0.0,4.2])

plt.plot(xls, yls)
plt.show()
