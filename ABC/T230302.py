qwq = input().split()
a, b = qwq[0], qwq[1]
a = (int(a) ^ 9961) + 17
b = (int(b) ^ 9961) + 17 + a
a = a * 81
b = b * 81
ab = a + b
ab = (ab-6)
ab += 2
ab = list(str(ab))
ab[len(ab)-1] = 1
v1 = '0'
for i in ab:
    v1 += str(i)
ans = int(v1) % 9
print(ans)