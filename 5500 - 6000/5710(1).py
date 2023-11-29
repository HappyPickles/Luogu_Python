n = int(input())

if n % 2 == 0 and 4 < n <= 12:
    print(1, end=' ')
else:
    print(0, end=' ')

if n % 2 == 0 or 4 < n <= 12:
    print(1, end=' ')
else:
    print(0, end=' ')

if n % 2 == 0 or 4 < n <= 12:
    if not(n % 2 == 0 and 4 < n <= 12):
        print(1, end=' ')
    else:
        print(0, end=' ')
else:
    print(0, end=' ')

"""if n % 2 != 0:
    if n <= 4 or n > 12:
        print(1, end=' ')
    else:
        print(0, end=' ')
else:
    print(0, end=' ')
"""

