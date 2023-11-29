x, n = list(map(int, input().split()))
ans = 1
for i in range(n):
    ans += ans * x
print(ans)
