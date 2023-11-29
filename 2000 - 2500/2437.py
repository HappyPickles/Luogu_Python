m, n = map(int, input().split())
dp = [1, 1] + n * [0]
for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n-m])
