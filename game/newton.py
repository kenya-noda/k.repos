#ニュートン法を用いて二次関数の解を求める

#二次関数を定義
def f(x):
    return x**2 - 5*x + 6

#微分する
def df(x):
    h = 1e-4

    return (f(x+h) - f(x-h)) / (2*h)

#ニュートン法の関数定義
def newton(a, e):
    for i in range(1000):
        ah = a - f(a)/df(a)
#ある微少量epsilonを過ぎるとbreak
        if abs(ah - a) < e:
            break

        a = ah

    return a

#最初はx=1.0から、eps = 0.001でbreak
ans = newton(1.0, 0.001)

#formatを用いてfloatの表示桁数を制限
print('Solution: ',"{:.2}".format(ans))


