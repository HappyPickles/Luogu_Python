sen = input()
lower = []
v = []
ans = ''
for i in range(97, 124):
    lower.append(chr(i))
for i in sen:
    if chr(ord(i)) in lower:
        v.append(chr(ord(i) - 32))
    else:
        v.append(i)
for i in v:
    ans += i
print(ans)
