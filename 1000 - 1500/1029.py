def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


x, y = map(int, input().split())
multi = x*y
cont = 0

for i in range(1, int((multi**0.5)+1)):
    if (multi/i) % 1 == 0:
        j = (multi/i)
        if gcd(i, j) == x:
            cont += 2
if x == y:
    cont = 1
print(cont)
