T = int(input().strip())
asks = []
for _ in range(T):
    asks.append(int(input().strip()))

memories = {1: 1, 2: 1, 3: 1}


def a(x: int) -> int:
    if x in memories:
        return memories[x]
    else:
        ret = a(x-1) + a(x-3)
        memories[x] = ret
        return ret


ans = []
for ask in asks:
    print(a(ask) % 1000000007)
