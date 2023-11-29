n = int(input())
qwq = list(map(int, input().split()))
ans = 1
cont = 1
v = qwq[0]
for i in range(n):
    if qwq[i] >= v:
        cont += 1
        if cont > ans:
            ans = cont
    else:
        cont = 1
    v = qwq[i]

print(ans)
