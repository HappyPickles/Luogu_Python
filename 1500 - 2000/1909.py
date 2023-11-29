n = int(input())
cost = []
for i in range(3):
    qwq = input().split()
    need = n/int(qwq[0])
    if need != int(need):
        need = int(need) + 1
    cost.append(int(qwq[1])*need)
print(int(min(cost)))