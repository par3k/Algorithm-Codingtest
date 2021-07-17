# 최대공약수와 최소공배수
a, b = map(int, input().split())


def gcd(a, b):
    if a % b == 0: return b
    else: return gcd(b, a % b)


if a > b:
    gcd = gcd(a, b)
    lcm = (a * b) // gcd
    print(gcd)
    print(lcm)
else:
    gcd = gcd(b, a)
    lcm = (a * b) // gcd
    print(gcd)
    print(lcm)