N = input()
n = int(N)
num = n/364
more = num % 3
x0 = int(more)
k0 = int((num - more) / 3)
for i in range(100):
    if k0 == 1 or x0 >= 97:
        break
    k0 -= 1
    x0 += 3
print(x0)
print(k0)