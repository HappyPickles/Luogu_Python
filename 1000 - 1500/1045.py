import math

p = int(input())


def fast_pow(a, n):
    var = 1
    while n > 0:
        if n % 2 == 1:
            var *= a
        a *= a
        n = int(n / 2)
    return var


ans = fast_pow(2, p) - 1
l: int = int(math.log10(ans)) + 1
print(l)
ans %= fast_pow(10, 501)
f = []
for i in range(500):
    f.append(ans % 10)
    ans //= 10
for i in range(500 - 1, -1, -1):
    print('%d' % f[i], end='')
    if i % 50 == 0:
        print()
