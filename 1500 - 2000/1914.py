n = int(input())
strings = input()
n %= 26
ans = ''
for i in strings:
    if ord(i)+n > 122:
        v = ((ord(i)+n) % 122)
        ans += chr(96 + v)
    else:
        ans += chr(ord(i)+n)
print(ans)
