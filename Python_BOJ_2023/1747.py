# 소수&팰린드롬
import math
n = int(input())

def chk_primarynum(num):
    sqrt_num = int(math.sqrt(num))
    if num == 1:
        return False

    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            return False # 소수가 아님
    return True # 소수임

def chk_pelindrome(num):
    val = str(num)
    reverse_val = val[::-1]

    if val == reverse_val:
        return True # 팰린드롬임
    else:
        return False # 팰린드롬이 아님

while True:
    if chk_pelindrome(n) and chk_primarynum(n):
        print(n)
        exit()
    n += 1