n = int(input())
num = 0
for i in range(n):
    for q in range(n-i):
        num += 1
        if len(str(num)) < 2:
            str_num = '0' + str(num)
        else:
            str_num = str(num)
        print(str_num, end='')
    for w in range(i):
        print('  ', end='')
    print()
