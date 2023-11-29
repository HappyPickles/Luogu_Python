qwq = input().split()
n = int(qwq[0])
k = int(qwq[1])
A = []
B = []
for i in range(1, n+1):
    if (i/k)%1 == 0:
        A.append(i)
    else:
        B.append(i)
a, b = sum(A)/len(A), sum(B)/len(B)
print(str('%.1f' % a) + ' ' + str('%.1f' % b))
