import math


t = int(input())
ans = []
for _ in range(t):
    n, a = map(int, input().split())
    ans.append(str(math.factorial(n)).count(str(a)))

for qwq in ans:
    print(qwq)
