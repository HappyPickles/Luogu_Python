ab = input().split()
a = int(ab[0])
b = int(ab[1])


def is_prime(x):
    if x <= 1:
        return False
    else:
        for d in range(2, int(x**0.5)+1):
            if x % d == 0:
                return False
        return True


def is_plalindrome(x):
    v = []
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False


for i in range(a, b+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 and i != 5:
        continue
    if is_plalindrome(i) and is_prime(i):
        print(i)
    else:
        continue
