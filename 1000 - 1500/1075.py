n = int(input())
import time
time_start = time.time()
for i in range(n-1, 1, -1):
    if (n / i) % 1 == 0:
        print(i)
        break
time_end = time.time()
time_c = time_end - time_start
print('time cost', time_c, 's')
