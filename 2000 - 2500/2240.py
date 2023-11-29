N, T = list(map(int, input().split()))
n, t = (N, T)
golds = []
bag = []
for i in range(N):
    golds.append(list(map(int, input().split())))
golds = sorted(golds, key=lambda x: x[1]/x[0], reverse=True)
print(golds)
for i in golds:
    if t == 0:
        break
    if t - i[0] >= 0:
        bag.append(i)
        t -= i[0]
    else:
        # t - i[0] <= 0
        bag.append([t, t*(i[1]/i[0])])
        t -= t

ans = 0
for i in bag:
    ans += i[1]
print('%.2f' % ans)
