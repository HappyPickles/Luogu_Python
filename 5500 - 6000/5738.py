n, m = map(int, input().split())
nums = []


def get_point(alis: list) -> float:
    alis.remove(max(alis))
    alis.remove(min(alis))
    an = sum(alis)/(m-2)
    return an


ans = []
for _ in range(n):
    lis = list(map(float, input().split()))
    ans.append(get_point(lis))
r_ans = max(ans)
print('%.2f' % r_ans)
