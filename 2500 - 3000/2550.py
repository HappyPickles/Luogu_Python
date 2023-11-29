n = int(input())
need = list(map(int, input().split()))
buys = []
ans = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(n):
    buy = list(map(int, input().split()))
    buys.append(buy)
cont = 0
for i in buys:
    for q in i:
        if q in need:
            cont += 1
    ans[(7 - cont)] += 1
    cont = 0
for i in range(7):
    print(ans[i], end=' ')
