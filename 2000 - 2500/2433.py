question = input()
num = int(question)


def f(x):
    if x == 1:
        print('I love Luogu!')
    if x == 2:
        print('6 4')
    if x == 3:
        print('3')
        print('12')
        print('2')
    if x == 4:
        L = 500 / 3
        print(round(L, 3))
    if x == 5:
        l0 = 260
        l1 = 220
        t = 480/32
        print(int(t))
    if x == 6:
        q = pow((6**2 + 9**2), 1/2)
        print('%.4f' % q)
    if x == 7:
        money = 100
        print(money+10)
        print(money+10-20)
        print(money-money)
    if x == 8:
        r = 5
        pi = 3.141593
        w0 = 2 * pi * r
        w1 = pi * r * r
        w2 = 4 / 3 * pi*r*r*r
        print('%.4f' % w0)
        print('%.4f' % w1)
        print('%.3f' % w2)
    if x == 9:
        end = 1
        print(22)
    if x == 10:
        print(9)
    if x == 11:
        print(33.3333)
    if x == 12:
        print(13)
        print('R')
    if x == 13:
        r0 = 4
        r1 = 10
        V = (4/3*3.141593*r0*r0*r0) + (4/3*3.141593*r1*r1*r1)
        block = int(pow(V,1/3))
        print(block)
    if x == 14:
        price = 110
        people = 10
        way = []
        for i in range(111):
            qian = price * people
            if qian == 3500 :
                way.append(price)
            price -= 1
            people += 1
        print(int(min(way)))
    return 0


f(num)
