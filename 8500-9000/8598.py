N = int(input())
nums = []
for _ in range(N):
    nums += list(map(int, input().split()))
nums = sorted(nums)
same = 0
less = 0
for i in range(len(nums)-1):
    if nums[i] + 2 == nums[i+1]:
        less = nums[i] + 1

    if nums[i] == nums[i+1]:
        same = nums[i]

print(less, same)
