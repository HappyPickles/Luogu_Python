n = int(input())
ax = input().split()
for a in range(n, -1, -1):
    i = ax[n-a]
    if a == n:
        if int(i) != 0:
            print(i + 'x^' + str(a), end='')
        else:
            print('', end='')
    if a != n and a == 0:
        if int(i) > 0:
            print('+' + i)
        elif int(i) == 0:
            print('', end='')
        else:
            print(i, end='')
    if a != n and a != 0:
        if int(i) > 0 and int(i) != 1:
            print('+' + i + 'x^' + str(a), end='')
        elif int(i) == 0:
            print('', end='')
        elif int(i) == 1:
            print('+' + 'x^' + str(a), end='')
        elif int(i) == -1:
            print('-' + 'x^' + str(a), end='')
        else:
            print(i + 'x^' + str(a), end='')
