Encrypted = input().strip()
Original = input().strip()
Untranslated = input().strip()

ABC = [chr(i) for i in range(65, 65+26)]
values = [0 for _ in range(26)]
translate = dict(zip(ABC, values))
Failed = 0
for i in range(len(Encrypted)):
    S = Encrypted[i]
    if translate[S] == 0:
        translate[S] = Original[i]
    elif translate[S] == Original[i]:
        pass
    else:
        Failed = 1
        break

if 0 in translate.values():
    Failed = 1
for ab in range(65, 65+26):
    if chr(ab) not in translate.values():
        Failed = 1
        break

if Failed == 1:
    print('Failed')
else:
    for j in Untranslated:
        print(translate[j], end='')
