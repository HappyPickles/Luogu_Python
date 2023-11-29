n = int(input())
act = []
for i in range(n):
    act.append(list(map(float, input().split())))

lights = [0 for i in range(2000000)]
for work in act:
    a = work[0]
    for t in range(1, int(work[1])+1):
        labs = int(a*t)-1
        if lights[labs]:
            lights[labs] = 0
        else:
            lights[labs] = 1

print(lights.index(1)+1)

"""n = int(input())
act = []
for i in range(n):
    act.append(list(map(float, input().split())))

lights = {}
for work in act:
    a = work[0]
    for t in range(1, int(work[1])+1):
        labs = int(a*t)
        if str(labs) not in lights:
            lights[str(labs)] = 1
        else:
            lights[str(labs)] += 1

for labs in lights:
    if lights[labs] % 2 == 1:
        print(labs)
        break
"""