import numpy as np
np.set_printoptions(suppress=True)
"""A*B = IFFT(FFT(A)*FFT(B))"""
a = int(input())
b = int(input())
c = np.array([a])
d = np.array([b])
ans = np.fft.ifft(np.fft.fft(c)*np.fft.fft(d))
print(int(ans[0].real))
print(a*b)
