ini = input().split()
l = int(ini[0])
m = int(ini[1])
the_tree = [0 for i in range(l + 1)]
for _ in range(m):
    num = input().split()
    start = int(num[0])
    end = int(num[1]) + 1
    for i in range(start, end):
        the_tree[i] = 1
tree_number = the_tree.count(0)
print(tree_number)
