import time
time_start = time.time()
def is_prime(n):
    if n <= 1:
        return False
    #  素数的定义，除1以外的自然数
    for i in range(2, int(n**0.5) + 1):
        #  判断是否能被2到 开根号n 整除 不需要判断到n-1
        if n % i == 0:
            return False
    return True

Primetable = []
for i in range(1, 100000):
    if is_prime(i) == 1:
        Primetable.append(i)

print(Primetable)
time_end = time.time()
time_c = time_end - time_start
print('time cost', time_c, 's')
