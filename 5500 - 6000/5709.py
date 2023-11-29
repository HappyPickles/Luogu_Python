qwq = input().split()
m = int(qwq[0])
t = int(qwq[1])
s = int(qwq[2])
if s == 0:
    print(m)
if t == 0:
    print(0)
else:
    most = s/t
    if most >= m:
        print(0)
    else:
        print(int(m - most))