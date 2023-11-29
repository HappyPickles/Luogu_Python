qwq = input().split()
m = float(qwq[0])
h = float(qwq[1])
BMI = m / (h*h)
if BMI < 18.5:
    print('Underweight')
elif 18.5 <= BMI < 24:
    print('Normal')
else:
    ans = '{:.6g}'.format(BMI)
    print(ans)
    print('Overweight')
