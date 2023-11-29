def huiwen(s: str):
    if s == s[::-1]:
        return True
    return False


n = int(input())
ans = []
for i in range(n):
    line = input()
    lens = len(line)
    for long in range(lens, 0, -1):
        if len(ans) == i+1:
            continue
        l = 0
        r = long
        """a[l:r], l+r == long"""
        for num in range(lens+1-long, 0, -1):
            if huiwen(line[l:r]):
                ans.append(len(line[l:r]))
                break
            l += 1
            r += 1

for i in ans:
    print(i)
