# 파도반 수열

import sys
input = lambda: sys.stdin.readline().rstrip()

p = [0, 1, 1, 1, 2, 2, 3, 4, 5]


def padovan_seq(n):
    for i in range(9, n+1):
        ans = p[i-5] + p[i-1]
        p.append(ans)
    return p


padovan_seq(1000)
for _ in range(int(input())):
    n = int(input())
    print(p[n])