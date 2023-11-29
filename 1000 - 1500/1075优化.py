n = int(input())
for i in range(2, n-1):
    if (n / i) % 1 == 0:
        print(int(n / i))
        break