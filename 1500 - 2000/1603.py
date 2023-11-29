inpt = input().lower().split()
nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
        'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
        'nineteen': 19, 'twenty': 20, 'a': 1, 'both': 2, 'another': 1, 'first': 1,
        'second': 2, 'third': 3}
have = []
for s in inpt:
    if s in nums:
        v = (nums[s]**2) % 100
        have.append('%s' % v if v >= 10 else '0%s' % v)

have.sort()
v = ''
for i in have:
    v = v+i
if v == '':
    print(0)
else:
    print(int(v))
