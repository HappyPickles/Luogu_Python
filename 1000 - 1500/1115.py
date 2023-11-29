n = int(input())
nums = list(map(int, input().split()))
dp = [0 for _ in range(n)] + [-1145141919810]
for i in range(n):
    dp[i] = max(dp[i-1]+nums[i], nums[i])
print(max(dp))
