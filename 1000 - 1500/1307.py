n = input()
l0 = []
ans = ''
if int(n) != 0:
    for i in n:
        l0.append(i)
    l0 = l0[::-1]
    for i in l0:
        if i != '-':
            ans += i
    if int(n) < 0:
        print(-int(ans))
    else:
        print(int(ans))
else:
    print(0)
