n = int(input())
dp = [1, 1] + [0 for _ in range(n-1)]
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
