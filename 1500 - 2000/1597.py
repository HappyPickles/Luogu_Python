inpt = input()
dirs = {'a': 0, 'b': 0, 'c': 0}
for i in range(0, len(inpt)):
    if inpt[i] == ':' and inpt[i+1] == '=':
        if inpt[i+2] not in ['a', 'b', 'c']:
            dirs[inpt[i-1]] = inpt[i+2]
        else:
            dirs[inpt[i - 1]] = dirs[inpt[i+2]]

print(dirs['a'], end=' ')
print(dirs['b'], end=' ')
print(dirs['c'])
