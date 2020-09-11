# 저울
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr)
ans = 1

for i in range(n):
    if ans < arr[i]:
        break
    ans += arr[i]

print(ans)