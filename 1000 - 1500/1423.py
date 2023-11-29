far = float(input())
s = float(2)
steps = 0
for i in range(2**16):
    far -= s
    steps += 1
    if far <= 0:
        break
    s *= 0.98
print(steps)
