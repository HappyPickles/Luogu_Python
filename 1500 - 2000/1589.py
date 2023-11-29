n, L = map(int, input().strip().split())
load = [True for _ in range(10000)]
for _ in range(n):
    v = list(map(int, input().strip().split()))
    if v[0] >= 10000:
        continue
    elif v[1] >= 10000:
        for i in range(v[0], 10000):
            load[i] = False
    else:
        for i in range(v[0], v[1]):
            load[i] = False

cont = 0
for i in range(10000):
    if load[i]:
        continue
    elif i+L <= 10000:
        cont += 1
        for j in range(i, i+L):
            load[j] = True
    else:
        cont += 1
        for j in range(i, 10000):
            load[j] = True

print(cont)
