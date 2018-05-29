#給料計算

def payroll(x):
    ans = x * 900
#時給900円として計算
    return ans

print ('Input monthly Working hours')
wh = (input('>> '))

sal = payroll(int(wh))
#intが無いと入力した値が900回表示される
#because input関数は入力を文字列として扱う。intで数値に変換
print (sal)

