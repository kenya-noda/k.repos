#打球の飛距離判定　中堅125mの球場
#角度と打球速度により算出　簡単な高校物理で

import math
import random
from time import sleep


def jdg(v, theta):
    x = 122
    g = 9.8
#km/hをm/sに変換
    v = v * 0.278

    y = math.tan(theta) * x - (g * x**2)/(2 * (v**2) * (math.cos(theta))**2)

#地面との接触判定
    if y <= 0:
        y = 0

    return y


#飛距離を計算
def cal(v,theta):
    g = 9.8
    v = v * 0.278
    
    x = (v**2 * math.sin(2*theta)) / g
    return x


print ('Input initial velocity')
print ('From home base: 122 (m), Wall: 4.2 (m)')
v = float(input("(km/h) >>"))


#打球角度を乱数で与える
theta = random.uniform(0, 1.57)
print('Angle (degrees):', int(math.degrees(theta)))

y122 = jdg (v, theta)
#ちょっと間をとる
sleep(0.5)


#フェンスを越えるかの判定
if y122 < 4.2:
    print("Not a home run...")
    if y122 == 0:
        car = cal(v,theta)
    else:
        car = 122

else:
    print("Home run!")
    car = cal(v,theta)

print ("Carry (m):",int(car))


