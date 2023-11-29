memories = {0: 1, 1: 1}


def factorial(x: int) -> int:
    if x in memories:
        return memories[x]
    if x < 0:
        return 0
    if x >= 1:
        ans = factorial(x-1) * x
        memories[x] = ans
        return ans


n = int(input())
print(factorial(n))
