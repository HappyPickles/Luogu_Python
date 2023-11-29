def leap_year(year):  # input years
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False


a, b = map(int, input().split())
ans = []
cont = 0
for y in range(a, b+1):
    if leap_year(y):
        ans.append(y)
        cont += 1

print(cont)
for i in ans:
    print(i, end=' ')
