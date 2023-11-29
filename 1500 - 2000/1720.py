n = int(input())
S5 = pow(5,1/2)
def Fbi(n):
    a = ((1+S5)/2)**n
    b = ((1-S5)/2)**n
    ans = (a-b)/S5
    return print('%.2f'% ans)
Fbi(n)