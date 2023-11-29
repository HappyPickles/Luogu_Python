n = int(input())
people = []
for _ in range(n):
    people.append(input().split())


def del_EXP(p):
    ret = p[0] + ' ' + p[1] + ' ' + p[3]
    return ret


position = ['HuFa' for _ in range(2)] + ['ZhangLao' for _ in range(4)] + \
           ['TangZhu' for _ in range(7)] + ['JingYing' for _ in range(25)]

rule = {'BangZhu': 0, 'FuBangZhu': 1, 'HuFa': 2, 'ZhangLao': 3,
        'TangZhu': 4, 'JingYing': 5, 'BangZhong': 6}


if n <= 3:
    for p in people:
        print(del_EXP(p))
else:
    bangzhu = people[0:3]
    unbangzhu = people[3:]
    unbangzhu = sorted(unbangzhu, key=lambda x: int(x[3]), reverse=True)
    unbangzhu = sorted(unbangzhu, key=lambda x: rule[x[1]])
    unbangzhu = sorted(unbangzhu, key=lambda x: int(x[2]), reverse=True)
    length = len(unbangzhu)

    if length > len(position):
        for i in range(len(position)):
            if unbangzhu[i][1] == position[i]:
                continue
            unbangzhu[i][1] = position[i]

        for i in range(len(position), len(unbangzhu)):
            unbangzhu[i][1] = 'BangZhong'
    else:
        for i in range(len(unbangzhu)):
            unbangzhu[i][1] = position[i]


    unbangzhu = sorted(unbangzhu, key=lambda x: int(x[3]), reverse=True)
    unbangzhu = sorted(unbangzhu, key=lambda x: rule[x[1]])
    ans = bangzhu + unbangzhu

    for qwq in ans:
        print(del_EXP(qwq))
