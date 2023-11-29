n = int(input())
memory = {}


def f(x: int) -> int:
    if x in memory:
        return memory[x]
    if x in (0, 1):
        memory[x] = 1
        return 1
    else:
        ans = 1
        for i in range(1, (x//2)+1):
            ans += f(i)
        memory[x] = ans
        return ans


print(f(n))
print(memory)
