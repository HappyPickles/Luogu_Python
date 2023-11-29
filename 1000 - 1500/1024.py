abcd = list(map(float, input().split()))
a, b, c, d = abcd[0], abcd[1], abcd[2], abcd[3]

def f(x):
    return a*(x**3) + b*(x**2) + c*x + d


def f_der(x):
    det_x = 1E-5
    return (f(x + det_x) - f(x)) / det_x


def newtown(n):
    det_x = 1E-5
    if f_der(n) != 0:
        n = n - (f(n)/f_der(n))
    else:
        n = n - (f(n)/det_x)
    if abs(f(n)) < 1E-5:
        return n
    else:
        return newtown(n)

ans = []
for i in range(-100, 100):
    jie = '%.2f' % newtown(i)
    if jie not in ans:
        ans.append(jie)

ans = list(map(float, ans))
ans = sorted(ans)
for i in ans:
    print('%.2f' % i, end=' ')
