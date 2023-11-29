import math
jihe = list(map(int, input().split()))
m = len(jihe)
ans = 0
sums = sum(jihe)
for n in range(1, m+1):
    cishu = ((math.comb(m, n)*n)/m)
    ans += sums * cishu
print(float(ans))
