lenth = input().split()
a = float(lenth[0])
b = float(lenth[1])
c = float(lenth[2])
p = 0.5*(a+b+c)
qwq = p*(p-a)*(p-b)*(p-c)
area = pow(qwq,1/2)
print('%.1f'%area)