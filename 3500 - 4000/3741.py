n = int(input())
s = input().strip('\r')
if n <= 1:
    print(0)
elif n == 2:
    if s == "KK":
        print(2)
    else:
        print(1)
else:
    v = s.count('VK')
    key = 0
    if s.count('VV') > s.count('VVK') > 0 or s.count('KK') >= 1:
        key = 1
        print(v+key)
    else:
        print(v)
