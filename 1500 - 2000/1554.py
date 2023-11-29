m, n = list(map(int, input().split()))
v = ''
for i in range(m, n+1):
    v += str(i)

for q in range(10):
    print(v.count(str(q)), end=' ')



