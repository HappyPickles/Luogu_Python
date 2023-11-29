import math
n, m = list(map(int, input().split()))
a = math.comb(n+1, 2) * math.comb(m+1, 2)
b = 0
for i in range(min(n, m)):
    b += (n-i) * (m-i)
bl = a-b
sq = b
print(sq, end=' ')
print(bl)
