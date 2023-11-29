n, m, x, y = map(int, input().split())
dp = [[0 for a in range(m + 2)] for b in range(n + 2)]
# 多开一行一列的位置用于严格规避-1下标修改表中内容的情况
print(dp)
dp[-1][0] = 1
t = ((x, y), (x - 2, y - 1), (x - 1, y - 2), (x + 1, y - 2), (x + 2, y - 1),
             (x + 1, y + 2), (x + 2, y + 1), (x - 2, y + 1), (x - 1, y + 2))
for i in range(n + 1):
    for j in range(m + 1):
        if (i, j) not in t:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
print(dp[n][m])
print(dp)
