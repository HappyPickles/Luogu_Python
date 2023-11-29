import math
n, k = list(map(int, input().split()))
ans = math.comb(n+k, k)
print(ans)
