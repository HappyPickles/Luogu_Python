"""---coding == utf-8 ---"""
import numpy as np


def press(xy, v_matrix):
    def qwq(s):
        if s == 1:
            return 0
        return 1
    x, y = xy[0], xy[1]
    ret = []
    for i in range(3):
        v_press = []
        for j in range(3):
            vn = v_matrix[i][j]
            if i == x and j == y:
                v_press.append(qwq(vn))
                continue
            if i == x-1 and j == y and 0 <= x - 1 <= 2:
                v_press.append(qwq(vn))
                continue
            if i == x+1 and j == y and 0 <= x + 1 <= 2:
                v_press.append(qwq(vn))
                continue
            if i == x and j == y - 1 and 0 <= y - 1 <= 2:
                v_press.append(qwq(vn))
                continue
            if i == x and j == y + 1 and 0 <= y + 1 <= 2:
                v_press.append(qwq(vn))
                continue
            v_press.append(vn)
        ret.append(v_press)
    return ret


def show(vv):
    print(np.array(vv))
    return 0


def right(v_m):
    for i in range(3):
        for j in range(3):
            if v_m[i][j] == 0:
                return False
    return True


def press_by_bin(bins: str, m):
    for b in range(9):
        if bins[b] == '1':
            p = all_lights[b]
            m = press(p, m)
    return m


def nums_of_1(ss: str):
    cont = 0
    for sss in ss:
        if sss == '1':
            cont += 1
    return cont


if __name__ == '__main__':
    matrix = []
    for _ in range(3):
        matrix.append(list(map(int, input().split())))
    all_lights = [(0, 0), (0, 1), (0, 2),
                  (1, 0), (1, 1), (1, 2),
                  (2, 0), (2, 1), (2, 2)]
    ans_list = []
    all_possibilities = []
    #  qwqwq = []
    for num in range(1024, 1536):
        v = '%8s' % str(bin(num))[4:]
        if right(press_by_bin(v, matrix)):
            ans_list.append(nums_of_1(v))
            #  qwqwq.append(v)

    print(min(ans_list))
    #  print(qwqwq)
