xp, yp, x, y = map(int, input().split())
dp = [[0 for _ in range(21)] for _ in range(21)]
dp[0][0] = 1
pony = ((x, y), (x - 2, y - 1), (x - 1, y - 2), (x + 1, y - 2), (x + 2, y - 1),
        (0, 0), (x + 1, y + 2), (x + 2, y + 1), (x - 2, y + 1), (x - 1, y + 2))


for i in range(21):
    for j in range(21):
        if (i, j) not in pony:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[xp][yp])
