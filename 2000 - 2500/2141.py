n = int(input())
al = list(map(int, input().split()))
ans = []
for q in al:
    for w in al:
        if w == q:
            continue
        for e in al:
            if e == w:
                continue
            if e + w == q:
                v = [w, e]
                if sorted(v) not in ans:
                    ans.append(sorted(v))
real = []
for i in ans:
    v = i[0]+i[1]
    if v not in real:
        real.append(v)
    else:
        continue
print(len(real))




