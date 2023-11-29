alis = []
for i in range(int(input())):
    v = input().split()
    qian = 0
    if int(v[1]) > 80 and int(v[5]) >= 1:
        qian += 8000
    if int(v[1]) > 85 and int(v[2]) > 80:
        qian += 4000
    if int(v[1]) > 90:
        qian += 2000
    if v[4] == 'Y' and int(v[1]) > 85:
        qian += 1000
    if v[3] == 'Y' and int(v[2]) > 80:
        qian += 850
    alis.append(v+[str(qian)])
ans = sorted(alis, key=lambda x: int(x[6]), reverse=True)
print(ans[0][0])
print(ans[0][6])
cont = 0
for i in alis:
    cont += int(i[6])
print(cont)
