N = int(input())
alis = []
for _ in range(N):
    alis.append(input().strip().split())

alis = sorted(alis, key=lambda x: int(x[1])+int(x[2])+int(x[3]), reverse=True)
for i in alis[0]:
    print(i, end=' ')
