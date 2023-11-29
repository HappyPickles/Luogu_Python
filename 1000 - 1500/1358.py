import math
nm = input().split()
n, m = int(nm[0]), int(nm[1])
lis = list(map(int, input().split()))
cout = 1
for i in lis:
    cout *= math.comb(n, i)
    n -= i

print(cout % 10007)
