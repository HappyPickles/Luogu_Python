memories = {}
inputs = []


def w(a, b, c):
    ins = (a, b, c)
    if ins in memories:
        return memories[ins]

    if a <= 0 or b <= 0 or c <= 0:
        memories[ins] = 1
        return 1

    if a > 20 or b > 20 or c > 20:
        memories[ins] = w(20, 20, 20)
        return w(20, 20, 20)

    if a < b < c:
        var = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        memories[ins] = var
        return var

    else:
        var = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a-1, b-1, c-1)
        memories[ins] = var
        return var


while 1:
    x, y, z = map(int, input().split())
    inputs.append((x, y, z))
    if [x, y, z] == [-1, -1, -1]:
        break

for i in inputs:
    if i == (-1, -1, -1):
        break
    x, y, z = i
    ans = w(x, y, z)
    print('w(%i, %i, %i) = %i' % (x, y, z, ans))
