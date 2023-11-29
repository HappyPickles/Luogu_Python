V = int(input())
n = int(input())
alis = []
memorise = {}
for _ in range(n):
    alis.append(int(input()))


def f(i: int, nums: int) -> int:
    if (i, nums) in memorise:
        ret = memorise[(i, nums)]
        return ret
    if i+1 > n:
        ret = nums
        memorise[(i, nums)] = ret
        return ret
    if nums + alis[i] <= V:
        ret = max(f(i+1, nums+alis[i]), f(i+1, nums))
        memorise[(i, nums)] = ret
        return ret
    return f(i+1, nums)


print(V-f(0, 0))
