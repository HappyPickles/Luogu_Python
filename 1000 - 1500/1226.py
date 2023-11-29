a, b, p = map(int, input().split())


def fast_pow(m, n, mod=0):
    if mod != 0:  # 不存在对0取模所以用0作为默认参数
        ans = 1 % mod
        while n != 0:
            if n % 2 == 1:
                ans = m * ans % mod
            m *= m % mod
            n = int(n/2)
        return ans
    else:
        ans = 1
        while n != 0:
            if n % 2 == 1:
                ans *= m
            m *= m
            n = int(n / 2)
        return ans


print('%s^%s mod %s=%s' % (a, b, p, fast_pow(a, b, p)))
