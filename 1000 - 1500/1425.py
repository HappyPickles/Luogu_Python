t =input().split()
time = (60*((int(t[2]) - int(t[0])))) + (int(t[3]) - int(t[1]))
print(str(time // 60) + ' ' + str(time % 60))