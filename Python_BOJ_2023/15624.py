# 피보나치 수 7

n = int(input())

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b % 1000000007, (a + b) % 1000000007
        return b

print(fibo(n))