w, x, h = map(int, input().split())
q = int(input())
cuts = []
for _ in range(q):
    cuts.append(list(map(int, input().split())))
block = [[[1 for _ in range(h)] for _ in range(x)] for _ in range(w)]
ans = w * x * h

for cut in cuts:
    x1, y1, z1, x2, y2, z2 = cut
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            for k in range(z1-1, z2):
                if block[i][j][k] == 1:
                    ans -= 1
                    block[i][j][k] = 0

print(ans)
