a, b, c = map(str, input().split())
if len(a) >= 8:
    print(a, end=' ')
else:
    for n in range(1, 8):
        print(' ', end='')
        if n + len(a) == 8:
            break
    print(a, end=' ')
if len(b) >= 8:
    print(b, end=' ')
else:
    for n in range(1, 8):
        print(' ', end='')
        if n + len(b) == 8:
            break
    print(b, end=' ')
if len(c) >= 8:
    print(c, end=' ')
else:
    for n in range(1, 8):
        print(' ', end='')
        if n + len(c) == 8:
            break
    print(c, end=' ')

