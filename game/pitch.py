#配列を用いたピッチングシミュレーション
#3*3行列をステータスとする

import numpy as np
import sys

def pitch(p, bat): 
#バッターの数値とピッチャーの入力数値が一致したら1,しなければ0の配列を返す
    pitch = np.where( bat == p, 1, 0)
    #print(pitch)

#pitch配列の中で1を持つ要素数を求める
    jdg = len(pitch[pitch == 1])
    return jdg

#バッターの数値、整数値で1から9までの3*3行列
bat = np.random.randint(1, 10, (3, 3))
#print(bat)

print("Input the Pitch Number (1 ~ 9)")
try:
    p = int(input(">> "))

#数値以外が入ったら強制終了
except:
    print("Input error")
    sys.exit()

result = pitch(p, bat)

while result < 3:
#1つも一致しなかったら打たれる
    if result == 0:
        print("Hit! You Lose...")
        break
    
#1つ以上、3つ未満の一致だと再度試行
    print("Input the next Pitch Number (1 ~ 9)")
    try:
        p = int(input(">> "))

    except:
        print("Input error")
        sys.exit()

#2回目以降も一致しないと打たれる
    if pitch(p, bat) != 0:
        result += pitch(p, bat)
    
    else:
        print("Hit! You Lose...")
        break

#3つ以上一致するとアウトが取れる
else:
    print("Strike out! You win!")

