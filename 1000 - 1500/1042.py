string = ''
while 1:
    v = input().strip()
    string += v
    if 'E' in v:
        break

L = 0
R = 0
for i in string:
    if i == 'W':
        L += 1
    if i == 'L':
        R += 1
    if L >= 11 or R >= 11:
        if abs(L-R) > 1:
            print('%s:%s' % (L, R))
            L, R = 0, 0
    if i == 'E':
        print('%s:%s' % (L, R))
        L, R = 0, 0
        break
print()
for i in string:
    if i == 'W':
        L += 1
    if i == 'L':
        R += 1
    if L >= 21 or R >= 21:
        if abs(L-R) > 1:
            print('%s:%s' % (L, R))
            L, R = 0, 0
    if i == 'E':
        print('%s:%s' % (L, R))
        L, R = 0, 0
        break
