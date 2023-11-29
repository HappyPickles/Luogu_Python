q = int(input())
ans = input().strip()
for _ in range(q):
    var = input().rstrip().split()
    if var[0] == '1':
        ans += var[1]
        print(ans)

    if var[0] == '2':
        left = int(var[1])
        right = int(var[2])
        ans = ans[left:left+right]
        print(ans)

    if var[0] == '3':
        ind = int(var[1])
        ind_str = var[2]
        vl = ans[0:ind]
        vr = ans[ind: len(ans)]
        ans = vl + ind_str + vr
        print(ans)

    if var[0] == '4':
        try:
            print(ans.index(var[1]))
        except:
            print(-1)
