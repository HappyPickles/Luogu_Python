n = int(input())
high = list(map(int, input().split()))
ans = 0
for h in range(1, n-1):
    if high[h-1] <= high[h] > high[h+1]:
        ans += 1
print(ans)

