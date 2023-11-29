n = int(input())
alis = []
for i in range(n):
    alis.append(input().split() + [i])
alis = sorted(alis, key=lambda x: x[4], reverse=True)
for i in range(3, 0, -1):
    alis = sorted(alis, key=lambda x: int(x[i]))
for i in alis:
    print(i[0])
