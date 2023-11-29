import numpy as np
pi = np.pi
n, m = map(int, list(input().split()))
inpt0 = list(map(int, list(input().split())))
inpt1 = list(map(int, list(input().split())))

l = max(n, m)
var0 = np.fft.fft(inpt0, 4)
var1 = np.fft.fft(inpt1, 4)

print(var0)
print(var1)


