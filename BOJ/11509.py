# 풍선 맞추기
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))

h = [0] * 1000001
ans = 0

for i in range(n):
    if h[arr[i]+1]:
        h[arr[i]+1] -= 1
        h[arr[i]] += 1
    else:
        ans += 1
        h[arr[i]] += 1

print(ans)