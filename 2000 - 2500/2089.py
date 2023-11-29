n = int(input())
init_a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ans = []


def list_i(alis: list, i: int, num: int) -> list:
    v = eval(str(alis))
    v[i] = v[i] + num
    return v


def dfs(i: int, a: list, nums: int) -> int:
    if sum(a) == nums:
        ans.append(a)
        return 0
    if sum(a) > nums:
        return 0
    if i == 10:
        return 0
    if a[i] == 1:
        return dfs(i+1, a, nums) + dfs(i+1, list_i(a, i, 1), nums) + dfs(i+1, list_i(a, i, 2), nums)
    elif a[i] == 2:
        return dfs(i+1, a, nums) + dfs(i+1, list_i(a, i, 1), nums)
    else:
        return dfs(i + 1, a, nums)


dfs(0, init_a, n)
print(len(ans))
for plan in ans:
    for mix in plan:
        print(mix, end=' ')
    print()
