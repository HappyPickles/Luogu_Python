table = [[0, -1, 1, 1, -1],
         [1, 0, -1, 1, -1],
         [-1, 1, 0, -1, 1],
         [-1, -1, 1, 0, 1],
         [1, 1, -1, -1, 0]]
n, na, nb = map(int, input().split())
player0 = list(map(int, input().split()))
player1 = list(map(int, input().split()))
l, r = 0, 0
point0, point1 = 0, 0
for _ in range(n):
    if l == na:
        l = 0
    if r == nb:
        r = 0
    i = player0[l]
    j = player1[r]
    if table[i][j] == 1:
        point0 += 1
    elif table[i][j] == -1:
        point1 += 1
    else:
        pass
    l += 1
    r += 1
print(point0, point1)
