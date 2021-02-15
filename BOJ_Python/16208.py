# 귀찮음
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
ans = 0

for i in range(n-1):
    a = arr.pop(len(arr)-1)
    if len(arr) == 0:
        break
    ans += sum(arr) * a


print(ans)