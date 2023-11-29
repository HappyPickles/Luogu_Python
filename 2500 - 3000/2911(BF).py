a, b, c = map(lambda n: int(n)+1, input().split())
dirs = {}
for i in range(1, a):
    for j in range(1, b):
        for k in range(1, c):
            v = i+j+k
            if v not in dirs:
                dirs[v] = 1
            else:
                dirs[v] += 1

print(max(dirs, key= lambda n: dirs[n]))
