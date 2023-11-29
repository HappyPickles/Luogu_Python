n, b = list(map(int, input().split()))
cows = []
for i in range(n):
    cows.append(int(input()))
cows = sorted(cows, reverse=True)
cout = 0
hight = 0
for i in cows:
    cout += 1
    hight += i
    if hight >= b:
        break
print(cout)
