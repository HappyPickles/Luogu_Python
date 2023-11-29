while True:
    n = int(input())
    cout = 1
    key = 1
    v = [1, 1]
    for i in range(1, n+1):
        key *= -1
        for q in range(i):
            if cout == n:
                break
            if key == 1 and v[0] == 1:
                v[1] += 1
            elif key == 1 and v[0] != 1:
                v[1] += 1
                v[0] -= 1
            elif key == -1 and v[1] == 1:
                v[0] += 1
            elif key == -1 and v[1] != 1:
                v[0] += 1
                v[1] -= 1
            cout += 1
    print(str(v[1]) + '/' + str(v[0]))