import numpy as np
n = int(input())
matrix = [[1 for _ in range(2 ** n)] for _ in range(2 ** n)]


def show(alis: list):
    return print(np.array(alis))


def tran(sx: int, ex: int, sy: int, ey: int) -> int:
    for i in range(sx, int((sx + ex) / 2)):
        for j in range(sy, int((sy + ey) / 2)):
            matrix[i][j] = 0
    if (ex - sx) * (ey - sy) == 4:
        return 0
    return tran(int((ex+sx)/2), ex, sy, int((ey+sy)/2)) + \
        tran(sx, int((ex+sx)/2), int((ey+sy)/2), ey) + \
        tran(int((ex+sx)/2), ex, int((ey+sy)/2), ey)


tran(0, 2**n, 0, 2**n)
"""
for line in matrix:
    for num in line:
        print(num, end=' ')
    print()
"""
show(matrix)
