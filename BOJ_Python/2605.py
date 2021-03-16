# 줄 세우기
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
cmd = list(map(int, input().split()))
arr = []

for i in range(1, n + 1):
    arr.insert(len(arr) - cmd[i - 1], i) # insert 함수 처음 봄...

for i in arr:
    print(i, end=' ')