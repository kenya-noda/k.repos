#給料計算　残業代込

def payroll(x):
    ans = x * 900
#時給900円として計算,残業代は25%up
    return ans

def overtime(x):
    ove = (x - 8)*900*1.25
#この段階でfloat型
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


print ('base , over , all')
#int型に戻す
print (sal , int(salove) , int(sal+salove))
