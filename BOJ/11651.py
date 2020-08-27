# 좌표 정렬하기2
import sys
arr = []

for i in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append((b, a))


for i, j in sorted(arr):
    print(j, i)
