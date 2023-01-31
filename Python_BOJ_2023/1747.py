# 소수&팰린드롬
import math
n = int(input())

def chk_primarynum(num):
    sqrt_num = int(math.sqrt(num))
    if num <= 1:
        return False # 소수가 아님

    if num % 2 == 0:
        if num == 2:
            return True
        else:
            return False

    for i in range(3, sqrt_num):
        if num % i == 0:
            return False # 소수가 아님
    return True # 소수임

def chk_pelindrome(num):
    val = list(map(str, str(num)))
    reverse_val = val[::-1]

    if val == reverse_val:
        return True # 팰린드롬임
    else:
        return False # 팰린드롬이 아님

for i in range(n, 10 ** 6):
    if chk_pelindrome(i) and chk_primarynum(i):
        print(i)
        exit()