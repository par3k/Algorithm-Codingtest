# 제로
import sys
input = lambda :sys.stdin.readline().rstrip()

arr = list()
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        arr.pop()
    elif n != 0:
        arr.append(n)

print(sum(arr))