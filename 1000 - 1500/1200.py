star = input()
cout = 1
for i in star:
    v = ord(i)
    v = v - 64
    cout *= v
cout = cout % 47

team = input()
cont = 1
for i in team:
    v = ord(i)
    v = v - 64
    cont *= v
cont %= 47

if cout == cont:
    print('GO')
else:
    print('STAY')
