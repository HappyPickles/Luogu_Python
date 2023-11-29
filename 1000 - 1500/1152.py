qwq = list(map(int, input().split()))
n = len(qwq) - 1
pack = []
for i in range(1, n):
    pack.append(abs(qwq[i] - qwq[i+1]))
ans = [i for i in range(1, n)]
pack = sorted(pack)
if pack == ans:
    print('Jolly')
else:
    print('Not jolly')
