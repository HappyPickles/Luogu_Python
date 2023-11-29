N = input()
n = int(N)
# n == 364*x + 1092*k
x = 1
k = 1
for i in range(1,101):
    a = 364 * i + 1092
    if a == n:
        x = i
        break
    if a < n:
        x = i - 1
        for i in range(1, 15):
            a = (364*x)+(i*1092)
            if a == n:
                k = i
                break
        if a == n:
            break
print(x)
print(k)