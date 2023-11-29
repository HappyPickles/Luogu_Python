import numpy as np
n, k = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
A = np.array(A, dtype='int64')


def array_fast_pow(a: np.ndarray, m: int, mod=0) -> np.ndarray:
    if mod == 0:
        ans_np = np.eye(a.shape[0], dtype='int64')
        while m > 0:
            if m % 2 == 1:
                ans_np *= a
            m = int(m / 2)
            a = np.dot(a, a)
        return ans_np
    else:
        ans_np = np.eye(a.shape[0], dtype='int64') % mod
        while m > 0:
            if m % 2 == 1:
                ans_np = np.dot(ans_np, a) % mod
            m = int(m / 2)
            a = np.dot(a, a) % mod
        return ans_np


ans = array_fast_pow(A, k, 1000000007)
for q in ans:
    for w in q:
        print(w, end=' ')
    print()
