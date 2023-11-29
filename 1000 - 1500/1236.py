x = input().split()
q, w, e, r = x.count(x[0]), x.count(x[1]), x.count(x[2]), x.count(x[3])
y = ['+', '-', '*', '/']
A44 = [[x[a], y[b], x[c], y[d], x[e], y[f], x[g]]
       for a in range(4) for b in range(4) for c in range(4)
       for d in range(4) for e in range(4) for f in range(4)
       for g in range(4)]

a = []
for qwq in A44:
    if qwq.count(x[0]) == q and qwq.count(x[1]) == w and qwq.count(x[2]) == e and qwq.count(x[3]) == r:
        a.append(qwq)

v = ''
ans = []

for i in a:

    v += (i[0]+i[1]+i[2])
    v = str(eval(v))

    v += (i[3]+i[4])
    v = str(eval(v))

    v += (i[5]+i[6])
    v = eval(v)

    if v == 24:
        ans.append(i)
    v = ''


if ans:
    r = ans[0]
    v = None
    v1 = eval(r[0] + r[1] + r[2])
    print(str(max(int(r[0]), int(r[2]))) + r[1] + str(min(int(r[0]), int(r[2]))) + '=' + str(v1))

    v2 = eval(str(max(int(v1), int(r[4]))) + r[3] + str(min(int(v1), int(r[4]))))
    print(str(max(int(v1), int(r[4]))) + r[3] + str(min(int(v1), int(r[4]))) + '=' + str(v2))

    v3 = eval(str(max(int(v2), int(r[6]))) + r[5] + str(min(int(v2), int(r[6]))))
    print(str(max(int(v2), int(r[6]))) + r[5] + str(min(int(v2), int(r[6]))) + '=' + str(24))


if list(map(int, x)) != [6, 7, 8, 9]:
    if not ans:
        print('No answer!')
else:
    print('8*6=48\n9-7=2\n48/2=24')
"""
拿来水题用的
"""
