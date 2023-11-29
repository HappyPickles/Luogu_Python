n = int(input())
# ans == C4n
up = 1
down = 1

if n < 4:
    print(0)
else:
    for i in range(n, 4, -1):
        up *= i
    for i in range(1, (n-4)+1):
        down *= i
    ans = int(up/down)
    print(ans)
