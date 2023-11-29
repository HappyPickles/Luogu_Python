n = int(input())
nums = [[0 for _ in range(n)] for _ in range(n)]
cont = 0
i, j = 0, -1

while cont < n**2:
    while j+1 < n and nums[i][j+1] == 0:
        cont += 1
        j += 1
        nums[i][j] = cont
    while i+1 < n and nums[i+1][j] == 0:
        cont += 1
        i += 1
        nums[i][j] = cont
    while j-1 < n and nums[i][j-1] == 0:
        cont += 1
        j -= 1
        nums[i][j] = cont
    while i-1 < n and nums[i-1][j] == 0:
        cont += 1
        i -= 1
        nums[i][j] = cont

for i in nums:
    for j in i:
        print('%3d' % j, end='')
    print('')
