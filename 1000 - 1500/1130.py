N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
dp = [[0 for _ in range(N)] for _ in range(M)]
"""dp[i][j] = min(dp[i-1][j-1], dp[i][j-1]) + lst[i][j] if i != 0"""
"""dp[i][j] = min(dp[M][j-1], dp[i][j-1]) + lst[i][j] if i == 0"""

for qwq in range(M):
    # 初始化dp
    dp[qwq][0] = lst[qwq][0]

for j in range(N):
    for i in range(M):
        if i != 0:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1]) + lst[i][j]
        else:
            dp[i][j] = min(dp[M-1][j - 1], dp[i][j - 1]) + lst[i][j]

ans = dp[M-1][N-1]
for a in range(M-1):
    if dp[a][N-1] < ans:
        ans = dp[a][N-1]

print(ans)
