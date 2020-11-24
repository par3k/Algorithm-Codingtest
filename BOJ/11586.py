# 지영 공주님의 마법 거울
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [list(input()) for _ in range(n)]
k = int(input())

if k == 1:
    for i in range(n):
        print(''.join(arr[i]))

elif k == 2:
    tmp = [[''] * len(arr) for _ in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr)):
            tmp[i][n - 1 - j] = arr[i][j]

    ans = list(map(''.join, tmp))

    for i in ans:
        print(i)

elif k == 3:
    tmp = [[''] * len(arr) for _ in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr)):
            tmp[len(arr) - 1 - i][j] = arr[i][j]

    ans = list(map(''.join, tmp))

    for i in ans:
        print(i)
