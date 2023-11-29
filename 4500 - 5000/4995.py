n = int(input())
stones = sorted([0] + list(map(int, input().split())))
l, r, ans = 0, n, 0
for i in range(n):
    ans += (stones[l] - stones[r]) ** 2
    if i % 2 == 0:
        l += 1
    else:
        r -= 1
print(ans)
