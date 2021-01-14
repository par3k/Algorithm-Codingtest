# 끝말잇기
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
data = list(map(str, input().split()))
arr = set()

for i in range(N):
    arr.add(data[i][0])

print(1 if len(arr) == 1 else 0)