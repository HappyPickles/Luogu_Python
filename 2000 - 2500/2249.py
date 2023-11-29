n, m = map(int, input().split())
nums = list(map(int, input().split()))
inpt = list(map(int, input().split()))
memories = {}


def bi_find(x: int):
    if x in memories:
        return memories[x]

    l, r = 0, int(str(n))-1
    mid = int((l+r+1)/2)

    while r - l != 1:

        if nums[mid] >= x:
            r = int((l+r+1)/2)
        elif nums[mid] < x:
            l = int((l+r+1)/2)

        mid = int((l+r+1)/2)

    if nums[l] == x:
        memories[x] = l+1
        return l+1
    if nums[r] == x:
        memories[x] = r+1
        return r+1

    memories[x] = -1
    return -1


for i in inpt:
    print(bi_find(i), end=' ')
