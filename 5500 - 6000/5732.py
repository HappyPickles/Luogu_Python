while True:
    n = int(input())
    yang_hui = []
    fr = [1]


    def yanghui(x, n):
        if n == 1:
            return x
        l = len(x)
        v = []
        for i in range(l + 1):
            if i == 0 or i == l:
                v.append(1)
            else:
                v.append(x[i-1] + x[i])
        if len(v) == n:
            return v
        else:
            return yanghui(v, n)


    ans = []
    for i in range(1, n+1):
        ans.append(yanghui(fr, i))

    for i in ans:
        for q in i:
            print(q, end=' ')
        print()

