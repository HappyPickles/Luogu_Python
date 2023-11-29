n, m = list(map(int, input().split()))
fuck_things = []
for i in range(n):
    fuck_things.append(int(input()))
if n == m:
    print(sum(fuck_things))
else:
    sums = []
    v = 0
    for i in range(len(fuck_things)-m):
        for q in range(m):
            v += fuck_things[i+q]
        sums.append(v)
        v = 0


    print(min(sums))
