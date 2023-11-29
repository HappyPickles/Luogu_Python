n = int(input())
memories = {}


def function(x):
    if x in memories:
        return memories[x]
    if x == 1:
        return 2
    else:
        ans = 2*function(x-1) + 2
        memories[x] = ans
        return ans


print(function(n))
