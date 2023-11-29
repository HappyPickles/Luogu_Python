n = int(input())
fr = []
for i in range(n):
    fr.append([i+1] + list(map(int, input().split())))
se = sorted(fr, key=lambda x: x[0])

tr = sorted(se, key=lambda x: x[1], reverse=True)

fo = sorted(tr, key=lambda x: x[1] + x[2] + x[3], reverse=True)
cout = 0
for i in fo:
    print(i[0], end=' ')
    print(i[1] + i[2] + i[3])
    cout += 1
    if cout == 5:
        break
