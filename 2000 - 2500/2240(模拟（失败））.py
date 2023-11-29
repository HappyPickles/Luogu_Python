N, T = list(map(int, input().split()))
n, t = (N, T)
bag = []
print(t)
for i in range(N):
    gold = list(map(int, input().split()))
    power = gold[1]/gold[0]
    if bag != []:
        bag = sorted(bag, key=lambda x: x[1]/x[0])
        mini = bag[0]
    else:
        mini = [100, 1]
    if t > 0:
        if power >= mini[1]/mini[0]:
            a = min((T-t), gold[0])
            v = [a, a * power]
            bag.append(v)
            t -= min((T-t), gold[0])
        for i in sorted(bag, key=lambda x: x[1]/x[0]):
            pw = i[1]/i[0]
            if pw < power:
                if i[0] < gold[0]:
                    bag.remove(i)
                    t += i[0]
                else:
                    bag.remove(i)
                    t += i[0]
                    i[0] -= i[0]-gold[0]
                    i[1] -= (i[0]-gold[0])*pw
                    bag.append([i[0], i[1]])
                    t -= i[0]
                    bag.append(gold)
                    t -= gold[0]
    elif t <= 0:
        if power <= mini[1]/mini[0]:
            continue
        else:
            for i in sorted(bag, key=lambda x: x[1]/x[0]):
                pw = i[1]/i[0]
                if pw < power:
                    if i[0] < gold[0]:
                        bag.remove(i)
                        t += i[0]
                    else:
                        bag.remove(i)
                        t += i[0]
                        i[0] -= i[0]-gold[0]
                        i[1] -= (i[0]-gold[0])*pw
                        bag.append([i[0], i[1]])
                        t -= i[0]
                        bag.append(gold)
                        t -= gold[0]


ans = 0
for i in bag:
    ans += i[1]
print(ans)
print(bag)
