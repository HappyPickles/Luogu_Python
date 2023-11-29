N = int(input())
qwq = list(map(int, input().split()))
qwq.append(-1)
cout = 1
li = []
for i in range(len(qwq)-1):
    fi = qwq[i]
    se = qwq[i+1]
    if se == fi + 1:
        cout += 1
    else:
        li.append(cout)
        cout = 1
print(max(li))
