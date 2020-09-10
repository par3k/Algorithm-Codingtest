# 신입 사원

import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    arr = []
    n = int(input())

    for _ in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort(key = lambda x : x[0])

    tmp = arr[0][1]
    ans = 0

    for i in range(1, n):
        if arr[i][1] > tmp:
            ans += 1
        else:
            tmp = arr[i][1]

    print(n - ans)