import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split())


def pow(a, b, c):
    if b == 1:
        return a % c
    val = pow(a, b//2, c)
    val = val * val % c
    if b % 2 == 0:
        return val
    return val * a % c


print(pow(a, b, c))

