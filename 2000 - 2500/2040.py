"""---coding == utf-8 ---"""
import numpy as np


def press(x: int, y: int, v_matrix):
    v_matrix[x][y] ^= 1
    if 0 <= x - 1 <= 2:
        v_matrix[x - 1][y] ^= 1
    if 0 <= x + 1 <= 2:
        v_matrix[x + 1][y] ^= 1
    if 0 <= y - 1 <= 2:
        v_matrix[x][y - 1] ^= 1
    if 0 <= y + 1 <= 2:
        v_matrix[x][y + 1] ^= 1
    return v_matrix


def show(vv):
    print(np.array(vv))
    return 0


def right(v_m):
    for i in range(3):
        for j in range(3):
            if v_m[i][j] == 0:
                return False
    return True


class Solution:

    def __init__(self):
        self.ans = 0
        self.ans_list = []
        self.matrix = []
        self.cont = 0
        for _ in range(3):
            self.matrix.append(list(map(int, input().split())))


    def main(self, v):
        show(v)
        if self.cont > 20:
            self.cont = 0
            return 0
        elif right(v):
            self.ans_list.append(self.cont)
            self.cont = 0
            return 0
        else:
            self.cont += 1
            return (self.main(press(0, 0, v)) + self.main(press(0, 1, v)) +
                    self.main(press(0, 2, v)) + self.main(press(1, 0, v)) +
                    self.main(press(1, 1, v)) + self.main(press(1, 2, v)) +
                    self.main(press(2, 0, v)) + self.main(press(2, 1, v)) +
                    self.main(press(2, 2, v)))


if __name__ == '__main__':
    s = Solution()
    s.main(s.matrix)
    print(s.ans_list)
