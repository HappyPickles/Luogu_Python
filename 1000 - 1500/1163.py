a, b, c = map(int, input().split())


def f(al, t, ret):
    s = al*(1+t) - ret
    return s


ans = 0.0001
alis = {'0.0000': (b*c)-a}
if b > a:
    ans = 1.0001
for _ in range(1000000):
    var = a
    for _ in range(c):
        var = f(var, ans, b)
    alis[str('%.4f' % ans)] = var

    if '%.4f' % (ans-0.0001) in alis:
        if b <= a:
            if abs(alis['%.4f' % ans]) - abs(alis['%.4f' % (ans-0.0001)]) > 0:
                break
        else:
            if abs(alis['%.4f' % ans]) - abs(alis['%.4f' % (ans-0.0001)]) > 0:
                break
    ans += 0.0001

ans *= 100
print('%.1f' % ans)
