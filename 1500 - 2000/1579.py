n = int(input())

sieve = [False, False]+[True for _ in range(20000)]
for num in range(20002):
    if sieve[num] is True:
        for qwq in range(num**2, 20002):
            if qwq % num == 0:
                sieve[qwq] = False

ans = []
key = True
for i in range(2, 20001):
    if key is False:
        break
    if sieve[i]:
        for j in range(2, 20001):
            if key is False:
                break
            if sieve[j]:
                k = n - i - j
                if 2 <= k <= 20000:
                    if sieve[k]:
                        ans.append([i, j, k])
                        key = False

for i in ans[0]:
    print(i, end=' ')
