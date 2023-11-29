N = int(input())
alis = []
for _ in range(N):
    v = input().split()
    alis.append([v[0], int(v[1]), int(v[2]), int(v[3])])
ans = []
length = len(alis)

for student_n in range(length):
    student = alis[student_n]
    for adversary_n in range(student_n, length):
        adversary = alis[adversary_n]
        """
        if student != adversary:
            total = int(student[1])+int(student[2])+int(student[3])
            total1 = int(adversary[1]) + int(adversary[2]) + int(adversary[3])
            gap0 = abs(total1-total)
            gap1 = abs(int(adversary[1]) - int(student[1]))
            gap2 = abs(int(adversary[2]) - int(student[2]))
            gap3 = abs(int(adversary[3]) - int(student[3]))
            if gap0 <= 10 and gap1 <= 5 and gap2 <= 5 and gap3 <= 5:
                v_ans = sorted((student[0], adversary[0]))
        """
        if student != adversary:
            if -5 <= adversary[1] - student[1] <= 5:
                if -5 <= adversary[2] - student[2] <= 5:
                    if -5 <= adversary[3] - student[3] <= 5:
                        if -10 <= (student[1] + student[2] + student[3]) -\
                                (adversary[1] + adversary[2] + adversary[3]) <= 10:
                            v_ans = sorted((student[0], adversary[0]))
                            ans.append(v_ans)

for i in ans:
    print(i[0], end=' ')
    print(i[1])
