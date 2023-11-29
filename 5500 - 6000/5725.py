n = int(input())
last = n*n
count = 0
for i in range(1, last+1):
    num = str(i)
    if len(num) < 2:
        num = '0' + num
    if (i-1) % n == 0 and (i-1) != 0:
        print()
    print(num, end='')
print('\n')
nothing = '  '
for i in range(1, n+1):
    for q in range(n-i):
        print(nothing, end='')
    for w in range(i):
        count += 1
        if len(str(count)) < 2:
            qwq = '0' + str(count)
        else:
            qwq = str(count)
        print(qwq, end='')
    print()
