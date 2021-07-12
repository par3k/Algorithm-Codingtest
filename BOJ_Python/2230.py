# 수 고르기
import sys
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

left, right = 0, 0
answer = 2345678910

while left < n and right < n:
    if arr[right] - arr[left] < m:
        right += 1
    else:
        answer = min(answer, arr[right] - arr[left])
        left += 1

print(answer)