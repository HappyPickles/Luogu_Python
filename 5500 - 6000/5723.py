L = int(input())
cont = 0
num_sum = 0


def is_prime(n):
    if n <= 1:
        return False
    for a_num in range(2, int(n**0.5) + 1):
        #  判断是否能被2到 开根号n 整除 不需要判断到n-1
        if n % a_num == 0:
            return False
    return True


for i in range(1, L+1):
    if is_prime(i) and num_sum+i <= L:
        num_sum += i
        cont += 1
        print(i)
    if num_sum+i > L:
        break
print(cont)
