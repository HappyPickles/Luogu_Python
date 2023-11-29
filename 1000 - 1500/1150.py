n, k = map(int, input().split())
ans = n
more = n
while more >= k:
    more -= (k-1)
    ans += 1
print(ans)
