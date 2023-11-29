ISBN = input()
v = list(ISBN)
isbn = list(ISBN)
while '-' in isbn:
    isbn.remove('-')
while 'X' in isbn:
    isbn.remove('X')
isbn = list(map(int, isbn))
ct = 0
for i in range(1, 10):
    ct += isbn[i-1] * i
key = ct % 11
if key == 10:
    key = 'X'
if ISBN[12] == str(key):
    print('Right')
else:
    v[-1] = str(key)
    ans = ''
    for i in v:
        ans += i
    print(ans)
