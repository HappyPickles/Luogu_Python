n = int(input())
dirs = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
        '5': 5, '6': 6, '7': 3, '8': 7, '9': 6,
        '+': 2, '=': 2}


for i in range(2000):
    if i not in dirs:
        value = 0
        ans = 0
        for a in str(i):
            ans += dirs[a]
        dirs[str(i)] = ans


equations = [dirs[str(a)] + 2 + dirs[str(b)] + 2 + dirs[str(a+b)] for a in range(1000) for b in range(1000)]

print(equations.count(n))

