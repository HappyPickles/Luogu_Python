n = input().split()
a, b, c = int(n[0]), int(n[1]), int(n[2])
up = min(a, b, c)
down = max(a, b, c)
v = 1
for i in range(1, down):
    if (up/i) %1 == 0 and (down/i) %1 == 0:

        v = i
up = str(int(up / v))
down = str(int(down / v))
print(up+'/'+down)
