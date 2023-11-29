qwq = list(map(int, input().split()))
n = qwq[0]
cont = 0
key = 1
for i in range(1, len(qwq)):
    nums = qwq[i]
    for q in range(nums):
        if cont == n:
            print()
            cont = 0
        if key == 1:
            print('0', end='')
            cont += 1
        if key == -1:
            print('1', end='')
            cont += 1
    key *= -1
