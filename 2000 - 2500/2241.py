N, M = list(map(int, input().split()))
square, rectangle = 0, 0
for n in range(1, N+1):
    for m in range(1, M+1):
        if n != m:
            rectangle += (M+1-m)*(N+1-n)
        elif n == m:
            square += (M+1-m)*(N+1-n)
print(square, rectangle)
