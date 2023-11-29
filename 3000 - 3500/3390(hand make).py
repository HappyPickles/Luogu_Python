import time
s = time.time()


def matrix_multiplication(a: list, b: list) -> list or str:
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
    for i_mod in range(len(a)):
        for j in range(len(a[0])):
            a[i_mod][j] %= mod
    return a


def array_fast_pow_no_numpy(A_fast: list, n_k: int, s: int, mod=0) -> list:
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


n, k = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
ans = array_fast_pow_no_numpy(A, k, n, 1000000007)
for q in ans:
    for w in q:
        print(w, end=' ')
    print()
e = time.time()
print('cost time(s) == %ss' % (e-s))

