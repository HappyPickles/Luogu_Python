n = input()
b = 'boy'
g = 'girl'
a1 = n.count('boy')
a2 = n.count('bo') - a1
a3 = n.count('oy') - a1
a4 = n.count('b') - a2 - a1
a5 = n.count('o') - a2 - a3 - a1
a6 = n.count('y') - a3 - a1

bs = a1 + a2 + a3 + a4 + a5 + a6
print(bs)

b1 = n.count('girl')
b2 = n.count('gir') - b1
b3 = n.count('irl') - b1
b4 = n.count('gi') - b1 - b2
b5 = n.count('ir') - b1 - b2 - b3
b6 = n.count('rl') - b1 - b3
b7 = n.count('g') - b1 - b2 - b4
b8 = n.count('i') - b1 - b2 - b3 - b4 - b5
b9 = n.count('r') - b1 - b2 - b3 - b5 - b6
b10 = n.count('l') - b1 - b3 - b6

gs = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10
print(gs)
