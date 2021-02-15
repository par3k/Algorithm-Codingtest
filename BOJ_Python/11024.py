# 더하기 4
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    print(sum(arr))