def EuclideanDistance(a, b):
    sums = 0
    for i in range(len(a)):
        sums += (a[i] - b[i])**2
    distance = sums ** 0.5
    return distance


ins = []
for _ in range(3):
    ins.append(list(map(float, input().split())))

ans = 0
ans += EuclideanDistance(ins[0], ins[1])
ans += EuclideanDistance(ins[2], ins[1])
ans += EuclideanDistance(ins[0], ins[2])
print('%.2f' % ans)
