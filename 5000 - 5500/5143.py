import math
n = int(input())
point = []
for i in range(n):
    point.append(list(map(int, input().split())))
point = sorted(point, key=lambda x: x[2])


def EuclideanDistance(a, b):
    sums = 0
    for i in range(len(a)):
        sums += (a[i] - b[i])**2
    distance = math.sqrt(sums)
    return distance


ans = 0
for i in range(n-1):
    ans += EuclideanDistance(point[i], point[i+1])

print('%.3f' % ans)
