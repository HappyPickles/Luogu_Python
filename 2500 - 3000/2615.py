N = int(input())
ans = [[0 for _ in range(N)] for _ in range(N)]
i, j = 0, int(N/2)
ans[i][j] = 1
for k in range(2, (N**2)+1):
    if i == 0 and j != N-1:
        i = N-1
        j += 1
        ans[i][j] = k
        continue

    if j == N-1 and i != 0:
        j = 0
        i -= 1
        ans[i][j] = k
        continue


    if i == 0 and j == N-1:
        i += 1
        ans[i][j] = k
        continue

    if i != 0 and j != N-1:
        if ans[i-1][j+1] == 0:
            i -= 1
            j += 1
        else:
            i += 1
        ans[i][j] = k
        continue

for i in ans:
    for j in i:
        print('%4d' % j, end='')
    print()
