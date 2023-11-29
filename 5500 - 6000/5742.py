N = int(input())
alis = []
for _ in range(N):
    alis.append(list(map(int, input().split())))
for student in alis:
    if student[1]+student[2] > 140:
        if student[1] * 0.7 + student[2] * 0.3 >= 80:
            print("Excellent")
        else:
            print("Not excellent")
    else:
        print("Not excellent")

