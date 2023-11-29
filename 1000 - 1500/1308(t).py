keyword = input().lower()
line = input().lower()
words = line.split()
if keyword in words:
    place = 0
    nums = words.count(keyword)
    for i in range(len(line)):
        abc = line[i]
        if abc == keyword[0]:
            if i != 0 and i != len(line)-len(keyword):
                fr = line[i-1]
                la = line[i+len(keyword)]
            else:
                fr = ' '
                la = ' '
            v = line[i:i+len(keyword)]
            if v == keyword and fr == la == ' ':
                place = i
                break
    print(nums, place)
else:
    print(-1)
