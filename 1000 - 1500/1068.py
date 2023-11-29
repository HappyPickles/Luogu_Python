n, m = list(map(int, input().split()))
qwq = []
for i in range(n):
    qwq.append(list(map(int, input().split())))
a = int(1.5*m)
qwq = sorted(qwq, key=lambda x: x[0], reverse=False)
qwq = sorted(qwq, key=lambda x: x[1], reverse=True)
need_point = qwq[a-1][1]

ans = []
for i in qwq:
    if i[1] >= need_point:
        ans.append(i)
print(need_point, end=' ')
print(len(ans))
for i in ans:
    print(i[0], end=' ')
    print(i[1])

