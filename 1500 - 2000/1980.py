qwq = input().split()
n = int(qwq[0])
x = str(qwq[1])
ans = 0
for i in range(1,n+1):
    number = str(i)
    ans += number.count(x)
print(ans)