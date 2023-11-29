astr = input()
cont = 0
for i in astr:
    if i == ' ':
        continue
    elif i == '\n':
        continue
    else:
        cont += 1
print(cont)

