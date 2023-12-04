n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]
s = students[::]


def a(stu):
    return stu[0] + stu[1]


def b(stu):
    return sum(stu)


ans = sorted(s, key=a)
ans = sorted(ans, key=b)
ret = 0
add = 0
for i in range(n):
    if i != 0:
        add += a(ans[i]) + ans[i-1][-1]
    else:
        add += a(ans[i])
    ret += add
print(ret)
