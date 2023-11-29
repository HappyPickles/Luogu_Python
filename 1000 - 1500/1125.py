word = input()
d = {}
for i in word:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
maxn = max(d.values())
minn = min(d.values())
ans = maxn-minn


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        #  判断是否能被2到 开根号n 整除 不需要判断到n-1
        if n % i == 0:
            return False
    return True


if is_prime(ans):
    print('Lucky Word')
    print(ans)
else:
    print('No Answer')
    print(0)
