import numpy as np
n = int(input())
inputs = []
for _ in range(n):
    str_s = input().strip()
    v = []
    for i in str_s:
        if i == '@':
            v.append(1)
        else:
            v.append(0)
    inputs.append(v)
inputs = np.array(inputs)

needs = []
for _ in range(n):
    str_s = input().strip()
    v = []
    for i in str_s:
        if i == '@':
            v.append(1)
        else:
            v.append(0)
    needs.append(v)
needs = np.array(needs)


def rotate90(a1: np.ndarray) -> np.ndarray:
    b1 = np.rot90(a1, 1)
    return b1


def rotate180(a2: np.ndarray) -> np.ndarray:
    b2 = np.rot90(a2, 2)
    return b2


def rotate270(a3: np.ndarray) -> np.ndarray:
    b3 = np.rot90(a3, -1)
    return b3


def reflex(ar: np.ndarray) -> np.ndarray:
    var = np.zeros(ar.shape, dtype=int)
    x, y = ar.shape
    for i_r in range(x):
        for j in range(y):
            var[i_r][j] = int(ar[i_r][y-j-1])
    return var


def com_plex(ar: np.ndarray) -> list:
    qwq = []
    var = reflex(ar)
    qwq.append(rotate90(var))
    qwq.append(rotate180(var))
    qwq.append(rotate270(var))
    return qwq


def nothing(ar):
    return ar


def same(a: np.ndarray, b: np.ndarray) -> bool:
    x, y = a.shape
    for i_s in range(x):
        for j_s in range(y):
            if a[i_s][j_s] != b[i_s][j_s]:
                return False
    return True


def My_litter_Pony(ar: np.ndarray, ara: np.ndarray) -> int:
    if same(rotate90(ar), ara):
        return 1
    if same(rotate180(ar), ara):
        return 2
    if same(rotate270(ar), ara):
        return 3
    if same(reflex(ar), ara):
        return 4
    for ars in com_plex(ar):
        if same(ars, ara):
            return 5
    if same(nothing(ar), ara):
        return 6
    return 7


print(My_litter_Pony(inputs, needs))
