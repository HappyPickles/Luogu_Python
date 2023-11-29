k = int(input())
ans = 0
day = 0
days = 0
for a in range(k):
    day += 1
    for b in range(day):
        ans += day
        days += 1
        if days == k:
            break
    if days == k:
        break
print(ans)