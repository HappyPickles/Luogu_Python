A = int(input())


def only10(s: str) -> bool:
    for wo in s:
        if wo not in ("1", "0"):
            return False
    return True


for B in range(1, 20000000000000):
    ans = str(A*B)
    if only10(ans):
        print(B, end=' ')
        print(ans)
        break
