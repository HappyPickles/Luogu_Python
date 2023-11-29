n = int(input())
ans = [n]
for i in range((2**32)-1):
    if n == 1:
        break
    if n % 2 == 1:
        n = (3*n) + 1
    else:
        n = n/2
    ans.append(int(n))
for i in reversed(ans):
    print(i, end=' ')
