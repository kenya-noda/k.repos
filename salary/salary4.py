#日毎の給料計算　残業代込

from collections import OrderedDict

def payroll(x):
    ans = x * 900
#時給900円として計算,残業代は25%up
    return ans

def overtime(x):
    ove = (x - 8)*900*1.25
    return ove

print ('Input daily Working hours')
wh = [int(x) for x in input().split()]

sal = 0
salove = 0

#８時間超えたら残業代
for e in wh:
    if (e-8) <= 0:
        sal += payroll(e)

    if (e-8) > 0:
        sal += payroll(8)
        salove += overtime(e)

#dictionaryを使って整頓、勤務日数と時間を追加
#dictionaryではkeysの順番は保持されない為、OrderedDictを用いた
tap = (('days',len(wh)),('hours',sum(wh)),('base',sal),('over',int(salove)),('all',int(sal+salove)))
#簡単のためtupleを用いてdictionaryに要素を代入,OrderedDictは並べて書く必要がある。
odic = OrderedDict(tap)

#itemsmethodでkeyとvalueの両方を取得
for keys,values in odic.items():
    print('{} : {}'.format(keys,values))
#format関数は変数を文字列に埋め込む
