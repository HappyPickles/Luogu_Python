n = int(input())
alis = []
cont = 1
for i in range(n):
    alis.append(list(map(int, input().split()))+[cont])
    cont += 1
find = list(map(int, input().split()))
key = 0
for i in range(n-1, -1, -1):
    v = alis[i]
    for det_x in range(v[2]):
        x = v[0]+det_x
        for det_y in range(v[3]):
            y = v[1]+det_y
            if find[0] == x and find[1] == y:
                print(v[4])
                key += 1
                break
            break
        break

if key == 0:
    print(-1)

