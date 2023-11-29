# -*- coding:utf-8 -*-
# Author:Maxx1797


def matrix_multiplication(b: list, a: list) -> list or str:
    # TODO remake
    line = len(a[0])
    row = len(b)
    if line != row:
        return print('error input')
    else:
        ans_multi = []
        for vx in range(len(a)):  # ans's row
            v = []
            for vy in range(len(b[0])):  # ans's line
                var = 0
                for i_multi in range(line):
                    var += a[vx][i_multi] * b[i_multi][vy]
                v.append(var)
            ans_multi.append(v)
        return ans_multi


def eyes_array(r: int) -> list:
    # TODO Simplify
    ans_eye = []
    for i_eye in range(r):
        row = []
        for q_eye in range(r):
            if q_eye == i_eye:
                row.append(1)
            else:
                row.append(0)
        ans_eye.append(row)
    return ans_eye


def array_mod(a: list, mod: int) -> list:
    # TODO Simplify
    for i_mod in range(len(a)):
        for j in range(len(a[0])):
            a[i_mod][j] %= mod
    return a


def array_fast_pow_no_numpy(A_fast: list, n_k: int, mod=0) -> list:
    s = len(A_fast)
    if mod == 0:
        ans_fast = eyes_array(s)
        while n_k > 0:
            if n_k % 2 == 1:
                ans_fast = matrix_multiplication(ans_fast, A_fast)
            n_k = int(n_k / 2)
            A_fast = matrix_multiplication(A_fast, A_fast)
        return ans_fast
    else:
        ans_fast = eyes_array(s)
        while n_k > 0:
            if n_k % 2 == 1:
                ans_fast = array_mod(matrix_multiplication(ans_fast, A_fast), mod)
            n_k = int(n_k / 2)
            A_fast = array_mod(matrix_multiplication(A_fast, A_fast), mod)
        return ans_fast



if __name__ == '__main__':
    n = int(input())
    base_mat = [[1, 1], [1, 0]]
    init_mat = [1, 1]
    """
    def fast_pow(A: np.ndarray, k: int, mod=0):
        ret = np.eye(A.shape[0], A.shape[1])
        if mod == 0:
            while k > 0:
                if k % 2 == 1:
                    ret = np.dot(ret, A)
                k = int(k/2)
                A = np.dot(A, A)
            return ret
        else:
            mod_mat = np.ones(A.shape) * mod
            while k > 0:
                if k % 2 == 1:
                    ret = np.dot(ret, A)
                    ret %= mod_mat
                k = int(k/2)
                A = np.dot(A, A) % mod_mat
            return ret
    """
    def solution(x):
        if x >= 3:
            ret = matrix_multiplication(init_mat, array_fast_pow_no_numpy(base_mat, x-2, mod=(10**9)+7))
            return ret
        else:
            return 1


    print(solution(n))
