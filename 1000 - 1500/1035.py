k = input()
s = 0
for n in range(1,2**16):
    s += 1/n
    if float(s)>float(k):
        break
print(n)