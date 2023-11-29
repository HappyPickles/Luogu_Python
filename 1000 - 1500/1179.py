l, r = map(int, input().split())
ans = 0
for i in range(l, r+1):
    qwq = str(i)
    for q in qwq:
        if q == '2':
            ans += 1

print(ans)
