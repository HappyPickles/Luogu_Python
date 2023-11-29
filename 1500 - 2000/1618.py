a, b, c = list(map(int, input().split()))


def find(x, y, z):
    v = []
    for i in range(len(x)):
        v.append(x[i])
        v.append(y[i])
        v.append(z[i])
    if len(list(set(v))) == 9 and '0' not in v:
        return False
    else:
        return True

ans = []
for q in range(100, 1000):
    w = int((q/a) * b)
    e = int((q/a) * c)
    if find(str(q), str(w), str(e)) or w // 100 >= 10 or e // 100 >= 10:
        continue
    else:
        ans.append([q, w, e])
if ans != []:
    for i in ans:
        print(i[0], i[1], i[2])
else:
    print('No')
