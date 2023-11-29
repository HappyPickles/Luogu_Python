import numpy as np
T = int(input())
asks = []
for _ in range(T):
    asks.append(int(input().strip()))


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


init_a = np.array([[1, 0, 1], [1, 0, 0], [0, 1, 0]])
for ask in asks:
    print(array_fast_pow(init_a, ask, 1000000007)[1][0])

