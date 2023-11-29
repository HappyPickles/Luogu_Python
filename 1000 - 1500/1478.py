n, s = map(int, input().split())
a, b = map(int, input().split())
alis = []
for _ in range(n):
    alis.append(list(map(int, input().split())))
h = a + b
alis.sort(key=lambda x: x[1])
ans = 0
v = 0
for i in alis:
    if v+i[1] <= s:
        if h >= i[0]:
            ans += 1
            v += i[1]
    else:
        break

print(ans)
