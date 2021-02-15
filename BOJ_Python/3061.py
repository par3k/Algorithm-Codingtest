# 사다리
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    for j in range(n):
        for i in range(j):
            if arr[i] > arr[j]:
                cnt += 1
    print(cnt)