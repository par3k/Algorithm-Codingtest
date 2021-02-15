# 숫자 카드
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = set(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

for i in range(len(arr2)):
    if arr2[i] in arr:
        arr2[i] = 1
    else:
        arr2[i] = 0

for i in range(len(arr2)):
    print(arr2[i], end=' ')