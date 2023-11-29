r, c = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(r)]
memories = {}


def bfs(i, j):
    ret = 0
    if (i, j) in memories:
        return memories[(i, j)]
    if i > 0 and table[i][j] > table[i-1][j]:
        ret += 1
        bfs(i-1, j)
    if i < r and table[i][j] > table[i+1][j]:
        ret += 1
        bfs(i+1, j)
    if j > 0 and table[i][j] > table[i][j-1]:
        ret += 1
        bfs(i, j-1)
    if j < c and table[i][j] > table[i][j+1]:
        bfs(i, j+1)
    memories[(i, j)] = ret
    return ret

