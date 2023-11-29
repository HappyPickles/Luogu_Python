n = int(input())
point = list(map(int, input().split()))
point.remove(max(point))
point.remove(min(point))
n -= 2
ans = sum(point)/n
print('%.2f' % ans)
