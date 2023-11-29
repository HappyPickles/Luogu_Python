T, M = map(int, input().split())
lief = [[0, 0]]
for i in range(M):
    lief.append(list(map(int, input().split())))


memories = {}


def f(k: int, t: int) -> int:
    # 记忆化
    tk = lief[k][0]
    vk = lief[k][1]
    if (k, t) in memories:
        return memories[(k, t)]
    else:
        if t == 0 or k == 0:
            ans = 0
        elif t >= tk:
            ans = max(f(k-1, t-tk) + vk, f(k-1, t))
        else:
            ans = f(k-1, t)
    memories[(k, t)] = ans
    return ans


print(f(M, T))
