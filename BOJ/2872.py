# 우리집엔 도서관이 있어
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [int(input()) for _ in range(n)]
ans = n

for i in range(n-1, -1, -1):
    if arr[i] == ans:
        ans -= 1

print(ans)