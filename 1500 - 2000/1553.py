s = input()
a, b, c = ['.', '/', '%']
if a in s:
    v = s.index(a)
    ints = s[0:v]
    floats = s[v+1: len(s)+1]
    if s[v+1] != '0':
        print(str(int(ints[::-1])) + a + str(int(floats[::-1])))
    else:
        fanzuan = floats[1:len(floats)]
        if fanzuan:
            print(str(int(ints[::-1])) + a + str(int(fanzuan[::-1])))
        else:
            print(str(int(ints[::-1])) + a + '0')
if b in s:
    v = s.index(b)
    up = s[0:v]
    down = s[v+1: len(s)+1]
    print(str(int(up[::-1])) + b + str(int(down[::-1])))
if c in s:
    v = s.index(c)
    l = s[0: v]
    print(str(int(l[::-1])) + c)
if a not in s and b not in s and c not in s:
    print(str(int(s[::-1])))
