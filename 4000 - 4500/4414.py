qwq = list(map(int, input().split()))
b = 0
for i in qwq:
    if i != max(qwq) and i != min(qwq):
        b = i
ABC = input()
for i in ABC:
    if i == 'A':
        print(min(qwq), end=' ')
    if i == 'B':
        print(b, end=' ')
    elif i == 'C':
        print(max(qwq), end=' ')
