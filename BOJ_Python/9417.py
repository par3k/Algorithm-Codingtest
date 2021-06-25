# 최대 GCD
from math import gcd

n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    max_gcd = 1
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            this_gcd = gcd(arr[i], arr[j])
            if this_gcd > max_gcd:
                max_gcd = this_gcd
    print(max_gcd)