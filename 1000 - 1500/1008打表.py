num = list(i for i in range(1, 10))
maynum = []
f, s, t = 0, 0, 0
for i in num:
    f = i
    for i in num:
        if i == f:
            continue
        s = i
        for i in num:
            if i == s or i == f:
                continue
            t = i
            qwq = int(str(f) + str(s) + str(t))
            maynum.append(qwq)
print(maynum)
