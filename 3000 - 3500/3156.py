n, m = map(int, input().split())
student_no = list(map(int, input().split()))
ask = list(map(int, input().split()))
for i in ask:
    print(student_no[i-1])
