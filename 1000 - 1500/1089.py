more = 0
income = 0
q = 0
mom = 0
allmom = 0
for i in range(12):
    need = int(input())
    get = 300
    more = get - need + more
    mom = int(more / 100) * 100
    allmom += mom
    if more < 0 :
        print(-(i+1))
        q += 1
        break
    more -= mom
income = more + allmom*1.2
if q != 1:
    print(int(income))