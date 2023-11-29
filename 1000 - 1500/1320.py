fr = input().strip()
n = len(fr)
qwq = [fr, ]
for i in range(n-1):
    qwq.append(input().strip())

ans = [n, ]
long = ''
for i in qwq:
    long += i

cont = 0
before = long[0]
if long[0] == '1':
    ans.append(0)
for i in range(len(long)):
    if long[i] == before:
        cont += 1
    else:
        before = long[i]
        ans.append(cont)
        cont = 1
ans.append(cont)
for i in ans:
    print(i, end=' ')
