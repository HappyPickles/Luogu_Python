n = int(input())

qwq = [0, 1] + [2 for _ in range(n-1)]

for i in range(2, int(n/2)+2):
    for j in range((i*2), n+1, i):
        qwq[j] += 1

print(qwq)
print(sum(qwq))
