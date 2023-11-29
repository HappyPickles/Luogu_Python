n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(list(set(nums)))
long = len(nums)
if k > long:
    print('NO RESULT')
else:
    print(nums[k-1])
