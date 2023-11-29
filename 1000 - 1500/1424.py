week, days = list(map(int, input().split()))
num = 0
for _ in range(days):
    if week != 6 and week != 7:
        num += 1
    if week == 7:
        week = 0
    week += 1
print(250*num)
