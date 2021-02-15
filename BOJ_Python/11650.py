# 좌표 정렬하기

import sys
arr = []

for i in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append((a, b))


for i, j in sorted(arr):
    print(i, j)
