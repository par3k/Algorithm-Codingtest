# 이친수
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
d = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]


print(fibo(n))