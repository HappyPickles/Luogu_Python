N = int(input())
l = []
ans = 0
for i in range(N):
    qwq = input().split()
    qwq = list(map(int, qwq))
    l.append(qwq)
for i in range(N):
    i0 = l[0]
    l.remove(i0)
    for i1 in l:
        if abs(int(i0[0]) - int(i1[0])) <= 5 and abs(int(i0[1]) - int(i1[1])) <= 5 and abs(
                int(i0[2]) - int(i1[2])) <= 5 and abs((int(i0[0]) + int(i0[1]) + int(i0[2])) - (int(i1[0]) + int(i1[1])
                                                                                                + int(i1[2]))) <= 10:
            ans += 1
print(ans)
