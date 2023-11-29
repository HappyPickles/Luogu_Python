abc = input().split()
a, b, c = int(abc[0]), int(abc[1]), int(abc[2])
qwq = [a, b, c]
qwq = sorted(qwq)
short = qwq[0]
mid = qwq[1]
long = qwq[2]
if a >= b+c or b >= a+c or c >= a+b:
    print('Not triangle')
else:
    if a**2 == (b**2 + c**2) or b**2 == (a**2 + c**2) or c**2 == (b**2 + a**2):
        print('Right triangle')
    if short**2 + mid**2 > long**2:
        print('Acute triangle')
    if short**2 + mid**2 < long**2:
        print('Obtuse triangle')
    if a == b or b == c or a == c:
        print('Isosceles triangle')
    if a == b == c:
        print('Equilateral triangle')
