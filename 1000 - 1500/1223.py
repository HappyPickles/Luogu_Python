n = int(input())
times = list(map(int, input().split()))
index = [i for i in range(1, n+1)]
maps = sorted(zip(times, index))
var = 0
ans = 0
for st in maps:
    print(st[1], end=' ')
    ans += var
    var += st[0]
print()
print('%.2f' % (ans/n))
