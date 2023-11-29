string = ''
for i in range(4):
    string += input()
dirs = {}
for i in range(65, 91):
    dirs[chr(i)] = 0

for i in string:
    if i in dirs:
        dirs[i] += 1

for num in range(max(dirs.values()), 0, -1):
    for i in dirs:
        if dirs[i] >= num:
            print('*', end=' ')
        else:
            print('', end='  ')
    print()
for i in dirs:
    print(i, end='')
    print(' ', end='')
