n = int(input())


def even_num(x):
    if x != 0:
        return (x % 2) ^ 1
    else:
        return 1


def mark(x):
    if 4 < x <= 12:
        return 1
    else:
        return 0


if even_num(n) == 1 and mark(n) == 1:
    print(1, end=' ')
else:
    print(0, end=' ')
if even_num(n) == 1 or mark(n) == 1:
    print(1, end=' ')
else:
    print(0, end=' ')
if even_num(n) ^ mark(n) == 1:
    print(1, end=' ')
else:
    print(0, end=' ')
if even_num(n) != 1 and mark(n) != 1:
    print(1, end=' ')
else:
    print(0, end=' ')
