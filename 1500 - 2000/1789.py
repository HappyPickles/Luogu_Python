nmk = input().split()
n, m, k = int(nmk[0]), int(nmk[1]), int(nmk[2])
fire = []
fluorite = []
matrix = [(x, y) for x in range(1, 1+n) for y in range(1, 1+n)]
matrix_remove = []

for i in range(0, m):
    fire.append(list(map(int, input().split())))

for i in range(0, k):
    fluorite.append(list(map(int, input().split())))


def ManhattanDistance(q, w):
    distance = int(abs(q[0]-w[0])+abs(q[1]-w[1]))
    return distance


def ChevDistance(e, r):
    distance = int(max(abs(e[0]-r[0]), abs(e[1]-r[1])))
    return distance


for i in fire:
    for z in matrix:
        if ManhattanDistance(z, i) < 3:
            matrix_remove.append(z)

for i in fluorite:
    for z in matrix:
        if ChevDistance(z, i) < 3:
            matrix_remove.append(z)

for i in matrix_remove:
    if i in matrix:
        matrix.remove(i)

print(len(matrix))
