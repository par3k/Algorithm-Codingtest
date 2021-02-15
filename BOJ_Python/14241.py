# 슬라임 합치기
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0

for _ in range(n-1):
    a = arr.pop(len(arr)-1)
    if len(arr) == 0:
        break
    ans += a * arr[len(arr)-1]
    arr[len(arr)-1] = a + arr[len(arr)-1]

print(ans)