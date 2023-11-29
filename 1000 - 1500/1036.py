n, k = map(int, input().split())
qwq = list(map(int, input().split()))


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


def dfs(i: int, nums: int, sums: int) -> int:
    if nums == k:
        if is_prime(sums):
            return 1
    if i+1 > n:
        return 0
    return dfs(i+1, nums+1, sums+qwq[i]) + dfs(i+1, nums, sums)


print(dfs(0, 0, 0))
