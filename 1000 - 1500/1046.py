high = input().split()
long = input()
bandeng = 30
highest = int(long) + int(bandeng)
ans = 0
for i in high:
    if highest >= int(i):
        ans += 1
print(ans)