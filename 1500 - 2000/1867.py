n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(float, input().split())))

life = 10.0
det = 0.0001
exps = 0
for do in lst:
    reduce, exp = do[0], do[1]
    if life - reduce >= 10:
        life = 10
    else:
        life -= reduce
    if life > det:
        exps += exp
    else:
        break

lv = 0
for i in range(0, 21):
    if exps >= 2**i:
        lv += 1
        exps -= 2**i
    else:
        break

print(lv, int(exps))


