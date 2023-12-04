s_lst = [str(i) for i in range(1, 2024)]
S = ''
for s in s_lst:
    S = S + s
lens = len(S)
dp2 = [0 for _ in range(lens+1)]
dp20 = [0 for _ in range(lens+1)]
dp202 = [0 for _ in range(lens+1)]
dp2023 = [0 for _ in range(lens+1)]

for i in range(lens):
    if S[i] == '2':
        dp2[i] += 1
    dp2[i+1] = dp2[i]
for i in range(lens):
    if S[i] == '0':
        dp20[i] += dp2[i]
    dp20[i+1] = dp20[i]
for i in range(lens):
    if S[i] == '2':
        dp202[i] += dp20[i]
    dp202[i+1] = dp202[i]
for i in range(lens):
    if S[i] == '3':
        dp2023[i] += dp202[i]
    dp2023[i+1] = dp2023[i]
print(dp2023[-1])



def prime_sieve(num):
    is_p = [True for _ in range(num + 3)]
    for i in range(2, int(num**0.5)+1):
        if is_p[i]:
            for j in range(2*i, num+3, i):
                is_p[j] = False
    return is_p


def in_interval(num):
    if 2333 <= num <= 23333333333333:
        return True
    else:
        return False


def sp_func(a, b):
    return int((a**2 * b**2))


big_num = 23333333333333
end_num = int((big_num/4)**0.5) + 1000

is_prime = prime_sieve(end_num)
cont = 0
for p in range(2, end_num):
    if is_prime[p]:
        q_end = int((big_num / (p**2)) ** 0.5) + 100
        for q in range(p, q_end):
            if is_prime[q]:
                if in_interval(sp_func(p, q)) and p != q:
                    cont += 1
print(cont)
