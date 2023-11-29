n, m = map(int, input().split())
price = list(map(int, input().split()))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]


for i in range(n):
    for j in range(n):
        if dp[i][j] + price[i] <= m:
            dp[i+1][j] = dp[i][j] + price[i]
        else:
            dp[i+1][j] = dp[i][j]
print(dp)
