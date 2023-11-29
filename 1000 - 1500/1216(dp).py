r = int(input())
nums = []
dp = []
for m in range(1, r+1):
    nums.append(list(map(int, input().split())))
    dp.append([0 for _ in range(m)])

dp[0][0] = nums[0][0]
for i in range(1, r):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + nums[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + nums[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + nums[i][j]
print(max(dp[r-1]))
