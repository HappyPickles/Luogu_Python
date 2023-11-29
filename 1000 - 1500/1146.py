def fanzhuan(x: list, n: int):
    if x[n] == 0:
        x[n] = 1
    else:
        x[n] = 0


N = int(input())
print(N)
coins = [0 for i in range(N)]

for i in range(N):
    for q in range(N):
        if q != i:
            fanzhuan(coins, q)
    for z in coins:
        print(z, end='')
    print()
