Kwh = input()
kwh = int(Kwh)
price = 0
for i in range(1,kwh+1):
    if i <= 150:
        price += 0.4463
    elif 150 < i <=400:
        price += 0.4663
    elif 400 < i:
        price += 0.5663
print('%.1f' % price)
