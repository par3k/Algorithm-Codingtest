# 알바생 강호
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=True)

tip = 0
ans = []

for i in range(n):
    tip = arr[i] - i

    if tip < 0:
        tip = 0
    ans.append(tip)

print(sum(ans))