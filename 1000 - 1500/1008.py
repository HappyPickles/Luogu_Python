import time
num = list(i for i in range(1, 10))
nums = []

time_start = time.time()
f, s, t = 0, 0, 0
for i in num:
    f = i
    for i in num:
        if i == f:
            continue
        s = i
        for i in num:
            if i == s or i == f:
                continue
            t = i
            qwq = int(str(f) + str(s) + str(t))
            nums.append(qwq)
for f in nums:
    f1 = set(str(f))
    for s in nums:
        s1 = set(str(s))
        for t in nums:
            t1 = set(str(t))
            if t/f == 3 and s/f == 2 and len(f1 & s1) <= 0 and len(f1 & t1) <= 0 and len(t1 & s1) <= 0:
                print(f, s, t)
time_end = time.time()
time_c= time_end - time_start
print('time cost', time_c, 's')
