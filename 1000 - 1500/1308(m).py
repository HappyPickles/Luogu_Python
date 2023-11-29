keyword = input().lower()
line = input().lower()
place = 0
nums = 0
for i in range(len(line)):
    abc = line[i]
    if abc == keyword[0]:
        if i != 0 and i != len(line)-len(keyword)+1:
            fr = line[i-1]
            la = line[i+len(keyword)]
        else:
            fr = ' '
            la = ' '
        v = line[i:i+len(keyword)]
        if v == keyword and fr == la == ' ':
            if place == 0:
                place = i
            nums += 1
if nums != 0:
    print(nums, place)
else:
    print(-1)
