#  import numpy as np
table = [[s for s in input()] for _ in range(10)]
#  print(np.array(table))
Ci, Cj = 0, 0
Fi, Fj = 0, 0
for i_f in range(10):
    for j_f in range(10):
        if table[i_f][j_f] == 'C':
            Ci, Cj = i_f, j_f
        if table[i_f][j_f] == 'F':
            Fi, Fj = i_f, j_f

# print(Ci, Cj, Fi, Fj)
direction = ['N', 'E', 'S', 'W']
cow_d = 0
john_d = 0
ans = 0


def cow_turn():
    global cow_d
    if cow_d == 3:
        cow_d = 0
    else:
        cow_d += 1
    return 0


def john_turn():
    global john_d
    if john_d == 3:
        john_d = 0
    else:
        john_d += 1
    return 0


def cow_go():
    global Ci, Cj
    if cow_d == 2:
        if Ci != 9 and table[Ci+1][Cj] != '*':
            Ci += 1
        else:
            cow_turn()
        return 0
    if cow_d == 1:
        if Cj != 9 and table[Ci][Cj+1] != '*':
            Cj += 1
        else:
            cow_turn()
        return 0
    if cow_d == 0:
        if Ci != 0 and table[Ci-1][Cj] != '*':
            Ci -= 1
        else:
            cow_turn()
        return 0
    if cow_d == 3:
        if Cj != 0 and table[Ci][Cj-1] != '*':
            Cj -= 1
        else:
            cow_turn()
        return 0
    return 0


def john_go():
    global Fi, Fj
    if john_d == 2:
        if Fi != 9 and table[Fi+1][Fj] != '*':
            Fi += 1
        else:
            john_turn()
        return 0
    if john_d == 1:
        if Fj != 9 and table[Fi][Fj+1] != '*':
            Fj += 1
        else:
            john_turn()
        return 0
    if john_d == 0:
        if Fi != 0 and table[Fi-1][Fj] != '*':
            Fi -= 1
        else:
            john_turn()
        return 0
    if john_d == 3:
        if Fj != 0 and table[Fi][Fj-1] != '*':
            Fj -= 1
        else:
            john_turn()
        return 0
    return 0


chance = 0
while True:
    civ, cjv, jiv, jjv = Ci, Cj, Fi, Fj
    #  table[Ci][Cj] = '.'
    #  table[Fi][Fj] = '.'
    if [Ci, Cj] == [Fi, Fj]:
        print(ans)
        break
    cow_go()
    john_go()
    #  table[Ci][Cj] = 'C'
    #  table[Fi][Fj] = 'F'
    #  print(Ci, Cj, Fi, Fj)
    #  print(np.array(table))
    ans += 1
    if [civ, cjv] == [Ci, Cj] and [jiv, jjv] == [Fi, Fj]:
        chance += 1
        if chance == 7:
            print(0)
            break
    else:
        chance = 0
