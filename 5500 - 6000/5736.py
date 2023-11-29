a = input()
qwq = list(map(int, input().split()))
ans = []

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        #  判断是否能被2到 开根号n 整除 不需要判断到n-1
        if n % i == 0:
            return False
    return True


for i in qwq:
    if is_prime(i):
        ans.append(i)

for i in ans:
    print(i, end=' ')
