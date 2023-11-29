n = int(input())
qwq = list(map(int, input().split()))
qwq = sorted(qwq, key=lambda x: len(str(x)), reverse=False)
qwq = sorted(qwq, key=lambda x: str(x), reverse=True)
ans = ''
for i in qwq:
    ans += str(i)
print(qwq)
print(ans)
