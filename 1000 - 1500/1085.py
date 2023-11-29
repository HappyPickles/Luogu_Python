week = [0,0,0,0,0,0,0]
for i in range(7):
    qwq = input().split()
    t0 = int(qwq[0])
    t1 = int(qwq[1])
    if t0 + t1 > 8:
        week[i] += (t0+t1-8)
if max(week) != 0:
    ans = week.index(max(week))
    print(ans + 1)
else:
    print(0)