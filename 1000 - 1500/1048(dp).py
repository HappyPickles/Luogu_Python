t, m = map(int, input().split())
T, V = [], []
for _ in range(m):
    tn, va = map(int, input().split())
    T.append(tn)
    V.append(va)
dp = [[0 for _ in range(t+1)] for _ in range(m+1)]

for i in range(m):
    for j in range(t+1):
        if j - T[i] >= 0:
            dp[i+1][j] = max(dp[i][j], dp[i][j - T[i]] + V[i])
        else:
            dp[i+1][j] = dp[i][j]
print(dp[-1][-1])
