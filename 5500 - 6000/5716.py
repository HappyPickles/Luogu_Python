qwq = input().split()
year, month = int(qwq[0]), int(qwq[1])


def leapyear(year):  # input years
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

def monthsdays(month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 'IsFebruary'


if monthsdays(month) != 'IsFebruary':
    print(monthsdays(month))
elif leapyear(year) is True:
    print(29)
else:
    print(28)
