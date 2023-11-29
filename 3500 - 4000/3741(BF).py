n = int(input())
s = input().strip('\r')


def BF(sr: str, ns: int) -> int:
    alis = [sr.count('VK')]
    for i in range(ns):
        if sr[i] == 'V':
            vsr = 'K'
        else:
            vsr = 'V'
        v = sr[0:i] + vsr + sr[i+1:ns]
        alis.append(v.count('VK'))
    return max(alis)


print(BF(s, n))
