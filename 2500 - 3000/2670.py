n, m = list(map(int, input().split()))
alis = []
for i in range(n):
    alis.append(list(input()))


for x in range(n):
    for y in range(m):
        v = alis[x][y]
        if v == '?':
            cont = 0
            for det_x in range(-1, 2):
                for det_y in range(-1, 2):
                    if 0 <= x+det_x < n and 0 <= y+det_y < m:
                        around = alis[x+det_x][y+det_y]
                    else:
                        continue
                    if around == '*':
                        cont += 1
            alis[x][y] = cont

for x in range(n):
    for y in range(m):
        print(alis[x][y], end='')
    print()

