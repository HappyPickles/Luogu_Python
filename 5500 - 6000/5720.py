a = int(input())
if a == 1:
    print(1)
else:
    for i in range(1, 2**32):
        a = int(a / 2)
        if a == 1:
            print(i+1)
            break