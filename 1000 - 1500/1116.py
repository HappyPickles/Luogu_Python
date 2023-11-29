n = int(input())
qwq = list(map(int, input().split()))
cont = []


def bubble_sort(x):
    for i in range(len(x)-1):
        fi, se = x[i], x[i+1]
        if fi > se:
            x[i+1] = fi
            x[i] = se
            cont.append([1])
    for i in range(len(x)-1):
        fi, se = x[i], x[i+1]
        if fi > se:
            bubble_sort(x)
    return len(cont)


print(bubble_sort(qwq))
