n = int(input())
qwq = input().split()
h = 0
for i in range(n):
    for z in range(i):
        if int(qwq[z]) < int(qwq[i]):
            h += 1
    print(h,end = ' ')
    h = 0
