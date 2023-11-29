import math
N, M = list(map(int, input().split()))
square, rectangle = 0, 0
array = math.comb(M+1, 2)*math.comb(N+1, 2)
for i in range(1, min(N, M)+1):
    square += (M+1-i)*(N+1-i)
rectangle = array - square
print(square, rectangle)
