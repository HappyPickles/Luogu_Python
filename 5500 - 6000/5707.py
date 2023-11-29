sv = input().split()
s = int(sv[0])
v = int(sv[1])
time = s/v
if time % 1 != 0:
    time = int(time) + 1
time += 10
time = int(time)
if time < 480:
    h = time // 60
    m = 60 - (time % 60)
    if m == 60:
        m = 0
    if len(str(m)) < 2:
        m = '0' + str(m)
    else:
        m = str(m)
    h = 7 - h
    if len(str(h)) < 2:
        h = '0' + str(h)
    else:
        h = str(h)
    print(h + ':' + m)

if time == 480:
    print('00:00')

if time > 480:
    time -= 480
    h = int(time // 60)
    m = int(60 - (time % 60))
    if m == 60:
        m = 0
    if len(str(m)) < 2:
        m = '0' + str(int(m))
    else:
        m = str(int(m))
    h = 23 - h
    if len(str(int(h))) < 2:
        h = '0' + str(int(h))
    else:
        h = str(int(h))
    print(h + ':' + m)
