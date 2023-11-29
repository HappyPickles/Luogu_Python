a = input()
nums = {'0': ('XXX', 'X.X', 'X.X', 'X.X', 'XXX'), '1': ('..X', '..X', '..X', '..X', '..X'),
        '2': ('XXX', '..X', 'XXX', 'X..', 'XXX'), '3': ('XXX', '..X', 'XXX', '..X', 'XXX'),
        '4': ('X.X', 'X.X', 'XXX', '..X', '..X'), '5': ('XXX', 'X..', 'XXX', '..X', 'XXX'),
        '6': ('XXX', 'X..', 'XXX', 'X.X', 'XXX'), '7': ('XXX', '..X', '..X', '..X', '..X'),
        '8': ('XXX', 'X.X', 'XXX', 'X.X', 'XXX'), '9': ('XXX', 'X.X', 'XXX', '..X', 'XXX'),
        '.': ('.', '.', '.', '.', '.')}
b = input()
b = '.'.join(list(b))
for j in range(5):
    for i in b:
        print(nums[i][j], end='')
    print()
