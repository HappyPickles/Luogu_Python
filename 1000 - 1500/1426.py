s, x = list(map(int, input().split()))
fi = 7
l = s - x
r = s + x
lens = 0
key = 1
for i in range(100):
    if l <= lens <= r and l <= lens+fi <= r:
        print('y')
        key = 0
        break
    lens += fi
    fi *= 0.98
if key == 1:
    print('n')
