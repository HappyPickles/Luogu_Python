k = int(input())
ans = []
for i in range(10000, 30001):
    qwq = str(i)
    a1 = int(qwq[0:3])
    a2 = int(qwq[1:4])
    a3 = int(qwq[2:5])
    if a1 % k == 0 and a2 % k == 0 and a3 % k == 0:
        ans.append(i)

if ans:
    for i in ans:
        print(i)
else:
    print('No')
