import math


def sq(n: int, m: int):
    ans = -(n**3)/6 + (m*(n**2))/2 + (3*m*n)/2 + n/6  # 公式错了， 干
    return ans


n, m = list(map(int, input().split()))
a = math.comb(n+1, 2) * math.comb(m+1, 2)
sqs = int(sq(n, m))
print(sqs, end=' ')
print(a-sqs)
print(sq(n, m))
