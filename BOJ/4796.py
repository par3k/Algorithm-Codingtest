# 캠핑

import sys
input = lambda : sys.stdin.readline().rstrip()

cnt = 0
while True:
    cnt += 1
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0: break

    vacation = (V//P) * L + min(L, V - (V//P) * P)
    print(f'Case {cnt}: {vacation}')
