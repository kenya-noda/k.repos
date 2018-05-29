#月ごとの給料計算

def payroll(x):
    ans = x * 900
#時給900円として計算
    return ans


print ('Input　Working hours by month\n---------------------\n1  2  3  4  5  6  7  8  9  10  11  12 ')

list = [int(x) for x in input().split()]

salsum = sum(list)
sal = payroll(salsum)

print (sal)
