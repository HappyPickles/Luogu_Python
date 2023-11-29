n = int(input())


def a(x, y):
    ans = x+y
    ret = '%s+%s=%s' % (x, y, ans)
    length = len(ret)
    print(ret)
    print(length)
    return 0


def b(x, y):
    ans = x-y
    ret = '%s-%s=%s' % (x, y, ans)
    length = len(ret)
    print(ret)
    print(length)
    return 0


def c(x, y):
    ans = x*y
    ret = '%s*%s=%s' % (x, y, ans)
    length = len(ret)
    print(ret)
    print(length)
    return 0


key = ''
for _ in range(n):
    var = input().split()
    if len(var) == 3:
        x = int(var[1])
        y = int(var[2])

        if var[0] == 'a':
            a(x, y)
            key = var[0]
        if var[0] == 'b':
            b(x, y)
            key = var[0]
        if var[0] == 'c':
            c(x, y)
            key = var[0]
    elif len(var) == 2:
        x = int(var[0])
        y = int(var[1])
        if key == 'a':
            a(x, y)
        if key == 'b':
            b(x, y)
        if key == 'c':
            c(x, y)
