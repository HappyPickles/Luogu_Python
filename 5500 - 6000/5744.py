n = int(input())
alis = []
for _ in range(n):
    alis.append(input().split())
for student in alis:
    student[1] = int(student[1]) + 1
    if int(student[2]) * 1.2 >= 600:
        student[2] = 600
    else:
        student[2] = int(int(student[2])*1.2)
for i in alis:
    for j in i:
        print(j, end=' ')
    print()
