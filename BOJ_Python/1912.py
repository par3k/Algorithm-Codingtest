# 연속합
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))

sum = [arr[0]]

for i in range(n-1):
    sum.append(max(sum[i] + arr[i+1], arr[i+1]))
print(max(sum))