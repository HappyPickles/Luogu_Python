deep = int(input())
qwq = [str(i) for i in range(1, deep+1)]
big_tree = [[str(i)] for i in range(1, deep+1)]


def find(branch, tree):
    for i in qwq:
        if i not in branch:
            tree.append(branch+[i])


for i in big_tree:
    find(i, big_tree)
for i in big_tree:
    i = list(map(int, i))
    if len(i) >= deep:
        for n in range(len(i)):
            if n != len(i)-1:
                print('%5d' % i[n], end='')
            else:
                print('%5d' % i[n])
print(big_tree)
